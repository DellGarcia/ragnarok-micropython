# This example demonstrates a peripheral implementing the Nordic UART Service (NUS).

import bluetooth
from micropython import const

from app.ble.ble_advertising import advertising_payload


_IRQ_CENTRAL_CONNECT = const(1)
_IRQ_CENTRAL_DISCONNECT = const(2)
_IRQ_GATTS_WRITE = const(3)

_FLAG_WRITE = const(0x0008)
_FLAG_NOTIFY = const(0x0010)

_UART_UUID = bluetooth.UUID('dd17e794-3b63-4548-9e9c-94eb2ed7bfee')
_UART_TX = (bluetooth.UUID('2e705a53-4a16-46bb-9c31-0ce91f152f43'), _FLAG_NOTIFY,)
_UART_RX = (bluetooth.UUID('c85b3aac-29a0-4467-9647-b18344086a86'), _FLAG_WRITE,)
_UART_SERVICE = (_UART_UUID, (_UART_TX, _UART_RX),)

# org.bluetooth.characteristic.gap.appearance.xml
_ADV_APPEARANCE_GENERIC_COMPUTER = const(128)


class BLEUART:
    def __init__(self, ble, name='ragnarok', rxbuf=100):
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        ((self._tx_handle, self._rx_handle),) = self._ble.gatts_register_services((_UART_SERVICE,))

        # Increase the size of the rx buffer and enable append mode.
        self._ble.gatts_set_buffer(self._rx_handle, rxbuf, True)
        self._connections = set()
        self._rx_buffer = bytearray()
        self._handler = None

        # Optionally add services=[_UART_UUID], but this is likely to make the payload too large.
        self._payload = advertising_payload(name=name, appearance=_ADV_APPEARANCE_GENERIC_COMPUTER)
        self._advertise()

    def irq(self, handler):
        self._handler = handler

    def _irq(self, event, data):
        # Track connections so we can send notifications.
        if event == _IRQ_CENTRAL_CONNECT:
            conn_handle, _, _ = data
            self._connections.add(conn_handle)
        elif event == _IRQ_CENTRAL_DISCONNECT:
            conn_handle, _, _ = data

            if conn_handle in self._connections:
                self._connections.remove(conn_handle)

            # Start advertising again to allow a new connection.
            self._advertise()
        elif event == _IRQ_GATTS_WRITE:
            conn_handle, value_handle = data
            if conn_handle in self._connections and value_handle == self._rx_handle:
                self._rx_buffer += self._ble.gatts_read(self._rx_handle)
                if self._handler:
                    self._handler()

    def any(self):
        return len(self._rx_buffer)

    def read(self, sz=None):
        if not sz:
            sz = len(self._rx_buffer)
        result = self._rx_buffer[0:sz]
        self._rx_buffer = self._rx_buffer[sz:]
        return result

    def write(self, data):
        for conn_handle in self._connections:
            self._ble.gatts_notify(conn_handle, self._tx_handle, data)

    def close(self):
        for conn_handle in self._connections:
            self._ble.gap_disconnect(conn_handle)
        self._connections.clear()

    def _advertise(self, interval_us=500000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload)


def demo():
    import time

    ble = bluetooth.BLE()
    uart = BLEUART(ble)

    def on_rx():
        print('rx: ', uart.read().decode().strip())

    uart.irq(handler=on_rx)
    nums = [4, 8, 15, 16, 23, 42]
    i = 0

    try:
        while True:
            uart.write(str(nums[i]) + '\n')
            i = (i + 1) % len(nums)
            time.sleep_ms(1000)
    except KeyboardInterrupt:
        pass

    uart.close()

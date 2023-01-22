from machine import Pin

led = Pin(2, Pin.OUT)


def connectToWifiAndUpdate():
    import time, machine, network, gc, app.secrets as secrets

    led.value(1)
    time.sleep(1)
    print('Memory free', gc.mem_free())

    from app.ota_updater import OTAUpdater

    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(secrets.WIFI_SSID, secrets.WIFI_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    otaUpdater = OTAUpdater('https://github.com/DellGarcia/ragnarok-micropython', main_dir='app', secrets_file="secrets.py")
    hasUpdated = otaUpdater.install_update_if_available()
    if hasUpdated:
        machine.reset()
    else:
        del(otaUpdater)
        gc.collect()

def startApp():
    from app.main import run
    led.value(0)
    run()

connectToWifiAndUpdate()
startApp()

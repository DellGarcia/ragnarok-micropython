<h1 align="center">
  Ragnarok Micropython
</h1>

<p align="center">
  <a href="#" target="blank">
    <!--<img src="https://camo.githubusercontent.com/c8ea1110aab43014bb8d5f86c84f82881f9847f2ea92a6ca6c7e511d06d7339c/68747470733a2f2f662e636c6f75642e6769746875622e636f6d2f6173736574732f3733353030382f313834353232392f37373338666530612d373537392d313165332d383466342d3762313261613462323939622e706e67" width="250" alt="MicroPython" />-->
    <img src="https://user-images.githubusercontent.com/49599535/217877950-45471c18-cbb8-4772-8c46-fd1ecfa6a13a.png" width="800" alt="Ragnarok" />
  </a>
</p>

<p align="center">
  Line follower cart built using Micropython and ESP32 firmware
</p>

## Built With
- [MicroPython - ESP32 v1.19.1][micropython]

## Cart Parts
| Name | Image | Name | Image |
| --- | --- | --- | --- |
| ESP32 x1 | <img src="https://w7.pngwing.com/pngs/200/964/png-transparent-microcontroller-esp8266-nodemcu-esp32-wi-fi-wemos-d1-mini-electronics-internet-electronic-device-thumbnail.png" width="150"> | InfraRed TCRT5000 x3 | <img src="https://www.curtocircuito.com.br/pub/media/catalog/product/m/_/m_dulo_sensor_ptico_-_segue_faixa_-_tcrt5000_4.jpg" width="150"> |
| Bridge H L298N x1 | <img src="https://www.eletronicafaria.com.br/1339-thickbox_default/modulo-ponte-h-dupla-l298n-arduino.jpg" width="150"> | DC Motor 3V-6V x2 | <img src="https://http2.mlstatic.com/D_NQ_NP_825620-MLB49469570426_032022-O.webp" width="150"> |
| Battery 18650 x4 | <img src="https://m.media-amazon.com/images/I/51UawMqTuxL.jpg" width="150"> | HC-SR04 Ultrasonic x1 | <img src="https://http2.mlstatic.com/D_NQ_NP_836363-MLB31143102699_062019-W.jpg" width="150"> |

<br>

## Getting Started
For the use of the project, some prerequisites will be necessary.

### Prerequisites
* Thonny IDE
    1. You can download here: [Thonny][thonny_url]
    2. Here is a step-by-step installation tutorial. [(Windows)][thonny_tutorial_windows]
* MicroPython Firmware
    1. You can download here: [MicroPython Firmware][micropython_firmware_url]
    2. Here is a step-by-step installation tutorial. [(For ESP32 with Thonny IDE)][micropython_tutorial]


## Roadmap
- [x] Buy the parts 🙏
- [x] Assemble the cart
- [ ] Line-following logic
    - [x] IR digital reading
    - [ ] Stop when encountering an obstacle
    - [x] Fix route when a sensor activates
    - [x] Finite State Machine
- [ ] Bluetooth Module
    - [ ] Control via DualSense
    - [ ] Control via Flutter app


## Acknowledgments
Here in this [link][acknowledgments_url] you can see all the material I used to build the project. 😉


## Contributors
| [<div><img width=115 src="https://avatars.githubusercontent.com/u/54884313?v=4"><br><sub>Alexandre Ferreira de Lima</sub></div>][arekushi] <div title="Code">💻</div> | [<div><img width=115 src="https://avatars.githubusercontent.com/u/49599535?v=4"><br><sub>Lucas Del Puerto Garcia</sub></div>][dellgarcia] <div title="Code and Component assembly">💻🔧</div> |
| :---: | :---: |

<!-- [Build With] -->
[micropython]: https://micropython.org/download/esp32/

<!-- [Some links] -->
[thonny_url]: https://thonny.org/
[thonny_tutorial_windows]: https://www.youtube.com/watch?v=rI2Zl0ZJCzY

[micropython_firmware_url]: https://micropython.org/download/
[micropython_tutorial]: https://www.youtube.com/watch?v=EOa-qegjIBs

<!-- Acknowledgments-->
[acknowledgments_url]: https://arekushi.notion.site/Acknowledgments-6860cfac100948328b7fd09286b8c188

<!-- [Constributors] -->
[arekushi]: https://github.com/Arekushi
[dellgarcia]: https://github.com/DellGarcia

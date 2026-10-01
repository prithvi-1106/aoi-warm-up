# AOI Hardware

## Current Rebuild

The original physical AOI prototype was dismantled. The rebuild currently has the two core components needed to reconstruct the physical face:

| Component | Quantity | Purpose |
|---|---:|---|
| Arduino Uno | 1 | Microcontroller / serial hardware controller |
| SSD1306 I2C OLED | 1 | AOI physical face |
| USB cable | 1 | Power and serial communication |
| Jumper wires | 4+ | OLED power and I2C connections |

## OLED Interface

AOI uses a 128×64 SSD1306 OLED over I2C.

For an Arduino Uno, the conventional I2C pins are:

- **SDA → A4**
- **SCL → A5**

Power connections:

- **GND → GND**
- **VCC → the voltage supported by the specific OLED breakout**

The current hardware test successfully renders the AOI face.

## Current Target Wiring

| OLED | Arduino Uno |
|---|---|
| GND | GND |
| VCC | 5V* |
| SDA | A4 |
| SCL | A5 |

*Confirm the exact OLED module specification before reconnecting power.*

## Communication

The AOI Python controller opens the Arduino serial port at:

```text
9600 baud
```

The firmware accepts one ASCII character per state:

```text
0 sleep
1 idle
2 thinking
3 talking
4 happy
5 sad
6 confused
```

## Physical Rebuild Evidence

Session 1 evidence is stored under `media/`.

- [Session 1 working hardware photo](../media/session-01-working-face.jpg)
- [Session 1 reconstruction notes](session-01-hardware-rebuild.md)

## Future Hardware

The original complete prototype also used:

- Windows laptop
- PC webcam
- Realme smartphone as a Wi-Fi microphone through WO Mic
- USB-connected Arduino
- SSD1306 OLED

Those parts will be reintroduced only after the physical display layer is stable.

# Session 1 — Hardware Reconstruction

**Goal:** rebuild the minimum physical AOI interface and verify that the Arduino Uno can control the SSD1306 OLED.

## Session Objective

The original AOI hardware was dismantled, so the first rebuild session intentionally starts from the two surviving core components:

- Arduino Uno
- SSD1306 I2C OLED

The objective is not to rebuild the entire AI system yet. The objective is to prove the physical display layer first.

## Components Identified

| Component | Qty | Role |
|---|---:|---|
| Arduino Uno | 1 | Microcontroller and serial interface |
| SSD1306 OLED | 1 | Physical AOI face |
| USB cable | 1 | Arduino power + USB serial |
| Jumper wires | 4+ | I2C and power connections |

The OLED shown in the session photos is a small I2C SSD1306-style module with four connections.

## Wiring

The AOI firmware expects I2C communication.

| OLED pin | Arduino Uno pin | Purpose |
|---|---|---|
| GND | GND | Ground |
| VCC | 5V* | OLED power |
| SDA | A4 | I2C data |
| SCL | A5 | I2C clock |

\* Check the exact OLED breakout's VCC specification before reconnecting it. The current module is already operating successfully in this rebuild.

### Wiring Notes

- Do not connect SDA/SCL to arbitrary digital pins; the Uno's conventional I2C pins are A4 and A5.
- Keep the USB cable connected to the Arduino for both power and serial communication.
- The Python prototype previously used **9600 baud** for serial communication.
- The OLED address used by the firmware is **0x3C**.

## Firmware Baseline

The previous AOI firmware defines these states:

```text
0 = Sleep
1 = Idle
2 = Thinking
3 = Talking
4 = Happy
5 = Sad
6 = Confused
```

The Arduino receives a single ASCII character over serial and converts it into the corresponding face state.

The display is refreshed continuously and includes an automatic blinking mechanism for several states.

## What Was Tested

The physical display was reconnected to the Arduino and the AOI face was successfully displayed.

### Evidence

![AOI Arduino and SSD1306 showing the working face](../media/session-01-working-face.jpg)

The photo records the reconstructed physical interface with the Arduino powered over USB and the OLED actively rendering the AOI face.

## Result

**Session 1 physical milestone: COMPLETE.**

The core display path is working:

```
Arduino Uno
    │
    ├── USB power / serial
    │
    └── I2C
         ├── SDA → A4
         └── SCL → A5
              ↓
          SSD1306 OLED
              ↓
          AOI face
```

This gives the project a verified hardware baseline for the next sessions.

## What Comes Next

Session 2 should move from "the face works" to a reproducible firmware project:

1. create the Arduino firmware folder with the final sketch,
2. record the exact library versions,
3. test every face state individually,
4. test serial commands `0` through `6`,
5. capture a photo of at least two different expressions,
6. document any animation bugs before reconnecting the Python system.

## Documentation Evidence Checklist

- [x] Component photo
- [x] Working Arduino + OLED photo
- [x] Wiring recorded
- [x] Firmware state map recorded
- [x] Session result recorded
- [ ] Individual state test evidence
- [ ] Final wiring close-up

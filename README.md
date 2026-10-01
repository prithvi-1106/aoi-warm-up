# AOI — Physical AI Companion

I am rebuilding AOI as a personal physical-AI project, starting from the hardware layer and moving upward into the desktop AI stack. AOI is a desktop AI companion that connects a multimodal Python software stack to a physical OLED face driven by an Arduino Uno.

The original AOI prototype combined:
- webcam vision through OpenCV
- voice input through SpeechRecognition / PyAudioWPatch
- cloud AI through Groq
- neural speech through edge-tts
- serial communication with an Arduino Uno
- SSD1306 OLED facial animations
- a lightweight Tkinter text console

This repository documents the rebuild from the physical hardware upward.

## Rebuild Status

| Stage | Status |
|---|---|
| Arduino Uno available | ✅ |
| SSD1306 OLED available | ✅ |
| OLED wired and powered | ✅ |
| OLED face firmware tested | ✅ |
| Python desktop pipeline | ⏳ |
| Vision pipeline | ⏳ |
| Voice / wake-word pipeline | ⏳ |
| Emotion-to-face pipeline | ⏳ |
| Full AOI integration | ⏳ |

## Repository Structure

```
.
├── docs/
│   ├── development-log.md
│   ├── hardware.md
│   ├── project-spec.md
│   ├── serial-protocol.md
│   └── session-01-hardware-rebuild.md
├── firmware/
├── media/
├── src/
└── tools/
```

## Hardware

The current rebuild starts with:

- Arduino Uno
- SSD1306 I2C OLED, 128×64
- USB cable
- jumper wires

The standard Arduino Uno I2C pins used by the AOI firmware are:

| OLED | Arduino Uno |
|---|---|
| GND | GND |
| VCC | 5V or the voltage specified by the OLED module |
| SDA | A4 |
| SCL | A5 |

**Important:** verify the OLED module's VCC marking before applying power. The wiring table describes the current AOI target configuration, not a universal rule for every SSD1306 breakout.

## AOI Face States

The firmware uses one-character serial commands:

| Code | State |
|---:|---|
| 0 | Sleep |
| 1 | Idle |
| 2 | Thinking |
| 3 | Talking |
| 4 | Happy |
| 5 | Sad |
| 6 | Confused |

## Session Documentation

Session 1 establishes the physical baseline and records evidence that the Arduino can drive the OLED face.

See [Session 1 — Hardware Reconstruction](docs/session-01-hardware-rebuild.md).

## Media

The first hardware test photo is stored in `media/session-01-working-face.jpg`.

![AOI Arduino + SSD1306 working face](media/session-01-working-face.jpg)

## Original Software Stack

Python packages used by the previous AOI prototype:

- opencv-python
- pyserial
- edge-tts
- playsound3
- groq
- SpeechRecognition
- pyaudiowpatch

Arduino libraries:

- Adafruit GFX Library
- Adafruit SSD1306
- Wire.h

The original prototype code is being reconstructed and improved incrementally rather than copied into the repository all at once.

## Development Philosophy

Each rebuild session should leave behind three things:

1. a working technical milestone,
2. evidence such as photos, screenshots, or serial logs,
3. a short development record explaining what changed and why.

This keeps the project reproducible and makes the final build easier to understand.

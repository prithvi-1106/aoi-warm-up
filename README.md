# AOI — Physical AI Companion

I am rebuilding AOI as a personal physical-AI project, starting from the hardware layer and moving upward into the desktop AI stack.

The original prototype combined a webcam, speech recognition, a cloud multimodal model, neural text-to-speech, an Arduino-controlled OLED face, and a small desktop console. This repository is the structured rebuild of that system, with each development stage recorded as a separate session.

## Current Status

| Area | Status |
|---|---|
| Arduino Uno | Working |
| SSD1306 128×64 OLED | Working |
| I2C communication | Working |
| Animated AOI face | Working |
| Serial face-state control | Working |
| Python emotion control GUI | Working |
| Python assistant | Prototype |
| Webcam vision | Prototype |
| Speech recognition | Prototype |
| Neural TTS | Prototype |
| Multimodal AI | Prototype |
| Full integration | In progress |

## System Overview

AOI is being developed as a layered system:

- **Hardware:** Arduino Uno + SSD1306 OLED
- **Vision:** OpenCV
- **Voice input:** SpeechRecognition + PyAudioWPatch
- **AI:** Groq multimodal API
- **Voice output:** Edge TTS
- **Desktop UI:** Tkinter
- **Communication:** Python serial connection to Arduino
- **Expression system:** OLED face states controlled by Arduino firmware

The OLED is the first physical output interface. The objective is to make the physical and software layers operate as one assistant.

## Session 1 — Hardware Reconstruction

The first rebuild session focused on the minimum working physical interface.

![AOI hardware](media/session-01-working-face.jpg)

The connected hardware evidence records the Arduino Uno driving the SSD1306 OLED face.

The current I2C wiring is:

| OLED | Arduino Uno | Function |
|---|---|---|
| GND | GND | Ground |
| VCC | 5V* | Power |
| SDA | A4 | I2C data |
| SCL | A5 | I2C clock |

*The OLED breakout's voltage specification should be checked before applying power.*

**Session 1 result:** the physical AOI face is working.

[Read the full Session 1 documentation](docs/session-01-hardware-rebuild.md).

## Session 2 — Python ↔ Arduino Emotion Control

The second session connected the Python layer to the working Arduino face.

The bridge uses:

`Python → USB serial → Arduino → I2C → OLED`

The Arduino accepts the same seven face states:

| Command | State |
|---:|---|
| 0 | Sleep |
| 1 | Idle |
| 2 | Thinking |
| 3 | Talking |
| 4 | Happy |
| 5 | Sad |
| 6 | Confused |

I also added a small Tkinter control window so I can type a state number and immediately update AOI's physical expression.

The seven states were tested individually and are working through the Python-to-Arduino path.

[Read the full Session 2 documentation](docs/session-02-python-arduino-emotions.md).

## OLED Face Protocol

The Arduino firmware accepts one ASCII character at a time over serial at **9600 baud**.

The firmware also includes automatic blinking for selected states.

## Software Stack

### Python

- opencv-python
- pyserial
- edge-tts
- playsound3
- groq
- SpeechRecognition
- pyaudiowpatch
- tkinter

Standard-library modules used by the prototype include time, sys, base64, re, threading, asyncio, and tkinter.

### Arduino

- Adafruit GFX Library
- Adafruit SSD1306
- Wire.h

## Repository Structure

    .
    ├── docs/
    ├── firmware/
    ├── media/
    ├── src/
    └── tools/

Documentation, firmware, source code, and physical-build evidence are kept separate so the rebuild remains easy to follow.

## Development Method

I am documenting the project as a sequence of development sessions. Each session records:

1. objective
2. hardware or software changes
3. connections and configuration
4. code and library requirements
5. test result
6. photographic or screen evidence
7. problems discovered
8. next step

This repository is therefore both the project source and the development record.

## Next Milestone

The next stage is to connect the emotion controller to the main Python assistant so that AOI can change its physical expression automatically while thinking, speaking, listening, and responding.

## Security

API keys and credentials are kept out of the repository. The previous Python prototype uses a placeholder for the Groq API key and must be configured locally.

## Documentation

- [Hardware documentation](docs/hardware.md)
- [Serial protocol](docs/serial-protocol.md)
- [Project specification](docs/project-spec.md)
- [Development log](docs/development-log.md)
- [Session 1 — Hardware Reconstruction](docs/session-01-hardware-rebuild.md)
- [Session 2 — Python ↔ Arduino Emotion Control](docs/session-02-python-arduino-emotions.md)

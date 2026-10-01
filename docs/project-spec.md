# AOI Project Specification

## Overview

AOI is a desktop AI companion with a physical OLED face. The computer handles multimodal AI, voice, vision, text-to-speech, and user interaction while the Arduino controls the physical display.

## Rebuild Goal

Reconstruct and improve AOI's physical interface after the original hardware setup was dismantled.

## Rebuild Order

1. Arduino + OLED
2. OLED face rendering
3. Serial communication
4. Python hardware controller
5. Emotion mapping
6. TTS
7. Voice interaction
8. Vision
9. Wake/sleep behavior
10. Full integration

## Target Hardware

- Arduino Uno
- SSD1306 OLED
- USB connection to Windows PC
- PC webcam
- Smartphone microphone setup

## Target Software

- Python
- Arduino C++
- OpenCV
- SpeechRecognition
- PyAudioWPatch
- edge-tts
- playsound3
- Groq API
- Tkinter

## Emotional States

| State | Code |
|---|---:|
| Sleep | 0 |
| Idle | 1 |
| Thinking | 2 |
| Talking | 3 |
| Happy | 4 |
| Sad | 5 |
| Confused | 6 |

This mapping is provisional until the firmware is rebuilt and tested.

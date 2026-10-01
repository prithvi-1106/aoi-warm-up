# Session 2 — Python ↔ Arduino Emotion Control

## Goal

The OLED face is working on the Arduino. The next step is to connect the Python layer to the Arduino so that a Python-controlled emotion can directly change the physical AOI face.

For this session I kept the bridge deliberately small:

```
Python
  │
  │ USB serial / 9600 baud
  ▼
Arduino C++
  │
  │ I2C
  ▼
SSD1306 OLED
```

## Emotion Protocol

| Python command | Emotion | Arduino state |
|---:|---|---|
| `0` | Sleep | Sleep |
| `1` | Idle | Idle |
| `2` | Thinking | Thinking |
| `3` | Talking | Talking |
| `4` | Happy | Happy |
| `5` | Sad | Sad |
| `6` | Confused | Confused |

## Python Control GUI

I added a small Tkinter control window to test the physical expression system manually.

The GUI:

- opens the Arduino serial connection,
- accepts a number from 0 to 6,
- sends that ASCII command to the Arduino,
- shows the selected emotion in a chat-style log,
- updates the current-emotion label.

This keeps the first Python ↔ Arduino test separate from the larger AI assistant.

## Files

- `firmware/aoi_face/aoi_face.ino` — Arduino C++ face controller.
- `src/python/aoi_emotion_bridge.py` — Python serial connection and Tkinter emotion controller.

## Test Procedure

1. Upload the Arduino sketch to the Uno.
2. Keep the USB cable connected.
3. Close Arduino Serial Monitor before running Python.
4. Confirm that `PORT = "COM8"` matches the Arduino port on my PC.
5. Install PySerial in the project Python environment.
6. Run:

```bash
python src/python/aoi_emotion_bridge.py
```

7. Enter each command from 0 through 6 in the GUI.

## Result

All seven supported emotions were tested and the OLED face updated correctly for each command.

The verified path is:

```
Tkinter GUI
    ↓
PySerial
    ↓
COM8 / 9600 baud
    ↓
Arduino
    ↓
SSD1306 OLED
```

At this point the AI model is not involved yet. This is an isolated hardware/software integration test.

## What Comes Next

The next step is to call the same face-state controller from the main Python assistant so the physical face can react automatically to listening, thinking, speaking, and response emotions.

## Security

The Groq API key is not part of this bridge. Credentials stay in local environment variables or a local `.env` file and must not be committed to GitHub.

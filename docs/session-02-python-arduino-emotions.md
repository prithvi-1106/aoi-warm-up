# Session 2 — Python ↔ Arduino Emotion Bridge

## Goal

The OLED face is already working on the Arduino. The next step is to connect the Python layer to the Arduino so that a Python emotion can directly change the physical AOI face.

For this session I am keeping the bridge deliberately small:

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

## Emotion protocol

| Python emotion | Serial command | Arduino state |
|---|---:|---|
| sleep | `0` | Sleep |
| idle | `1` | Idle |
| thinking | `2` | Thinking |
| talking | `3` | Talking |
| happy | `4` | Happy |
| sad | `5` | Sad |
| confused | `6` | Confused |

## Files

- `firmware/aoi_face/aoi_face.ino` — Arduino C++ face controller.
- `src/python/aoi_emotion_bridge.py` — Python serial/emotion controller.

## First test

1. Upload the Arduino sketch to the Uno.
2. Keep the USB cable connected.
3. Close Arduino Serial Monitor before running Python, because only one program should own the COM port at a time.
4. Check that `PORT = "COM8"` matches the Arduino port on my PC.
5. Run:

```bash
python src/python/aoi_emotion_bridge.py
```

The script sends every supported emotion one by one with a short delay.

## Expected result

The OLED should change through:

```
sleep → idle → thinking → talking → happy → sad → confused
```

At this point the AI model is not involved yet. This is an isolated hardware/software integration test. Once this works reliably, the same `set_emotion()` function can be called from the voice, vision, and TTS code.

## Important

The Groq API key is not part of this bridge. Credentials should stay in local environment variables or a local `.env` file and must not be committed to GitHub.

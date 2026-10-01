# AOI Development Log

This file records the rebuild chronologically so the final documentation can be based on real engineering work.

## 2026-10-01 - Repository setup

### Completed

- Created the project documentation plan.
- Defined the hardware-first rebuild order.
- Added initial hardware and serial protocol documentation.

## 2026-10-01 - Session 1: Hardware reconstruction

### Completed

- Reconnected the Arduino Uno and SSD1306 OLED.
- Recorded the I2C wiring.
- Confirmed the working OLED face.
- Recorded the serial settings and face-state protocol.
- Added the first physical-build evidence to the repository.

### Result

The minimum physical AOI face is working.

## 2026-10-01 - Session 2: Python ↔ Arduino emotion control

### Completed

- Added the Arduino face firmware project.
- Added the Python serial emotion bridge.
- Added a small Tkinter emotion-control GUI.
- Connected Python to the Arduino over COM8 at 9600 baud.
- Tested all seven face-state commands individually.
- Confirmed that every supported state updates the physical OLED face.

### Result

The Python → serial → Arduino → OLED emotion pipeline is working.

### Next

- Connect the emotion controller to the main Python assistant.
- Map assistant actions and model emotion tags to the seven physical face states.
- Reintroduce voice, vision, and TTS incrementally after the hardware control path remains stable.

# AOI Serial Protocol

## State Commands

| Character | State |
|---|---|
| 0 | Sleep |
| 1 | Idle |
| 2 | Thinking |
| 3 | Talking |
| 4 | Happy |
| 5 | Sad |
| 6 | Confused |

## Transport

- USB serial
- Arduino Uno
- Target baud rate: 9600

This protocol will be verified during the firmware rebuild before the AI layer is reconnected.

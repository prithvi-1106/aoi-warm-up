# Session 1 - Hardware Reconstruction

## Objective

Reconstruct the minimum AOI hardware setup and establish a verified Arduino + SSD1306 OLED baseline.

## Before Powering Anything

- [ ] Photograph Arduino Uno
- [ ] Photograph OLED front
- [ ] Photograph OLED rear / pin labels
- [ ] Photograph available wires/connectors
- [ ] Identify OLED model/markings
- [ ] Confirm pin names
- [ ] Confirm expected voltage
- [ ] Identify Arduino board variant

## Target Wiring

| OLED | Arduino Uno |
|---|---|
| GND | GND |
| VCC | Appropriate power pin after voltage check |
| SDA | A4 |
| SCL | A5 |

This is a target, not a final instruction until the component photos are inspected.

## First Test

1. Connect Arduino by USB.
2. Upload a minimal SSD1306 test sketch.
3. Confirm the OLED initializes.
4. Display a simple test message.
5. Photograph the working result.
6. Record the OLED I2C address if discovered.

## Evidence

Add these to media/: session-01-components.jpg, session-01-oled-wiring.jpg, session-01-oled-test.jpg.

## Result

_To be completed after the physical test._

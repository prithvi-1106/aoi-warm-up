#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64
#define OLED_RESET -1
#define OLED_ADDR 0x3C

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

enum FaceState {
  SLEEP = 0,
  IDLE = 1,
  THINKING = 2,
  TALKING = 3,
  HAPPY = 4,
  SAD = 5,
  CONFUSED = 6
};

int faceState = IDLE;

unsigned long lastBlink = 0;
bool blinking = false;

void setup() {
  Serial.begin(9600);

  if (!display.begin(SSD1306_SWITCHCAPVCC, OLED_ADDR)) {
    while (true) {
      delay(1000);
    }
  }

  display.clearDisplay();
  display.display();
}

void loop() {
  readSerial();
  updateBlink();
  drawFace();
  delay(40);
}

void readSerial() {
  while (Serial.available() > 0) {
    char command = Serial.read();

    if (command >= '0' && command <= '6') {
      faceState = command - '0';
    }
  }
}

void updateBlink() {
  if (faceState == SLEEP) {
    blinking = true;
    return;
  }

  unsigned long now = millis();

  if (!blinking && now - lastBlink > 3500) {
    blinking = true;
    lastBlink = now;
  } else if (blinking && now - lastBlink > 140) {
    blinking = false;
    lastBlink = now;
  }
}

void drawFace() {
  display.clearDisplay();

  if (faceState == SLEEP) {
    drawClosedEyes();
  } else if (blinking) {
    drawClosedEyes();
  } else {
    switch (faceState) {
      case THINKING:
        drawThinking();
        break;
      case TALKING:
        drawTalking();
        break;
      case HAPPY:
        drawHappy();
        break;
      case SAD:
        drawSad();
        break;
      case CONFUSED:
        drawConfused();
        break;
      case IDLE:
      default:
        drawIdle();
        break;
    }
  }

  display.display();
}

void drawIdle() {
  drawEye(39, 31, 13, 19);
  drawEye(89, 31, 13, 19);
}

void drawClosedEyes() {
  display.drawLine(27, 32, 51, 32, SSD1306_WHITE);
  display.drawLine(77, 32, 101, 32, SSD1306_WHITE);
}

void drawEye(int x, int y, int w, int h) {
  display.fillRoundRect(x - w, y - h, w * 2, h * 2, 8, SSD1306_WHITE);
  display.fillCircle(x, y + 2, 5, SSD1306_BLACK);
}

void drawThinking() {
  drawEye(37, 34, 11, 15);
  drawEye(91, 28, 11, 15);
  display.drawLine(20, 14, 48, 10, SSD1306_WHITE);
}

void drawTalking() {
  drawEye(39, 30, 12, 17);
  drawEye(89, 30, 12, 17);
  display.fillRoundRect(50, 51, 28, 7, 3, SSD1306_WHITE);
}

void drawHappy() {
  display.drawLine(27, 32, 39, 24, SSD1306_WHITE);
  display.drawLine(39, 24, 51, 32, SSD1306_WHITE);

  display.drawLine(77, 32, 89, 24, SSD1306_WHITE);
  display.drawLine(89, 24, 101, 32, SSD1306_WHITE);

  display.drawLine(48, 49, 54, 54, SSD1306_WHITE);
  display.drawLine(54, 54, 64, 57, SSD1306_WHITE);
  display.drawLine(64, 57, 74, 54, SSD1306_WHITE);
  display.drawLine(74, 54, 80, 49, SSD1306_WHITE);
}

void drawSad() {
  drawEye(39, 33, 11, 15);
  drawEye(89, 33, 11, 15);

  display.drawLine(52, 56, 58, 51, SSD1306_WHITE);
  display.drawLine(58, 51, 64, 49, SSD1306_WHITE);
  display.drawLine(64, 49, 70, 51, SSD1306_WHITE);
  display.drawLine(70, 51, 76, 56, SSD1306_WHITE);
}

void drawConfused() {
  drawEye(37, 31, 11, 16);
  drawEye(91, 31, 11, 16);

  display.drawLine(51, 52, 77, 52, SSD1306_WHITE);
  display.drawLine(77, 52, 82, 47, SSD1306_WHITE);
}

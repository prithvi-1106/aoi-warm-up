import time
import serial

PORT = "COM8"
BAUD = 9600

EMOTION_TO_FACE = {
    "sleep": "0",
    "idle": "1",
    "thinking": "2",
    "talking": "3",
    "happy": "4",
    "sad": "5",
    "confused": "6",
}

def connect():
    return serial.Serial(PORT, BAUD, timeout=1)

def set_emotion(arduino, emotion):
    emotion = emotion.strip().lower()
    if emotion not in EMOTION_TO_FACE:
        raise ValueError(f"Unknown emotion: {emotion}")

    command = EMOTION_TO_FACE[emotion]
    arduino.write(command.encode("ascii"))
    arduino.flush()
    print(f"AOI -> {emotion} [{command}]")

def test_all_emotions(delay=1.5):
    with connect() as arduino:
        for emotion in EMOTION_TO_FACE:
            set_emotion(arduino, emotion)
            time.sleep(delay)

if __name__ == "__main__":
    print(f"Connecting to AOI on {PORT} at {BAUD} baud...")
    test_all_emotions()
    print("Emotion test complete.")

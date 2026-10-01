import time
import tkinter as tk
from tkinter import scrolledtext

import serial

PORT = "COM8"
BAUD = 9600

FACE_TO_EMOTION = {
    "0": "sleep",
    "1": "idle",
    "2": "thinking",
    "3": "talking",
    "4": "happy",
    "5": "sad",
    "6": "confused",
}


def connect():
    """Open the Arduino serial connection."""
    return serial.Serial(PORT, BAUD, timeout=1)


def set_face_state(arduino, state_code):
    """Send one face-state number to the Arduino."""
    state_code = state_code.strip()

    if state_code not in FACE_TO_EMOTION:
        raise ValueError("Enter a number from 0 to 6.")

    arduino.write(state_code.encode("ascii"))
    arduino.flush()

    return FACE_TO_EMOTION[state_code]


class AOIChatBox:
    def __init__(self, root, arduino):
        self.root = root
        self.arduino = arduino

        root.title("AOI Emotion Control")
        root.geometry("430x420")
        root.resizable(False, False)

        title = tk.Label(
            root,
            text="AOI Emotion Control",
            font=("Segoe UI", 14, "bold"),
        )
        title.pack(pady=(12, 6))

        subtitle = tk.Label(
            root,
            text="Enter a number from 0 to 6",
            font=("Segoe UI", 10),
        )
        subtitle.pack(pady=(0, 8))

        self.chat = scrolledtext.ScrolledText(
            root,
            width=46,
            height=16,
            state="disabled",
            wrap=tk.WORD,
            font=("Consolas", 10),
        )
        self.chat.pack(padx=12, pady=4)

        input_frame = tk.Frame(root)
        input_frame.pack(fill="x", padx=12, pady=10)

        self.entry = tk.Entry(
            input_frame,
            font=("Segoe UI", 11),
            justify="center",
        )
        self.entry.pack(side="left", fill="x", expand=True)
        self.entry.bind("<Return>", self.send_message)

        send_button = tk.Button(
            input_frame,
            text="Send",
            width=8,
            command=self.send_message,
        )
        send_button.pack(side="left", padx=(8, 0))

        self.status = tk.Label(
            root,
            text=f"Connected to {PORT}",
            font=("Segoe UI", 9),
        )
        self.status.pack(pady=(0, 8))

        self.write_chat("AOI", "Connected. Type 0-6 and press Enter.")
        self.entry.focus_set()

        root.protocol("WM_DELETE_WINDOW", self.close)

    def write_chat(self, speaker, message):
        self.chat.configure(state="normal")
        self.chat.insert(tk.END, f"{speaker}: {message}\n")
        self.chat.see(tk.END)
        self.chat.configure(state="disabled")

    def send_message(self, event=None):
        state_code = self.entry.get().strip()

        if not state_code:
            return

        self.write_chat("You", state_code)
        self.entry.delete(0, tk.END)

        try:
            emotion = set_face_state(self.arduino, state_code)
            self.write_chat("AOI", f"emotion updated to {emotion}")
            self.status.config(text=f"Current emotion: {emotion}")
        except ValueError as error:
            self.write_chat("AOI", str(error))
        except serial.SerialException as error:
            self.write_chat("AOI", f"Serial error: {error}")
            self.status.config(text="Serial connection error")

    def close(self):
        try:
            if self.arduino and self.arduino.is_open:
                self.arduino.close()
        finally:
            self.root.destroy()


def main():
    arduino = None

    try:
        print(f"Connecting to AOI on {PORT} at {BAUD} baud...")
        arduino = connect()

        # Give the Uno time to reset after the serial port opens.
        time.sleep(2)

        print("AOI connected.")

        root = tk.Tk()
        AOIChatBox(root, arduino)
        root.mainloop()

    except serial.SerialException as error:
        print(f"Could not connect to Arduino on {PORT}.")
        print(error)

    finally:
        if arduino is not None and arduino.is_open:
            arduino.close()


if __name__ == "__main__":
    main()

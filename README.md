# Bionic Arm — Hand Gesture Controlled Robotic Arm

A computer-vision based bionic arm that mimics human finger movements using real-time hand gesture recognition.

The system uses **Python, OpenCV, MediaPipe, Arduino, and servo motors** to detect the user's finger positions through a camera and reproduce the detected movements on a robotic hand.

---

## ✨ Features

- 🖐️ Real-time hand tracking
- 🤖 Five-finger robotic hand control
- 👁️ Hand landmark detection using MediaPipe
- 🎥 Live camera processing using OpenCV
- 🔌 Serial communication between Python and Arduino
- ⚙️ Individual servo control for each finger
- 🔄 Real-time gesture-to-motion conversion

---

## 🧠 How It Works

The system follows this process:

```text
Webcam
   ↓
OpenCV
   ↓
MediaPipe Hand Tracking
   ↓
Finger State Detection
   ↓
5-Bit Finger Pattern
   ↓
Serial Communication
   ↓
Arduino
   ↓
Servo Motors
   ↓
Bionic Arm Movement

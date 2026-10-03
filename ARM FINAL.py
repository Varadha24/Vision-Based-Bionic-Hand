import cv2
import mediapipe as mp
import serial
import time

# Arduino serial connection (update COM port for Windows, e.g., "COM3")
arduino = serial.Serial('COM5', 9600, timeout=1)
time.sleep(2)  # wait for Arduino reset

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

def get_finger_states(hand_landmarks, handedness):
    fingers = []

    # Thumb check depends on hand type (left/right)
    if handedness == "Right":
        # For right hand: thumb open if tip.x < joint.x
        if hand_landmarks.landmark[4].x < hand_landmarks.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
    else:
        # For left hand: thumb open if tip.x > joint.x
        if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
            fingers.append(1)
        else:
            fingers.append(0)

    # Other 4 fingers (same logic for both hands)
    finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky tips
    finger_pips = [6, 10, 14, 18]  # PIP joints
    for tip, pip in zip(finger_tips, finger_pips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[pip].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers  # [thumb, index, middle, ring, pinky]

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms, hand_handedness in zip(results.multi_hand_landmarks,
                                            results.multi_handedness):
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            handedness = hand_handedness.classification[0].label  # "Left" or "Right"
            states = get_finger_states(handLms, handedness)
            state_str = ''.join(map(str, states))

            # Send to Arduino
            arduino.write((state_str + '\n').encode())
            print(f"Hand: {handedness}, Sent: {state_str}")

    cv2.imshow("Hand Tracking", img)
    if cv2.waitKey(1) & 0xFF == 27:  # ESC to quit
        break

cap.release()
cv2.destroyAllWindows()
arduino.close()

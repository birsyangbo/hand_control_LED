import cv2
import mediapipe as mp #haatko laagi
import serial #arduino ko laagi
import time

ser = serial.Serial('/dev/cu.usbmodem11201', 9600) #aafno port rakhne
time.sleep(2) 


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)
mp_draw = mp.solutions.drawing_utils


cap = cv2.VideoCapture(1)#video on gareko


last_sent = -1 #surumaa on nahos vanera


def count_fingers(hand_landmarks):
    fingers = []


    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
        fingers.append(1)
    else:
        fingers.append(0)


    tips = [8, 12, 16, 20]

    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)


while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)  
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    result = hands.process(img_rgb)

    fingers = 0

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            fingers = count_fingers(handLms)

            
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)


    if fingers != last_sent:
        print("Fingers:", fingers)
        ser.write(str(fingers).encode())
        last_sent = fingers

    
    cv2.putText(img, f'Fingers: {fingers}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 0), 3)

    cv2.imshow("Hand Control LED", img)


    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()
ser.close()
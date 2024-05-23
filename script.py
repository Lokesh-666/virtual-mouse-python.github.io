import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture from the webcam
cap = cv2.VideoCapture(0)

# Initialize MediaPipe hands module
hand_detector = mp.solutions.hands.Hands()
drawing_utils = mp.solutions.drawing_utils

# Get screen dimensions
screen_width, screen_height = pyautogui.size()
index_y = 0

# Main loop
while True:
    # Read frame from webcam
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip frame horizontally

    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape

    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process frame with MediaPipe hands
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    if hands:
        for hand in hands:
            # Draw hand landmarks on frame
            drawing_utils.draw_landmarks(frame, hand)
            landmarks = hand.landmark

            for id, landmark in enumerate(landmarks):
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                if id == 8:  # Index finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                if id == 4:  # Thumb tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                    # Check distance between index finger tip and thumb tip
                    if abs(index_y - thumb_y) < 20:
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif abs(index_y - thumb_y) < 100:
                        pyautogui.moveTo(index_x, index_y)

    # Display frame
    cv2.imshow('Virtual Mouse', frame)
    cv2.waitKey(1)
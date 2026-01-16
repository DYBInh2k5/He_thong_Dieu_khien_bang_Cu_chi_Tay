import cv2
import os
# Tắt tensorflow để tránh xung đột
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import mediapipe as mp

class GestureDetector:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
    def count_fingers(self, landmarks):
        """Đếm số ngón tay đang giơ lên"""
        fingers = []
        
        # Ngón cái (so sánh x vì ngón cái nằm ngang)
        if landmarks[4].x < landmarks[3].x:
            fingers.append(1)
        else:
            fingers.append(0)
            
        # 4 ngón còn lại (so sánh y)
        tips = [8, 12, 16, 20]
        for tip in tips:
            if landmarks[tip].y < landmarks[tip - 2].y:
                fingers.append(1)
            else:
                fingers.append(0)
                
        return sum(fingers)
    
    def detect_gesture(self, landmarks):
        """Nhận diện cử chỉ cụ thể"""
        fingers_up = self.count_fingers(landmarks)
        
        # Số từ 0-9
        if fingers_up == 0:
            return "zero"
        elif fingers_up == 1:
            return "one"
        elif fingers_up == 2:
            return "two"
        elif fingers_up == 3:
            return "three"
        elif fingers_up == 4:
            return "four"
        elif fingers_up == 5:
            return "five"
            
        return None
    
    def process_frame(self, frame):
        """Xử lý frame và trả về kết quả"""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        
        gesture = None
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_draw.draw_landmarks(
                    frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                )
                gesture = self.detect_gesture(hand_landmarks.landmark)
                
        return frame, gesture

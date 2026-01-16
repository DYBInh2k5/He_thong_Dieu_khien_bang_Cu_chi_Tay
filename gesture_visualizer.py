import cv2
import numpy as np

class GestureVisualizer:
    """Hiển thị hướng dẫn cử chỉ trên màn hình"""
    
    def __init__(self):
        self.gestures_keyboard = {
            "zero": "0️⃣ Số 0",
            "one": "1️⃣ Số 1",
            "two": "2️⃣ Số 2",
            "three": "3️⃣ Số 3",
            "four": "4️⃣ Số 4",
            "five": "5️⃣ Số 5"
        }
        
        self.gestures_robot = {
            "forward": "⬆️ Tiến",
            "left": "⬅️ Trái",
            "right": "➡️ Phải",
            "backward": "⬇️ Lùi",
            "stop": "🛑 Dừng"
        }
        
        self.gestures_menu = {
            "one": "🖱️ Click",
            "two": "🔍+ Zoom In",
            "three": "🔍- Zoom Out",
            "four": "✋ Drag",
            "five": "❌ Cancel"
        }
    
    def draw_help_panel(self, frame, mode_name):
        """Vẽ bảng hướng dẫn"""
        h, w = frame.shape[:2]
        
        # Tạo panel bên trái
        panel_width = 250
        overlay = frame.copy()
        cv2.rectangle(overlay, (0, 0), (panel_width, h), (0, 0, 0), -1)
        cv2.addWeighted(overlay, 0.7, frame, 0.3, 0, frame)
        
        # Tiêu đề
        cv2.putText(frame, "HUONG DAN", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.line(frame, (10, 40), (panel_width - 10, 40), (255, 255, 255), 1)
        
        # Chọn gestures theo mode
        if mode_name == "Bàn phím":
            gestures = self.gestures_keyboard
        elif mode_name == "Robot":
            gestures = self.gestures_robot
        else:
            gestures = self.gestures_menu
        
        # Hiển thị danh sách
        y = 70
        for gesture, label in gestures.items():
            cv2.putText(frame, label, (15, y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            y += 30
        
        return frame
    
    def draw_gesture_indicator(self, frame, gesture, mode_name):
        """Vẽ chỉ báo cử chỉ hiện tại"""
        if not gesture:
            return frame
        
        h, w = frame.shape[:2]
        
        # Chọn label
        if mode_name == "Bàn phím":
            label = self.gestures_keyboard.get(gesture, gesture)
        elif mode_name == "Robot":
            label = self.gestures_robot.get(gesture, gesture)
        else:
            label = self.gestures_menu.get(gesture, gesture)
        
        # Vẽ box lớn ở giữa màn hình
        text_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 3)[0]
        box_w = text_size[0] + 40
        box_h = text_size[1] + 40
        box_x = (w - box_w) // 2
        box_y = h - 150
        
        # Vẽ background
        overlay = frame.copy()
        cv2.rectangle(overlay, (box_x, box_y), (box_x + box_w, box_y + box_h),
                     (0, 255, 0), -1)
        cv2.addWeighted(overlay, 0.6, frame, 0.4, 0, frame)
        
        # Vẽ text
        text_x = box_x + 20
        text_y = box_y + box_h - 20
        cv2.putText(frame, label, (text_x, text_y),
                   cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
        
        return frame
    
    def draw_stats(self, frame, stats):
        """Vẽ thống kê"""
        h, w = frame.shape[:2]
        y = h - 80
        
        for key, value in stats.items():
            text = f"{key}: {value}"
            cv2.putText(frame, text, (10, y),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            y += 20
        
        return frame

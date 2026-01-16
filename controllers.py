import pyautogui

class KeyboardController:
    """Điều khiển bàn phím bằng cử chỉ"""
    
    def execute(self, gesture):
        gesture_map = {
            "zero": "0", "one": "1", "two": "2", "three": "3", 
            "four": "4", "five": "5", "six": "6", "seven": "7",
            "eight": "8", "nine": "9"
        }
        
        if gesture in gesture_map:
            pyautogui.press(gesture_map[gesture])
            return f"Nhấn phím: {gesture_map[gesture]}"
        return None

class RobotController:
    """Điều khiển robot bằng cử chỉ"""
    
    def __init__(self):
        self.position = [0, 0]  # x, y
        self.direction = 0  # 0=Bắc, 90=Đông, 180=Nam, 270=Tây
        
    def execute(self, gesture):
        commands = {
            "left": "⬅️ Rẽ trái",
            "forward": "⬆️ Tiến",
            "right": "➡️ Rẽ phải",
            "backward": "⬇️ Lùi",
            "stop": "🛑 Dừng"
        }
        
        if gesture in commands:
            # Cập nhật vị trí ảo
            if gesture == "forward":
                self.position[1] += 1
            elif gesture == "backward":
                self.position[1] -= 1
            elif gesture == "left":
                self.position[0] -= 1
            elif gesture == "right":
                self.position[0] += 1
            
            # Ở đây bạn có thể thêm code để gửi lệnh đến robot thật
            # import serial
            # ser = serial.Serial('COM3', 9600)
            # ser.write(gesture.encode())
            
            result = f"{commands[gesture]} | Vị trí: ({self.position[0]}, {self.position[1]})"
            print(result)
            return result
        return None

class MenuController:
    """Điều khiển menu bằng cử chỉ"""
    
    def __init__(self):
        self.drag_mode = False
        
    def execute(self, gesture):
        # Map cử chỉ số sang hành động menu
        gesture_map = {
            "one": "click",
            "two": "zoom_in",
            "three": "zoom_out",
            "four": "drag",
            "five": "cancel"
        }
        
        action = gesture_map.get(gesture, gesture)
        
        actions = {
            "click": ("🖱️ Click", lambda: pyautogui.click()),
            "zoom_in": ("🔍+ Zoom In", lambda: pyautogui.hotkey('ctrl', '+')),
            "zoom_out": ("🔍- Zoom Out", lambda: pyautogui.hotkey('ctrl', '-')),
            "drag": ("✋ Drag Mode", lambda: self.toggle_drag()),
            "cancel": ("❌ Cancel", lambda: pyautogui.press('esc'))
        }
        
        if action in actions:
            label, func = actions[action]
            func()
            print(label)
            return label
        return None
    
    def toggle_drag(self):
        self.drag_mode = not self.drag_mode
        if self.drag_mode:
            print("Chế độ kéo: BẬT")
        else:
            print("Chế độ kéo: TẮT")

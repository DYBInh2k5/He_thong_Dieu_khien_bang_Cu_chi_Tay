"""
Ví dụ tạo controller tùy chỉnh
"""
import cv2
from gesture_detector_simple import GestureDetector

class MusicController:
    """Controller điều khiển nhạc"""
    
    def __init__(self):
        self.volume = 50
        self.is_playing = False
    
    def execute(self, gesture):
        if gesture == "one":
            self.is_playing = not self.is_playing
            status = "Playing" if self.is_playing else "Paused"
            print(f"🎵 {status}")
            return status
        
        elif gesture == "two":
            self.volume = min(100, self.volume + 10)
            print(f"🔊 Volume: {self.volume}%")
            return f"Volume: {self.volume}%"
        
        elif gesture == "three":
            self.volume = max(0, self.volume - 10)
            print(f"🔉 Volume: {self.volume}%")
            return f"Volume: {self.volume}%"
        
        elif gesture == "four":
            print("⏭️ Next track")
            return "Next"
        
        elif gesture == "five":
            print("⏮️ Previous track")
            return "Previous"
        
        return None

def main():
    cap = cv2.VideoCapture(0)
    detector = GestureDetector()
    controller = MusicController()
    
    last_gesture = None
    frame_count = 0
    
    print("🎵 Music Controller")
    print("1 ngón: Play/Pause")
    print("2 ngón: Volume Up")
    print("3 ngón: Volume Down")
    print("4 ngón: Next")
    print("5 ngón: Previous")
    print("\nNhấn 'q' để thoát")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        frame, gesture = detector.process_frame(frame)
        
        # Thực thi mỗi 15 frame
        frame_count += 1
        if gesture and gesture != last_gesture and frame_count % 15 == 0:
            controller.execute(gesture)
            last_gesture = gesture
        
        # Hiển thị thông tin
        cv2.putText(frame, f"Music Controller", (10, 30),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        cv2.putText(frame, f"Volume: {controller.volume}%", (10, 70),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        status = "Playing" if controller.is_playing else "Paused"
        cv2.putText(frame, f"Status: {status}", (10, 110),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        
        cv2.imshow("Music Controller", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

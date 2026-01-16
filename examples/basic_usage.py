"""
Ví dụ sử dụng cơ bản - Nhận diện cử chỉ đơn giản
"""
import cv2
from gesture_detector_simple import GestureDetector

def main():
    # Khởi tạo camera và detector
    cap = cv2.VideoCapture(0)
    detector = GestureDetector()
    
    print("Nhấn 'q' để thoát")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Lật frame để dễ nhìn
        frame = cv2.flip(frame, 1)
        
        # Nhận diện cử chỉ
        frame, gesture = detector.process_frame(frame)
        
        # In ra console khi phát hiện cử chỉ
        if gesture:
            print(f"Phát hiện: {gesture}")
        
        # Hiển thị
        cv2.imshow("Basic Gesture Detection", frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

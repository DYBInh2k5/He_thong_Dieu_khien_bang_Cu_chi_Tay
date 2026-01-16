import cv2
import time
from gesture_detector_simple import GestureDetector
from controllers import KeyboardController, RobotController, MenuController
from gesture_visualizer import GestureVisualizer

def main():
    # Hiển thị hướng dẫn
    from demo_mode import show_demo
    show_demo()
    
    # Chọn chế độ điều khiển
    print("=" * 50)
    print("HỆ THỐNG ĐIỀU KHIỂN BẰNG CỬ CHỈ TAY")
    print("=" * 50)
    print("Chọn chế độ:")
    print("1. Điều khiển bàn phím")
    print("2. Điều khiển robot")
    print("3. Điều khiển menu")
    print("=" * 50)
    
    mode = input("Nhập số (1-3): ").strip()
    
    if mode == "1":
        controller = KeyboardController()
        mode_name = "Bàn phím"
    elif mode == "2":
        controller = RobotController()
        mode_name = "Robot"
    elif mode == "3":
        controller = MenuController()
        mode_name = "Menu"
    else:
        print("Chế độ không hợp lệ!")
        return
    
    print(f"\nĐang khởi động chế độ: {mode_name}")
    print("Đang mở camera...")
    
    # Khởi tạo camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("LỖI: Không thể mở camera!")
        print("Vui lòng kiểm tra:")
        print("- Camera có được kết nối không?")
        print("- Ứng dụng khác có đang sử dụng camera không?")
        return
    
    print("Camera đã sẵn sàng!")
    print("Nhấn 'q' trong cửa sổ camera để thoát\n")
    
    detector = GestureDetector()
    visualizer = GestureVisualizer()
    
    last_gesture = None
    frame_count = 0
    gesture_count = 0
    start_time = time.time()
    fps = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc frame từ camera")
            break
            
        frame = cv2.flip(frame, 1)
        frame, gesture = detector.process_frame(frame)
        
        # Tính FPS
        frame_count += 1
        if frame_count % 30 == 0:
            elapsed = time.time() - start_time
            fps = 30 / elapsed if elapsed > 0 else 0
            start_time = time.time()
        
        # Thực thi lệnh khi phát hiện cử chỉ mới (mỗi 15 frame)
        if gesture and gesture != last_gesture and frame_count % 15 == 0:
            result = controller.execute(gesture)
            if result:
                gesture_count += 1
            last_gesture = gesture
        
        # Vẽ bảng hướng dẫn
        frame = visualizer.draw_help_panel(frame, mode_name)
        
        # Vẽ chỉ báo cử chỉ
        frame = visualizer.draw_gesture_indicator(frame, gesture, mode_name)
        
        # Hiển thị thông tin trên cùng
        cv2.putText(frame, f"Mode: {mode_name} | FPS: {fps:.1f}", 
                    (frame.shape[1] - 350, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        cv2.putText(frame, f"Gestures: {gesture_count}", 
                    (frame.shape[1] - 350, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 255), 2)
        
        cv2.putText(frame, "Nhan 'q' hoac ESC de thoat", 
                    (frame.shape[1] - 350, frame.shape[0] - 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)
        
        cv2.imshow("Hand Gesture Control", frame)
        
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:  # q hoặc ESC
            break
    
    print("\nĐang đóng chương trình...")
    cap.release()
    cv2.destroyAllWindows()
    print("Đã thoát!")

if __name__ == "__main__":
    main()

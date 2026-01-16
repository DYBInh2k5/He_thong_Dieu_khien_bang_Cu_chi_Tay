"""
Chế độ demo - hiển thị tất cả các cử chỉ có thể
"""
import cv2
import numpy as np

def create_gesture_guide():
    """Tạo hình ảnh hướng dẫn cử chỉ"""
    guide = np.zeros((800, 1200, 3), dtype=np.uint8)
    
    # Tiêu đề
    cv2.putText(guide, "HUONG DAN CU CHI TAY", (350, 50),
               cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)
    
    # Bàn phím
    cv2.putText(guide, "1. DIEU KHIEN BAN PHIM", (50, 120),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    y = 160
    keyboard_gestures = [
        "0 ngon (nam tay) -> So 0",
        "1 ngon -> So 1",
        "2 ngon -> So 2",
        "3 ngon -> So 3",
        "4 ngon -> So 4",
        "5 ngon -> So 5"
    ]
    for text in keyboard_gestures:
        cv2.putText(guide, text, (70, y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        y += 35
    
    # Robot
    cv2.putText(guide, "2. DIEU KHIEN ROBOT", (50, 400),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    y = 440
    robot_gestures = [
        "1 ngon -> Tien",
        "2 ngon -> Re trai",
        "3 ngon -> Re phai",
        "4 ngon -> Lui",
        "Nam tay -> Dung"
    ]
    for text in robot_gestures:
        cv2.putText(guide, text, (70, y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        y += 35
    
    # Menu
    cv2.putText(guide, "3. DIEU KHIEN MENU", (600, 120),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    y = 160
    menu_gestures = [
        "1 ngon -> Click chuot",
        "2 ngon -> Zoom In",
        "3 ngon -> Zoom Out",
        "4 ngon -> Che do keo",
        "5 ngon -> Huy"
    ]
    for text in menu_gestures:
        cv2.putText(guide, text, (620, y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        y += 35
    
    # Lưu ý
    cv2.putText(guide, "LUU Y:", (600, 400),
               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    notes = [
        "- Dat tay vao khung mau xanh",
        "- Gio ngon tay ro rang",
        "- Tranh anh sang manh phia sau",
        "- Nen phong co mau sac khac voi mau da"
    ]
    y = 440
    for text in notes:
        cv2.putText(guide, text, (620, y),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        y += 35
    
    # Footer
    cv2.putText(guide, "Nhan phim bat ky de tiep tuc...", (400, 750),
               cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
    
    return guide

def show_demo():
    """Hiển thị demo"""
    guide = create_gesture_guide()
    cv2.imshow("Huong Dan Cu Chi", guide)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    show_demo()

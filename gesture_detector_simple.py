import cv2
import numpy as np

class GestureDetector:
    """Phiên bản đơn giản sử dụng phát hiện màu da"""
    def __init__(self):
        self.gesture_count = 0
        self.last_gesture = None
        
    def detect_skin(self, frame):
        """Phát hiện vùng da trong ảnh"""
        # Chuyển sang HSV
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        # Ngưỡng màu da
        lower_skin = np.array([0, 20, 70], dtype=np.uint8)
        upper_skin = np.array([20, 255, 255], dtype=np.uint8)
        
        # Tạo mask
        mask = cv2.inRange(hsv, lower_skin, upper_skin)
        
        # Làm mịn
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        
        return mask
    
    def count_fingers_simple(self, contour):
        """Đếm ngón tay đơn giản dựa trên convex hull"""
        hull = cv2.convexHull(contour, returnPoints=False)
        
        if len(hull) > 3:
            defects = cv2.convexityDefects(contour, hull)
            if defects is not None:
                finger_count = 0
                for i in range(defects.shape[0]):
                    s, e, f, d = defects[i, 0]
                    start = tuple(contour[s][0])
                    end = tuple(contour[e][0])
                    far = tuple(contour[f][0])
                    
                    # Tính góc
                    a = np.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                    b = np.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                    c = np.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                    angle = np.arccos((b**2 + c**2 - a**2) / (2 * b * c))
                    
                    if angle <= np.pi / 2:
                        finger_count += 1
                
                return finger_count + 1
        return 0
    
    def detect_gesture(self, finger_count, contour):
        """Chuyển số ngón tay và hình dạng bàn tay thành cử chỉ"""
        # Tính toán hướng của bàn tay
        moments = cv2.moments(contour)
        if moments['m00'] != 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])
            
            # Phát hiện cử chỉ đặc biệt
            hull = cv2.convexHull(contour)
            hull_area = cv2.contourArea(hull)
            contour_area = cv2.contourArea(contour)
            
            if hull_area > 0:
                solidity = contour_area / hull_area
                
                # Nắm tay chặt (stop)
                if finger_count == 0 and solidity > 0.9:
                    return "stop"
                
                # Cử chỉ điều hướng
                if finger_count == 1:
                    return "forward"  # 1 ngón = tiến
                elif finger_count == 2:
                    return "left"  # 2 ngón = trái
                elif finger_count == 3:
                    return "right"  # 3 ngón = phải
                elif finger_count == 4:
                    return "backward"  # 4 ngón = lùi
        
        # Số từ 0-5
        gestures = {
            0: "zero",
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five"
        }
        return gestures.get(finger_count, None)
    
    def process_frame(self, frame):
        """Xử lý frame"""
        # Lấy vùng quan tâm (ROI) - góc trên bên phải
        roi = frame[50:300, 300:600]
        
        # Phát hiện da
        mask = self.detect_skin(roi)
        
        # Tìm contours
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        gesture = None
        if contours:
            # Lấy contour lớn nhất
            max_contour = max(contours, key=cv2.contourArea)
            
            if cv2.contourArea(max_contour) > 5000:
                # Vẽ contour
                cv2.drawContours(roi, [max_contour], -1, (0, 255, 0), 2)
                
                # Vẽ convex hull
                hull = cv2.convexHull(max_contour)
                cv2.drawContours(roi, [hull], -1, (255, 0, 0), 2)
                
                # Đếm ngón tay
                finger_count = self.count_fingers_simple(max_contour)
                gesture = self.detect_gesture(finger_count, max_contour)
                
                # Hiển thị số ngón
                cv2.putText(roi, f"Fingers: {finger_count}", (10, 30),
                           cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
        
        # Vẽ khung ROI
        cv2.rectangle(frame, (300, 50), (600, 300), (255, 0, 0), 2)
        cv2.putText(frame, "Dat tay vao khung nay", (310, 40),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
        
        return frame, gesture

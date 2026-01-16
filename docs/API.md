# 📚 API Documentation

## GestureDetector

Class chính để nhận diện cử chỉ tay.

### Constructor
```python
detector = GestureDetector()
```

### Methods

#### `process_frame(frame)`
Xử lý frame từ camera và trả về frame đã được vẽ cùng cử chỉ nhận diện.

**Parameters:**
- `frame` (numpy.ndarray): Frame từ camera

**Returns:**
- `tuple`: (frame_processed, gesture_name)
  - `frame_processed`: Frame đã vẽ contours và thông tin
  - `gesture_name`: Tên cử chỉ ("zero", "one", "two", ...) hoặc None

**Example:**
```python
cap = cv2.VideoCapture(0)
detector = GestureDetector()

ret, frame = cap.read()
frame, gesture = detector.process_frame(frame)
print(f"Detected: {gesture}")
```

#### `detect_skin(frame)`
Phát hiện vùng da trong frame.

**Parameters:**
- `frame` (numpy.ndarray): Frame đầu vào

**Returns:**
- `numpy.ndarray`: Binary mask của vùng da

#### `count_fingers_simple(contour)`
Đếm số ngón tay dựa trên convex hull.

**Parameters:**
- `contour` (numpy.ndarray): Contour của bàn tay

**Returns:**
- `int`: Số ngón tay (0-5)

#### `detect_gesture(finger_count, contour)`
Chuyển đổi số ngón tay thành tên cử chỉ.

**Parameters:**
- `finger_count` (int): Số ngón tay
- `contour` (numpy.ndarray): Contour của bàn tay

**Returns:**
- `str`: Tên cử chỉ

---

## Controllers

### KeyboardController

Điều khiển bàn phím bằng cử chỉ.

```python
controller = KeyboardController()
controller.execute("one")  # Nhấn phím "1"
```

#### `execute(gesture)`
**Parameters:**
- `gesture` (str): Tên cử chỉ

**Returns:**
- `str`: Thông báo kết quả hoặc None

---

### RobotController

Điều khiển robot bằng cử chỉ.

```python
controller = RobotController()
controller.execute("forward")  # Robot tiến
```

**Attributes:**
- `position` (list): Vị trí hiện tại [x, y]
- `direction` (int): Hướng hiện tại (0-360)

#### `execute(gesture)`
**Parameters:**
- `gesture` (str): Tên cử chỉ ("forward", "left", "right", "backward", "stop")

**Returns:**
- `str`: Thông báo kết quả

---

### MenuController

Điều khiển menu/giao diện bằng cử chỉ.

```python
controller = MenuController()
controller.execute("one")  # Click chuột
```

**Attributes:**
- `drag_mode` (bool): Trạng thái chế độ kéo

#### `execute(gesture)`
**Parameters:**
- `gesture` (str): Tên cử chỉ

**Returns:**
- `str`: Thông báo kết quả

---

## GestureVisualizer

Class để vẽ giao diện trực quan.

### Constructor
```python
visualizer = GestureVisualizer()
```

### Methods

#### `draw_help_panel(frame, mode_name)`
Vẽ bảng hướng dẫn bên trái màn hình.

**Parameters:**
- `frame` (numpy.ndarray): Frame cần vẽ
- `mode_name` (str): Tên chế độ ("Bàn phím", "Robot", "Menu")

**Returns:**
- `numpy.ndarray`: Frame đã vẽ

#### `draw_gesture_indicator(frame, gesture, mode_name)`
Vẽ chỉ báo cử chỉ hiện tại.

**Parameters:**
- `frame` (numpy.ndarray): Frame cần vẽ
- `gesture` (str): Tên cử chỉ
- `mode_name` (str): Tên chế độ

**Returns:**
- `numpy.ndarray`: Frame đã vẽ

---

## Demo Mode

### `show_demo()`
Hiển thị màn hình hướng dẫn.

```python
from demo_mode import show_demo
show_demo()
```

---

## Gesture Names

### Keyboard Mode
- `"zero"` - 0 ngón
- `"one"` - 1 ngón
- `"two"` - 2 ngón
- `"three"` - 3 ngón
- `"four"` - 4 ngón
- `"five"` - 5 ngón

### Robot Mode
- `"forward"` - Tiến
- `"left"` - Trái
- `"right"` - Phải
- `"backward"` - Lùi
- `"stop"` - Dừng

### Menu Mode
- `"one"` - Click
- `"two"` - Zoom In
- `"three"` - Zoom Out
- `"four"` - Drag
- `"five"` - Cancel

---

## Example Usage

### Tích hợp vào Project khác

```python
import cv2
from gesture_detector_simple import GestureDetector

# Khởi tạo
cap = cv2.VideoCapture(0)
detector = GestureDetector()

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    
    # Nhận diện cử chỉ
    frame, gesture = detector.process_frame(frame)
    
    # Xử lý cử chỉ
    if gesture == "one":
        print("Phát hiện 1 ngón!")
        # Thực hiện hành động của bạn
    
    cv2.imshow("My App", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

### Custom Controller

```python
from controllers import KeyboardController

class MyCustomController(KeyboardController):
    def execute(self, gesture):
        if gesture == "one":
            # Custom action
            print("Custom action for gesture one")
            return "Custom result"
        return super().execute(gesture)
```

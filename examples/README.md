# 📚 Examples

Thư mục này chứa các ví dụ sử dụng hệ thống.

## Danh sách Examples

### 1. basic_usage.py
Ví dụ cơ bản nhất - chỉ nhận diện và in ra cử chỉ.

```bash
python examples/basic_usage.py
```

### 2. custom_controller.py
Ví dụ tạo controller tùy chỉnh - Music Controller.

```bash
python examples/custom_controller.py
```

**Tính năng:**
- 1 ngón: Play/Pause
- 2 ngón: Tăng âm lượng
- 3 ngón: Giảm âm lượng
- 4 ngón: Bài tiếp theo
- 5 ngón: Bài trước

## Tạo Controller của riêng bạn

```python
class MyController:
    def execute(self, gesture):
        if gesture == "one":
            # Hành động của bạn
            print("Làm gì đó")
            return "Kết quả"
        return None
```

## Tích hợp vào Project

```python
from gesture_detector_simple import GestureDetector

detector = GestureDetector()
frame, gesture = detector.process_frame(frame)

if gesture:
    # Xử lý cử chỉ
    pass
```

# 🖐️ Hệ thống Điều khiển bằng Cử chỉ Tay

Dự án nhận diện cử chỉ tay để điều khiển bàn phím, robot và menu sử dụng Computer Vision.

## ✨ Tính năng

### 1. Điều khiển Bàn phím
- Nhập số 0-9 bằng cử chỉ tay
- Tự động nhận diện số ngón tay

### 2. Điều khiển Robot
- Điều hướng robot: tiến, lùi, trái, phải
- Dừng robot bằng cử chỉ nắm tay
- Theo dõi vị trí robot ảo

### 3. Điều khiển Menu
- Click chuột
- Zoom in/out
- Chế độ kéo (drag)
- Hủy thao tác

## 🚀 Cài đặt

```bash
pip install -r requirements.txt
```

## 📖 Sử dụng

```bash
python main.py
```

Chương trình sẽ hiển thị hướng dẫn, sau đó chọn chế độ:
1. **Bàn phím** - Điều khiển số 0-9
2. **Robot** - Điều khiển di chuyển
3. **Menu** - Điều khiển giao diện

## 🖐️ Bảng Cử chỉ

### Chế độ Bàn phím
| Cử chỉ | Hành động |
|--------|-----------|
| 0 ngón (nắm tay) | Số 0 |
| 1 ngón | Số 1 |
| 2 ngón | Số 2 |
| 3 ngón | Số 3 |
| 4 ngón | Số 4 |
| 5 ngón | Số 5 |

### Chế độ Robot
| Cử chỉ | Hành động |
|--------|-----------|
| 1 ngón | ⬆️ Tiến |
| 2 ngón | ⬅️ Rẽ trái |
| 3 ngón | ➡️ Rẽ phải |
| 4 ngón | ⬇️ Lùi |
| Nắm tay | 🛑 Dừng |

### Chế độ Menu
| Cử chỉ | Hành động |
|--------|-----------|
| 1 ngón | 🖱️ Click |
| 2 ngón | 🔍+ Zoom In |
| 3 ngón | 🔍- Zoom Out |
| 4 ngón | ✋ Drag |
| 5 ngón | ❌ Cancel |

## 💡 Lưu ý

- Đặt tay vào khung màu xanh trên màn hình
- Giơ ngón tay rõ ràng
- Tránh ánh sáng mạnh phía sau
- Nền phòng nên có màu sắc khác với màu da

## 🎮 Phím tắt

- **Q** hoặc **ESC**: Thoát chương trình
- Chương trình hiển thị FPS và số lượng cử chỉ đã thực hiện

## 📁 Cấu trúc Dự án

```
├── main.py                      # Chương trình chính
├── gesture_detector_simple.py   # Module nhận diện cử chỉ
├── controllers.py               # Các controller
├── gesture_visualizer.py        # Hiển thị giao diện
├── demo_mode.py                 # Chế độ demo
└── requirements.txt             # Dependencies
```

## 🔧 Mở rộng

### Kết nối Robot thật
Sửa file `controllers.py`, thêm code gửi lệnh qua Serial:

```python
import serial
ser = serial.Serial('COM3', 9600)
ser.write(gesture.encode())
```

### Thêm cử chỉ mới
Sửa file `gesture_detector_simple.py`, thêm logic nhận diện trong hàm `detect_gesture()`

## 📝 License

MIT License - Tự do sử dụng và phát triển

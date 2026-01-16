# 🖐️ Hệ thống Điều khiển bằng Cử chỉ Tay

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay.svg)](https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay.svg)](https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay/issues)

Dự án nhận diện cử chỉ tay để điều khiển bàn phím, robot và menu sử dụng Computer Vision.

<div align="center">
  <img src="image.png" alt="Hand Gesture Control Demo" width="800"/>
  <p><i>Hệ thống nhận diện cử chỉ tay với 3 chế độ điều khiển</i></p>
</div>

## 🎬 Demo & Screenshots

<table>
  <tr>
    <td align="center">
      <img src="docs/images/keyboard_mode.png" alt="Keyboard Mode" width="300"/><br>
      <b>Chế độ Bàn phím</b><br>
      Điều khiển số 0-9
    </td>
    <td align="center">
      <img src="docs/images/robot_mode.png" alt="Robot Mode" width="300"/><br>
      <b>Chế độ Robot</b><br>
      Điều hướng robot
    </td>
    <td align="center">
      <img src="docs/images/menu_mode.png" alt="Menu Mode" width="300"/><br>
      <b>Chế độ Menu</b><br>
      Điều khiển giao diện
    </td>
  </tr>
</table>

### 📹 Video Demo
> 🎥 [Xem video demo đầy đủ tại đây](https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay/releases) _(Sẽ cập nhật sau)_

![alt text](image.png)

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

## 🚀 Quick Start

```bash
# Clone repository
git clone https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay.git
cd He_thong_Dieu_khien_bang_Cu_chi_Tay

# Cài đặt dependencies
pip install -r requirements.txt

# Chạy chương trình
python main.py
```

📖 **[Xem hướng dẫn chi tiết](QUICKSTART.md)**

Chương trình sẽ hiển thị hướng dẫn, sau đó chọn chế độ:
1. **Bàn phím** - Điều khiển số 0-9
2. **Robot** - Điều khiển di chuyển
3. **Menu** - Điều khiển giao diện

## 🖐️ Bảng Cử chỉ

<details open>
<summary><b>📋 Xem tất cả cử chỉ</b></summary>

### 1️⃣ Chế độ Bàn phím
<table>
  <tr>
    <th>Cử chỉ</th>
    <th>Hình ảnh</th>
    <th>Hành động</th>
  </tr>
  <tr>
    <td>0 ngón (nắm tay)</td>
    <td>✊</td>
    <td>Số 0</td>
  </tr>
  <tr>
    <td>1 ngón</td>
    <td>☝️</td>
    <td>Số 1</td>
  </tr>
  <tr>
    <td>2 ngón</td>
    <td>✌️</td>
    <td>Số 2</td>
  </tr>
  <tr>
    <td>3 ngón</td>
    <td>🤟</td>
    <td>Số 3</td>
  </tr>
  <tr>
    <td>4 ngón</td>
    <td>🖖</td>
    <td>Số 4</td>
  </tr>
  <tr>
    <td>5 ngón</td>
    <td>🖐️</td>
    <td>Số 5</td>
  </tr>
</table>

### 2️⃣ Chế độ Robot
<table>
  <tr>
    <th>Cử chỉ</th>
    <th>Icon</th>
    <th>Hành động</th>
  </tr>
  <tr>
    <td>1 ngón</td>
    <td>☝️</td>
    <td>⬆️ Tiến</td>
  </tr>
  <tr>
    <td>2 ngón</td>
    <td>✌️</td>
    <td>⬅️ Rẽ trái</td>
  </tr>
  <tr>
    <td>3 ngón</td>
    <td>🤟</td>
    <td>➡️ Rẽ phải</td>
  </tr>
  <tr>
    <td>4 ngón</td>
    <td>🖖</td>
    <td>⬇️ Lùi</td>
  </tr>
  <tr>
    <td>Nắm tay</td>
    <td>✊</td>
    <td>🛑 Dừng</td>
  </tr>
</table>

### 3️⃣ Chế độ Menu
<table>
  <tr>
    <th>Cử chỉ</th>
    <th>Icon</th>
    <th>Hành động</th>
  </tr>
  <tr>
    <td>1 ngón</td>
    <td>☝️</td>
    <td>🖱️ Click</td>
  </tr>
  <tr>
    <td>2 ngón</td>
    <td>✌️</td>
    <td>🔍+ Zoom In</td>
  </tr>
  <tr>
    <td>3 ngón</td>
    <td>🤟</td>
    <td>🔍- Zoom Out</td>
  </tr>
  <tr>
    <td>4 ngón</td>
    <td>🖖</td>
    <td>✋ Drag</td>
  </tr>
  <tr>
    <td>5 ngón</td>
    <td>🖐️</td>
    <td>❌ Cancel</td>
  </tr>
</table>

</details>

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
He_thong_Dieu_khien_bang_Cu_chi_Tay/
├── 📄 main.py                      # Chương trình chính
├── 🤖 gesture_detector_simple.py   # Module nhận diện cử chỉ
├── 🎮 controllers.py               # Các controller
├── 🎨 gesture_visualizer.py        # Hiển thị giao diện
├── 🎬 demo_mode.py                 # Chế độ demo
├── 📦 requirements.txt             # Dependencies
├── 📚 docs/                        # Tài liệu
│   ├── API.md                      # API Documentation
│   ├── INSTALLATION.md             # Hướng dẫn cài đặt
│   └── images/                     # Ảnh minh họa
├── 💡 examples/                    # Ví dụ sử dụng
│   ├── basic_usage.py
│   └── custom_controller.py
└── 📖 README.md                    # Tài liệu chính
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

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Xem [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm chi tiết.

## 📧 Liên hệ

- **Author**: Dinh Yen Binh
- **Email**: binh.vd01500@sinhvien.hoasen.edu.vn
- **GitHub**: [@DYBInh2k5](https://github.com/DYBInh2k5)

## ⭐ Support

Nếu dự án hữu ích, hãy cho một ⭐ trên GitHub!

## 📝 License

MIT License - Tự do sử dụng và phát triển. Xem [LICENSE](LICENSE) để biết thêm chi tiết.

---

Made with ❤️ by [Dinh Yen Binh](https://github.com/DYBInh2k5)

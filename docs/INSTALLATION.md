# 📦 Hướng dẫn Cài đặt Chi tiết

## Yêu cầu Hệ thống

- **Python**: 3.7 trở lên
- **Webcam**: Camera tích hợp hoặc USB
- **RAM**: Tối thiểu 4GB
- **OS**: Windows, macOS, hoặc Linux

## Cài đặt Python

### Windows
1. Tải Python từ [python.org](https://www.python.org/downloads/)
2. Chạy installer, **tick "Add Python to PATH"**
3. Kiểm tra: `python --version`

### macOS
```bash
brew install python3
```

### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install python3 python3-pip
```

## Cài đặt Dự án

### Bước 1: Clone Repository
```bash
git clone https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay.git
cd He_thong_Dieu_khien_bang_Cu_chi_Tay
```

### Bước 2: Tạo Virtual Environment (Khuyến nghị)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Bước 3: Cài đặt Dependencies
```bash
pip install -r requirements.txt
```

### Bước 4: Kiểm tra Camera
```bash
python -c "import cv2; print('Camera OK' if cv2.VideoCapture(0).isOpened() else 'Camera Error')"
```

## Chạy Chương trình

```bash
python main.py
```

## Xử lý Lỗi Thường gặp

### Lỗi: "No module named cv2"
```bash
pip install opencv-python==4.8.1.78
```

### Lỗi: "Camera không mở được"
- Kiểm tra camera có hoạt động không
- Đóng các ứng dụng khác đang dùng camera
- Thử đổi camera index trong code: `cv2.VideoCapture(1)`

### Lỗi: "numpy version incompatible"
```bash
pip uninstall numpy
pip install numpy==1.26.4
```

### Lỗi: Permission denied (Linux)
```bash
sudo usermod -a -G video $USER
# Logout và login lại
```

## Cấu hình Nâng cao

### Thay đổi Camera
Sửa file `main.py`, dòng:
```python
cap = cv2.VideoCapture(0)  # Đổi 0 thành 1, 2, ...
```

### Điều chỉnh Độ nhạy
Sửa file `gesture_detector_simple.py`:
```python
# Ngưỡng diện tích tối thiểu
if cv2.contourArea(max_contour) > 5000:  # Tăng/giảm giá trị này
```

### Thay đổi Màu da
Sửa file `gesture_detector_simple.py`:
```python
lower_skin = np.array([0, 20, 70], dtype=np.uint8)
upper_skin = np.array([20, 255, 255], dtype=np.uint8)
```

## Kiểm tra Cài đặt

Chạy script test:
```bash
python -c "
import cv2
import numpy as np
import pyautogui
print('✓ Tất cả modules đã được cài đặt!')
"
```

## Gỡ cài đặt

```bash
# Deactivate virtual environment
deactivate

# Xóa thư mục dự án
cd ..
rm -rf He_thong_Dieu_khien_bang_Cu_chi_Tay
```

## Hỗ trợ

Nếu gặp vấn đề, vui lòng:
1. Kiểm tra [Issues](https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay/issues)
2. Tạo issue mới với thông tin chi tiết
3. Email: binh.vd01500@sinhvien.hoasen.edu.vn

# 🤝 Đóng góp cho Dự án

Cảm ơn bạn đã quan tâm đến việc đóng góp cho dự án Hệ thống Điều khiển bằng Cử chỉ Tay!

## 📋 Quy trình Đóng góp

1. **Fork repository**
   - Click nút "Fork" ở góc trên bên phải

2. **Clone repository của bạn**
   ```bash
   git clone https://github.com/YOUR_USERNAME/He_thong_Dieu_khien_bang_Cu_chi_Tay.git
   cd He_thong_Dieu_khien_bang_Cu_chi_Tay
   ```

3. **Tạo branch mới**
   ```bash
   git checkout -b feature/ten-tinh-nang-moi
   ```

4. **Thực hiện thay đổi**
   - Viết code
   - Test kỹ lưỡng
   - Commit với message rõ ràng

5. **Push lên GitHub**
   ```bash
   git push origin feature/ten-tinh-nang-moi
   ```

6. **Tạo Pull Request**
   - Mô tả chi tiết những gì bạn đã thay đổi
   - Đính kèm screenshots nếu có

## 💡 Ý tưởng Đóng góp

### Tính năng mới
- Thêm cử chỉ nhận diện mới
- Hỗ trợ nhận diện 2 tay
- Tích hợp machine learning
- Hỗ trợ điều khiển game
- Ghi lại và phát lại cử chỉ

### Cải thiện
- Tối ưu hiệu suất
- Cải thiện độ chính xác
- Thêm ngôn ngữ mới
- Viết test cases
- Cải thiện documentation

### Bug fixes
- Báo cáo bug qua Issues
- Sửa bug và tạo PR

## 📝 Coding Standards

### Python Style
- Tuân theo PEP 8
- Sử dụng type hints khi có thể
- Viết docstrings cho functions/classes
- Giữ functions ngắn gọn và rõ ràng

### Commit Messages
```
feat: Thêm tính năng nhận diện cử chỉ mới
fix: Sửa lỗi camera không mở
docs: Cập nhật README
refactor: Tối ưu code gesture detector
test: Thêm unit tests
```

### Code Example
```python
def detect_gesture(self, finger_count: int) -> str:
    """
    Nhận diện cử chỉ dựa trên số ngón tay
    
    Args:
        finger_count: Số ngón tay đang giơ lên (0-5)
        
    Returns:
        Tên cử chỉ được nhận diện
    """
    gestures = {
        0: "zero",
        1: "one",
        # ...
    }
    return gestures.get(finger_count, None)
```

## 🧪 Testing

Trước khi submit PR, hãy test:
- Chạy chương trình với cả 3 chế độ
- Test với điều kiện ánh sáng khác nhau
- Test với nhiều màu da khác nhau
- Kiểm tra không có lỗi syntax

## 📧 Liên hệ

- Email: binh.vd01500@sinhvien.hoasen.edu.vn
- GitHub Issues: [Tạo issue mới](https://github.com/DYBInh2k5/He_thong_Dieu_khien_bang_Cu_chi_Tay/issues)

## 🙏 Cảm ơn

Mọi đóng góp, dù lớn hay nhỏ, đều được trân trọng!

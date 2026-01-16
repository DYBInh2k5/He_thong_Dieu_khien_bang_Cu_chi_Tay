# 📸 Hướng dẫn Chụp Screenshots

Hướng dẫn chi tiết để chụp screenshots cho dự án.

## 🎯 Mục tiêu

Tạo các ảnh chất lượng cao để minh họa cho README và documentation.

## 📋 Danh sách Screenshots cần chụp

### 1. Screenshots chính (3 ảnh)
- [ ] `docs/images/keyboard_mode.png` - Chế độ bàn phím
- [ ] `docs/images/robot_mode.png` - Chế độ robot  
- [ ] `docs/images/menu_mode.png` - Chế độ menu

### 2. Demo screen
- [ ] `docs/images/demo_screen.png` - Màn hình hướng dẫn

### 3. Ảnh cử chỉ (6 ảnh)
- [ ] `docs/images/gesture_0.png` - Nắm tay
- [ ] `docs/images/gesture_1.png` - 1 ngón
- [ ] `docs/images/gesture_2.png` - 2 ngón
- [ ] `docs/images/gesture_3.png` - 3 ngón
- [ ] `docs/images/gesture_4.png` - 4 ngón
- [ ] `docs/images/gesture_5.png` - 5 ngón

## 🎬 Cách chụp

### Bước 1: Chuẩn bị
```bash
# Chạy chương trình
python main.py
```

### Bước 2: Chụp từng chế độ

#### Chế độ Bàn phím
1. Chọn chế độ `1`
2. Đặt tay vào khung màu xanh
3. Giơ 3 ngón tay (để demo)
4. Chụp màn hình:
   - **Windows**: `Win + Shift + S`
   - **Mac**: `Cmd + Shift + 4`
   - **Linux**: `Shift + PrtScn`
5. Lưu vào `docs/images/keyboard_mode.png`

#### Chế độ Robot
1. Chọn chế độ `2`
2. Giơ 1 ngón (tiến)
3. Chụp và lưu vào `docs/images/robot_mode.png`

#### Chế độ Menu
1. Chọn chế độ `3`
2. Giơ 2 ngón (zoom in)
3. Chụp và lưu vào `docs/images/menu_mode.png`

### Bước 3: Chụp Demo Screen
1. Khi chương trình hiển thị màn hình hướng dẫn
2. Chụp toàn bộ màn hình
3. Lưu vào `docs/images/demo_screen.png`

### Bước 4: Chụp từng cử chỉ
Chạy chương trình và chụp từng cử chỉ riêng lẻ:
- 0 ngón: Nắm tay chặt
- 1 ngón: Chỉ ngón trỏ
- 2 ngón: Ngón trỏ + ngón giữa
- 3 ngón: Ngón trỏ + giữa + áp út
- 4 ngón: Tất cả trừ ngón cái
- 5 ngón: Tất cả ngón tay

## ✨ Tips để có ảnh đẹp

### Ánh sáng
- ✅ Ánh sáng đủ, đều
- ✅ Ánh sáng từ phía trước hoặc bên
- ❌ Tránh ánh sáng mạnh phía sau
- ❌ Tránh bóng đổ lên tay

### Nền
- ✅ Nền đơn giản, không rối
- ✅ Màu nền khác với màu da
- ✅ Tường trắng hoặc màu nhạt
- ❌ Tránh nền có nhiều vật dụng

### Tay
- ✅ Tay sạch, móng tay gọn gàng
- ✅ Giơ ngón rõ ràng, tự nhiên
- ✅ Đặt tay ở giữa khung
- ❌ Tránh mờ do chuyển động

### Màn hình
- ✅ Độ phân giải cao (1920x1080 trở lên)
- ✅ Chụp toàn bộ cửa sổ
- ✅ Hiển thị rõ thông tin (FPS, mode, gesture)
- ❌ Tránh chụp khi có lỗi hiển thị

## 🖼️ Xử lý ảnh sau khi chụp

### Crop & Resize
```bash
# Sử dụng tool online hoặc:
# - Windows: Paint, Paint 3D
# - Mac: Preview
# - Linux: GIMP
```

### Kích thước khuyến nghị
- Screenshots chính: 1280x720px
- Demo screen: 1920x1080px
- Ảnh cử chỉ: 800x600px

### Tối ưu dung lượng
- Sử dụng PNG cho ảnh có text
- Nén ảnh nếu > 500KB
- Tool: [TinyPNG](https://tinypng.com/)

## 📤 Upload lên GitHub

```bash
# Copy ảnh vào thư mục
cp screenshot.png docs/images/keyboard_mode.png

# Add và commit
git add docs/images/
git commit -m "Add screenshots for documentation"
git push
```

## ✅ Checklist cuối cùng

Trước khi commit, kiểm tra:
- [ ] Tất cả ảnh đã được chụp
- [ ] Ảnh rõ nét, không bị mờ
- [ ] Tên file đúng theo quy định
- [ ] Kích thước phù hợp
- [ ] Dung lượng đã được tối ưu
- [ ] README đã cập nhật đường dẫn ảnh

## 🎨 Tạo Banner (Optional)

Sử dụng Canva hoặc Figma để tạo banner đẹp:
1. Kích thước: 1200x630px
2. Nội dung: Logo + Tên dự án + Tagline
3. Màu sắc: Phù hợp với theme dự án
4. Font: Rõ ràng, dễ đọc

---

**Chúc bạn chụp ảnh thành công!** 📸

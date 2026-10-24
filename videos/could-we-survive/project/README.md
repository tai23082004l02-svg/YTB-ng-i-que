# Dữ liệu sản xuất — Could We Survive?

- `chapters.json`: 28 phần của kịch bản mới bằng tiếng Anh.
- `visual-plans.json`: mô tả 384 hình trước tuyển chọn.
- `assets/sheet-00.png` đến `sheet-31.png`: 32 bộ ảnh nguồn, mỗi bộ 3 cột × 4 hàng. `cell` đếm từ 0 đến 11, từ trái sang phải rồi từ trên xuống.
- `shots.json`: 371 hình được dùng, với bộ ảnh, ô ảnh, phần kịch bản, mốc thời gian và số khung hình. Không có ô nguồn nào được dùng lại.
- `timeline.json`, `captions.json`: timeline cuối và 681 đoạn phụ đề, đã điều chỉnh cùng nhịp đọc.
- `timing-summary.json`: thời lượng và thống kê.
- `normalization-settings.json`: số đo nguồn và bộ lọc cân âm lượng hai lượt; không sao chép các giá trị đo này sang âm thanh khác.
- `curation-notes.json`: ghi nhận một hình có lỗi niên đại đã bị loại.

## Hình đã loại cần tránh đưa lại

Bộ `sheet-15`, ô 4, là hình biển Trias được AI vẽ nhầm có trilobite sống; nhóm này đã tuyệt chủng trước Trias. Bản dựng dùng `sheet-29`, ô 5 — minh họa dấu tích hóa thạch ở ranh giới địa tầng — thay thế ở shot 201 (đếm từ 0). Ảnh nguồn đủ 384 ô vẫn được giữ, nhưng không phải mọi ô đều được dùng hoặc được chấp nhận về nội dung.

Các sơ đồ đều là minh họa khái niệm, không phải biểu đồ dữ liệu đo, bản đồ dự báo hoặc xác suất sống sót. Cảnh cổ đại không phải phim tư liệu; cảnh thành phố hiện đại là tình huống giả định.

## Nhân vật và cách dựng

Nhóm hiện đại tham chiếu: Mara, nữ kỹ sư tóc xoăn đen buộc lại, áo làm việc màu teal; Leon, tóc ngắn và áo gile màu gạch; Iris, bác sĩ tóc bob xám và áo trắng; Sam, áo nâu và mũ làm vườn. Tạo hình là hư cấu và cần giữ nhất quán khi sửa hình hoặc tạo cảnh bổ sung.

Giữ hình đứng yên, cắt thẳng, không thêm zoom/header/counter. Nếu chỉ sửa hình, giữ nguyên lời đọc và đồng bộ hiện tại; khi cần có thể trích âm thanh từ MP4 đã bàn giao.

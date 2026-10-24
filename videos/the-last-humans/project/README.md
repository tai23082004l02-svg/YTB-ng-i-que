# Dữ liệu sản xuất

- `chapters.json`: 20 phần kịch bản tiếng Anh.
- `visual-plans.json`: mô tả 288 hình trước khi tuyển chọn.
- `assets/sheet-00.png` đến `sheet-23.png`: 24 bộ ảnh nguồn; mỗi bộ có 3 cột × 4 hàng, tương ứng 12 hình.
- `shots.json`: 268 hình được dùng, thời gian bắt đầu/kết thúc và số khung hình. `sheet` là tên bộ ảnh, `cell` đếm từ 0 đến 11, từ trái sang phải rồi từ trên xuống.
- `timeline.json`: thời gian của từng phần sau khi hoàn thiện nhịp đọc.
- `captions.json`: 480 đoạn phụ đề có mốc thời gian.
- `timing-summary.json`: thời lượng, nhịp đọc và thống kê cảnh.

Không phải tất cả 288 hình nguồn đều được dùng. Một hình có sơ đồ dễ bị hiểu thành bậc thang tiến hóa (`sheet-17`, ô 5) đã bị loại; danh sách dựng dùng hình so sánh DNA (`sheet-20`, ô 9) thay thế.

Những dữ liệu này dùng để chỉnh sửa và tiếp tục sản xuất. Tệp MP4 hoàn chỉnh, kịch bản, phụ đề và tài liệu nguồn nằm ở thư mục phía trên. Lời đọc có thể trích từ MP4 khi cần giữ nguyên âm thanh để sửa hình.

# Dữ liệu dựng — The Last Blue Day

- assets/: 45 ảnh nguồn PNG, sheet-00 đến sheet-44; **4 cột × 4 hàng**, ô 0–15 theo hàng.
- shots.json: thứ tự, thời gian, số khung, loại cảnh và mô tả của 654 hình tuyển chọn.
- grid-crops.json: ranh giới thực tế từng tấm, không mặc định chia đều tuyệt đối. Bỏ mép 6 pixel, scale giữ tỷ lệ rồi crop giữa cố định.
- timeline.json / chapters.json: lời đọc, thời điểm và thời lượng từng phần.
- captions.json: mốc phụ đề từ token Kokoro; SRT ở thư mục cha.
- visual-plans.json: kế hoạch từng ô, không phải bảo đảm mọi hình AI thực hiện đúng.
- curation-notes.json: các ô loại và thay thế trong bản cuối; **không đưa hình sai trở lại**.
- story-bible.json: Mara là người dẫn chuyện hiện đại; cảnh tương lai là giả định, không phải một nhân vật sống qua hàng tỷ năm.
- claim-checks.json / ../SOURCES.md: nguồn, ngưỡng và giới hạn mô hình.
- normalization-settings.json: thống kê cân âm riêng bản lời đọc này.

Khi chỉ sửa hình, giữ lời đọc và phụ đề. Có thể lấy âm thanh từ MP4 cuối; WAV/model/cache không đưa vào Git. Khi dựng lại, áp dụng shots.json và curation-notes.json cuối, không chỉ lấy visual-plans rồi tái chọn tất cả các ô ban đầu.

Độ phân giải nguồn từng ô thấp hơn khung xuất. Người dùng đã chọn giữ cách tạo ảnh nhiều ô hiện tại sau khi thảo luận độ mềm; chưa chuyển sang 4 cảnh/tấm hoặc 1080p.

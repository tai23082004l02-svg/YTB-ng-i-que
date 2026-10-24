# Dữ liệu dựng — Without Us

- assets/: 46 tấm PNG, sheet-00 đến sheet-45, **4 cột × 4 hàng**, ô 0–15 theo hàng. 736 ô nguồn, 695 dùng. Hai tấm 44–45 bổ sung để tuyển chọn hình sửa nội dung.
- shots.json: thứ tự, thời gian, số khung, loại cảnh và mô tả của bản cuối.
- grid-crops.json: ranh giới thực tế từng tấm; bỏ mép 6 pixel, scale giữ tỷ lệ rồi crop giữa cố định. Không mặc định chia đều khi chưa kiểm tra.
- chapters.json/timeline.json: kịch bản và mốc lời đọc; captions.json: mốc token Kokoro; SRT ở thư mục cha.
- visual-plans.json: kế hoạch hình, không bảo đảm mọi ô AI làm đúng.
- curation-notes.json: **5 ô loại và thay thế; không đưa ô sai trở lại**. Source07/cell12 và34/cell12 xếp hạng sống/chết theo giống được thay bằng44/cell0–1; source29/cell5 và41/cell11 vệt sao băng trong bầu trời Mặt Trăng được thay bằng45/cell0 và2; source31/cell10 voi ma mút được thay bằng45/cell1.
- story-bible.json: toàn bộ con người vắng mặt; Scout/Juniper chỉ thuộc ngày đầu hoặc đoạn cuối quay lại ngày đầu.
- claim-checks.json/../SOURCES.md: cơ chế, giới hạn bằng chứng và giả định.
- normalization-settings.json: cân âm theo chính bản lời đọc này, không dùng offset như preset cho video khác.

Giữ âm thanh/phụ đề khi chỉ sửa hình. Có thể trích âm từ MP4 cuối. Không đưa WAV, model, cache hay bài nghiên cứu tải về vào Git. Kịch bản, timing và hình nguồn đủ để kiểm tra hoặc tái dựng; final shots/curation là dữ liệu có thẩm quyền, không tái chọn tất cả ô từ bản kế hoạch ban đầu.

Người dùng đã chọn giữ cách tạo ảnh nhiều ô và xuất 720p; chưa đổi sang 4 cảnh/tấm hoặc 1080p. Đây là hình nguồn được phóng lên khung xuất, không phải ảnh gốc HD/4K.

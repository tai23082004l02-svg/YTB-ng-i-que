# Dữ liệu dựng — 12 Shorts The Last Humans

- assets/sheet-00…18.png:19 tấm **4 cột × 4 hàng**, mỗi ô là **ảnh dọc 9:16**; ô 0–15 theo hàng. Không dùng cách chia 3×4 của ảnh phim dài.
- scripts.json/timeline.json:12 lời dẫn mới và thời lượng giọng.
- visual-plans.json: kế hoạch hình, không phải mọi ô đều hợp lệ.
- shots.json:252 cảnh tuyển chọn, có episode, start/end, frames, kind và mô tả.
- grid-crops.json: ranh giới thực tế; bỏ mép 6 pixel, scale giữ tỷ lệ rồi crop giữa cố định.
- curation-notes.json/exclusions.json:16 ô không dùng. Giữ loại bỏ khi sửa/tái dựng; không tự lấy lại toàn bộ ảnh từ kế hoạch gốc.
- episodes/01…12/: caption token times, cảnh, timing và cân âm riêng từng giọng. Không dùng offset bản này làm preset cho clip khác.
- art-direction.json: tham chiếu ảnh phim dài và vùng phụ đề. Chỉ số tấm **phụ thuộc thư mục**; đừng nhầm parent project/assets/ với shorts/project/assets/.

Phụ đề trắng viền tối, cỡ46 px tại720×1280, chừa250 px phía dưới và110 px bên phải để tránh giao diện Shorts. Khung video không có header, bộ đếm, zoom hay dải đen cố định.

Nguồn ảnh được tái bố cục dọc từ phong cách/nhân vật phim gốc; không nhận là ảnh gốc HD/4K hoặc ảnh khảo cổ thật. MP4 phim dài và lời đọc phim dài không bị thay đổi. Có thể trích âm từ từng MP4 cuối nếu chỉ sửa hình. WAV/model/cache/bài nghiên cứu tải về không đưa vào Git.

# Dữ liệu dựng — Where Is Everybody?

34 PNG trong assets/, mỗi bộ **3 cột × 4 hàng**, 12 ô đánh số **0–11** từ trái sang phải rồi từ trên xuống. **408 hình nguồn, 377 ô khác nhau thực sự dùng.** Hình đứng yên, cắt thẳng khoảng 5,17–5,83 giây.

- chapters.json: kịch bản 28 phần, 5.028 từ theo khoảng trắng.
- timeline.json: thời gian theo lời đọc thực tế.
- captions.json: 683 cue; shots.json: nguồn ô, thời gian và số frame, 24 fps.
- visual-plans.json: ý tưởng từng ô; ảnh thật có thể khác kế hoạch, cần xem khi sửa.
- timing-summary.json: âm thanh gốc 2122,975 giây; Kokoro am_michael speed 1.07, không chỉnh tempo thêm.
- normalization-settings.json: bộ lọc hai lượt theo số đo riêng của lời đọc này.
- curation-notes.json: cảnh 251 bỏ sheet-18 ô 9 vì hình giả định trông như một ngôi đền do con người xây; thay sheet-30 ô 5 là khoáng vật tự nhiên. Không đưa ô đã loại trở lại.

**grid-crops.json** ghi ranh giới hàng/cột thực tế theo từng bộ: không mặc định chia đều tuyệt đối. Bản cuối lùi vào 6 pixel nguồn để bỏ đường chia ô, scale giữ tỷ lệ rồi crop giữa cố định. Không có zoom động.

Các chương 0–26 chủ yếu dùng bộ cùng số; **chương 27 dùng bộ 33**, còn bộ 27–32 cung cấp hình bổ sung. Dùng shots.json làm dữ liệu chính thức thay vì đoán thứ tự từ tên ảnh.

Nora: nữ da đen, tóc xoăn ngắn, áo vàng và ghi-lê xanh teal. Eli: nam Đông Á, tóc đen ngắn, hoodie màu gỉ và ghi-lê navy. Dr Vega: phụ nữ Latina lớn tuổi, tóc bạc bob, áo tím. Đây là nhân vật kể chuyện hư cấu, không phải các tác giả nghiên cứu thật.

Đồ thị, bản đồ thiên hà, hành tinh và quỹ đạo là sơ đồ khái niệm, không đúng tỷ lệ và không phải dữ liệu phát hiện. Máy móc ngoài hành tinh và khu định cư giả định không được trình bày thành bằng chứng thật. Câu chuyện tín hiệu ở đầu/cuối là ví dụ hư cấu.

Khi chỉ sửa hình, có thể trích âm thanh từ MP4 để giữ thời gian và giọng; không cần tạo lại TTS. Không cân âm lượng thêm mà không đo. WAV trung gian, cache mô hình và môi trường Python không lưu trong kho.

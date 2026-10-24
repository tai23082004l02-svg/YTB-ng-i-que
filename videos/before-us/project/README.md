# Dữ liệu dựng — Before Us

28 bộ PNG trong assets/, mỗi bộ **3 cột × 4 hàng**, 12 ô đánh số **0–11** từ trái sang phải rồi từ trên xuống. Tổng 336 hình nguồn, **322 ô khác nhau thực sự dùng** trong shots.json. Mỗi cảnh khoảng 5,46–5,88 giây; hình đứng yên hoàn toàn.

- chapters.json: kịch bản 24 phần; timeline.json: thời gian theo âm thanh thực tế.
- captions.json: 566 cue; shots.json: nguồn ô, thời gian và số khung hình, 24 fps.
- visual-plans.json: ý tưởng từng hình.
- timing-summary.json: thời lượng gốc 1807,575 giây; Kokoro am_michael speed 1.07, không chỉnh tempo thêm.
- normalization-settings.json: bộ lọc cân âm lượng đo hai lượt, riêng cho bản này.
- curation-notes.json: loại sheet-16 ô 2 vì vẽ trilobite sống sai niên đại PETM; cảnh 217 dùng sheet-24 ô 4 là cảnh sông mang trầm tích. Không đưa ô sai trở lại video.

Nhân vật tương lai và các cảnh phòng thí nghiệm là hình kể chuyện; thành phố trong bong bóng tưởng tượng không phải phát hiện khảo cổ thật. Biểu đồ là sơ đồ khái niệm, không phải dữ liệu đo gốc.

Khi chỉ sửa hình, có thể trích âm thanh từ MP4 để giữ nguyên giọng và thời gian; tránh tạo lại lời đọc hoặc cân âm lượng thêm một lần mà không đo. Dùng phụ đề ở thư mục cha. WAV trung gian và môi trường Python không được lưu trong kho.

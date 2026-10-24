# Dữ liệu dựng — Born Between Stars

**40 ảnh PNG**, mỗi bộ **4 cột × 4 hàng**, 16 ô đánh số **0–15** từ trái sang phải rồi từ trên xuống. **640 hình nguồn, 594 ô khác nhau thực sự dùng.** Không dùng quy ước 3 × 4 của các video cũ cho dự án này.

- chapters.json: kịch bản 32 phần, 5.798 từ lời đọc theo khoảng trắng, không tính tiêu đề.
- timeline.json: thời gian theo lời đọc thực tế; captions.json: 767 cue từ token timing Kokoro.
- shots.json: nguồn ô, nội dung, loại cảnh, thời gian và số khung hình ở 24 fps. **simple = 3–4 giây, explanation = 5–6 giây**; trung bình khoảng 4,004 giây. Có 417 cảnh simple và 177 cảnh explanation.
- visual-plans.json: ý tưởng và phân loại của từng ô; xem hình thật khi sửa vì ảnh có thể khác kế hoạch.
- grid-crops.json: ranh giới hàng/cột thực tế theo từng bộ; không mặc định chia đều. Lùi vào 6 pixel nguồn, scale giữ tỷ lệ, crop giữa cố định. Không chuyển động máy quay.
- timing-summary.json: âm thanh gốc 2378,45 giây; Kokoro am_michael speed 1.07, không tempo bổ sung. 179 điểm cắt gần đầu/cuối cue khi phù hợp với ràng buộc thời gian; không phải mọi điểm cắt đều ở ranh giới câu.
- normalization-settings.json: thông số cân âm lượng đo riêng cho lời đọc này.
- curation-notes.json: cảnh 160 bỏ sheet-09 ô 0 có mũi tên trọng lực sai hướng; thay sheet-32 ô 4 là sơ đồ bố trí khoang. Không đưa ô đã loại vào lại.
- story-bible.json: nhân vật, các giai đoạn tuổi, bước nhảy thế hệ, bố cục tàu và giới hạn giả định.
- physics-checks.json: phép tính minh họa tốc độ, thời gian cruise và động năng; không phải thiết kế chuyến bay hay năng lượng động cơ tổng.

Lyra có HAI búi tóc và huy hiệu TRÒN; trải qua tuổi nhỏ, trưởng thành và già rồi qua đời. Sera có MỘT BÍM TÓC DÀI và huy hiệu TAM GIÁC, là nhân vật khác nhiều thế kỷ sau. Người sáng lập xuất hiện trong thời Sera chỉ dưới dạng ảnh lưu trữ hoặc khung so sánh lịch sử. Trái Đất trên thumbnail là ảnh đóng khung trong khoang, không phải hành tinh ngoài cửa sổ của Sera.

Tàu có hai vành cư trú đồng trục cách nhau trên thân dài; cảnh cruise không có lửa động cơ liên tục hoặc vệt warp. Các sơ đồ là khái niệm, không phải dữ liệu đo hoặc bản vẽ được chứng nhận.

Khi chỉ sửa hình, có thể trích âm thanh từ MP4 để giữ giọng và thời gian; tránh tạo lại TTS hoặc cân âm lượng thêm khi chưa đo. WAV trung gian, cache mô hình và môi trường Python không được lưu trong kho.

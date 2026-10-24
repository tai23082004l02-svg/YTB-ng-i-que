# Cài đặt đề xuất khi đăng lên YouTube

## 1. Điền thông tin chính

| Mục | Đề xuất cho video này |
| --- | --- |
| Title | `A Starship Leaves Earth. Nobody On Board Will See Its Destination.` |
| Description | Toàn bộ `description.txt`; đã có chương, nguồn và hashtag. |
| Thumbnail | `thumbnail-main.jpg`. |
| Audience | **No, it's not made for kids**: video kiến thức dành cho khán giả phổ thông/thanh thiếu niên và người lớn, không được sản xuất riêng cho trẻ em. Hoạt hình không tự đồng nghĩa với nội dung cho trẻ em. |
| Video language | **English (United States)** nếu có, hoặc English. |
| Title and description language | English. |
| Category | **Education**. |
| License | **Standard YouTube License**. |
| Tags | Dán nội dung `tags.txt` vào trường Tags trong Show more. |
| Comments | Bật bình luận nếu phù hợp với kênh; đăng rồi ghim nội dung `pinned-comment.txt`. |
| Visibility | **Public** khi bạn sẵn sàng đăng; có thể dùng Unlisted trong lúc tự kiểm tra trang xem. |

Không cần đặt vị trí quay là Mỹ để nhắm khán giả Mỹ. Nội dung và lời đọc đã dùng tiếng Anh Mỹ; không điền địa điểm hoặc ngày quay không có thật.

Video dài 39:38, nên tài khoản cần có quyền tải video dài hơn 15 phút. Nếu Studio báo giới hạn, thực hiện bước xác minh mà YouTube yêu cầu trong tài khoản của bạn. Thumbnail tùy chỉnh cũng cần tính năng tương ứng của kênh.

## 2. Khai báo sử dụng AI

Gói mô tả đã có **Production note** ghi rõ sử dụng ảnh minh họa AI và lời đọc tổng hợp. Không mô tả giọng Kokoro là giọng của một nhà khoa học hoặc người thật cụ thể.

Đề xuất chủ động khai báo việc sử dụng AI nếu Studio có trường **AI use / Altered content** cho phép khai báo nội dung tổng hợp này. Đọc đúng câu hỏi đang hiển thị: theo hướng dẫn YouTube, yêu cầu bắt buộc tập trung vào nội dung AI có vẻ chân thực hoặc có thể khiến người xem hiểu lầm sự kiện/người thật; hoạt hình phi hiện thực không tự động thuộc nhóm bắt buộc. Đây là video minh họa 2D, không phải phim tư liệu về một chuyến bay liên sao có thật. Việc đề xuất công khai cách sản xuất không có nghĩa mọi video hoạt hình dùng AI đều bắt buộc chọn cùng một đáp án.

## 3. Phụ đề và chương

- MP4 **đã có phụ đề gắn trực tiếp trên hình**.
- `captions.en-US.srt` là track phụ đề có thời gian để thêm trong YouTube Studio, giúp người xem dùng tính năng CC và dịch phụ đề. Khi bật CC, người xem có thể thấy phụ đề YouTube cùng dòng chữ đã gắn trong hình. Không cần gắn thêm chữ vào MP4 lần nữa.
- Danh sách 32 chương trong `description.txt` đã bắt đầu từ **00:00**, tăng dần và mỗi chương dài hơn 10 giây. Dán nguyên mô tả; chương do người đăng cung cấp sẽ được ưu tiên khi tính năng được hỗ trợ.
- Giữ nguyên các mốc thời gian cho bản MP4 hiện tại. Nếu bạn cắt đoạn đầu hoặc sửa thời lượng bằng YouTube Editor, cần đối chiếu lại mốc chương và phụ đề.

## 4. End screen và nội dung tiếp theo

Trong **20 giây cuối video, theo thanh timeline trong Studio**, có thể thêm một nút Subscribe và một video liên quan bằng YouTube Studio. Đặt ở vị trí tránh phụ đề phía dưới và tránh che gương mặt quan trọng.

Nếu `Where Is Everybody? / Fermi Paradox` đã được đăng trên chính kênh YouTube, có thể chọn video đó làm nội dung tiếp theo. Gói này không có URL YouTube của video ấy; hãy chọn video thật trong kênh, không dùng đường dẫn GitHub làm phần tử end screen.

Nếu kênh chưa có video liên quan, dùng phần tử phù hợp đang có thay vì tạo liên kết không tồn tại. Các bước này là tùy chọn, không thay đổi MP4 đã bàn giao.

## 5. Trình tự đăng nhanh

1. Tải MP4 và `youtube-upload-kit.zip` từ GitHub; giải nén gói đăng.
2. Upload MP4 trong YouTube Studio. Nếu bạn đã tải video lên, mở trang Details của video đang có để cập nhật thông tin, không cần upload lại chỉ vì đổi metadata.
3. Dán `title.txt`, `description.txt`; tải `thumbnail-main.jpg`.
4. Điền các cài đặt ở trên; thêm Tags trong Show more.
5. Thêm SRT nếu muốn có track CC; đối chiếu chương và phần khai báo AI theo giao diện của Studio.
6. Khi YouTube xử lý xong chất lượng 720p, xem thử trang video, thumbnail, âm thanh và chương. Đăng Public hoặc lên lịch theo lựa chọn của bạn.
7. Sau khi đăng, thêm và ghim bình luận đã chuẩn bị.

Các tác vụ hiện tại chỉ chuẩn bị tệp và đưa lên GitHub. Không có thao tác đăng YouTube hoặc lên lịch tự động được thực hiện.

## Nguồn hướng dẫn YouTube

Đối chiếu ngày 24/10/2026:

- [Thumbnail](https://support.google.com/youtube/answer/72431?hl=en): 16:9 cho video, chiều rộng tối thiểu 640 px; giới hạn tải hiện phụ thuộc thiết bị. Tệp JPEG 1280 × 720 trong gói dưới 2 MB, đáp ứng giới hạn mobile được nêu. Đây không phải tuyên bố rằng 1280 × 720 là độ phân giải khuyến nghị cao nhất hiện tại.
- [Video chapters](https://support.google.com/youtube/answer/9884579?hl=en): bắt đầu 00:00, ít nhất 3 mốc, mỗi chương tối thiểu 10 giây.
- [Tags](https://support.google.com/youtube/answer/146402?hl=en): vai trò nhỏ hơn title, thumbnail và description; hữu ích cho cách viết dễ nhầm. Không nhồi tags vào mô tả.
- [Audience](https://support.google.com/youtube/answer/9527654?hl=en).
- [Khai báo GenAI](https://support.google.com/youtube/answer/14328491?hl=en).
- [Video dài hơn 15 phút](https://support.google.com/youtube/answer/71673?hl=en).

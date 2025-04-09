# Nhận Diện Côn Trùng Bằng AI

Dự án này là một ứng dụng web sử dụng trí tuệ nhân tạo (AI) để nhận diện các loài côn trùng từ hình ảnh. Ứng dụng được xây dựng bằng Django và sử dụng mô hình học sâu (Deep Learning) để phân loại hình ảnh.

## Mục Tiêu
- Phát triển một hệ thống nhận diện côn trùng chính xác và dễ sử dụng.
- Ứng dụng công nghệ học sâu (Deep Learning) và mô hình Vision Transformer (ViT) để phân loại hình ảnh.
- Tích hợp mô hình AI vào ứng dụng web để người dùng có thể tải lên hình ảnh và nhận kết quả dự đoán.

## Tính Năng
- Giao diện web thân thiện cho phép người dùng tải lên hình ảnh côn trùng.
- Hệ thống tự động xử lý hình ảnh và trả về kết quả dự đoán loài côn trùng.
- Hỗ trợ nhiều loài côn trùng khác nhau, được định nghĩa trong tệp `classes.txt`.

## Công Nghệ Sử Dụng
- **Django**: Framework web chính để xây dựng ứng dụng.
- **PyTorch**: Thư viện học sâu để huấn luyện và chạy mô hình.
- **Vision Transformer (ViT)**: Mô hình học sâu được sử dụng để phân loại hình ảnh.
- **Albumentations**: Thư viện xử lý ảnh để tiền xử lý dữ liệu.
- **Pillow**: Thư viện xử lý ảnh trong Python.

## Cách Cài Đặt
1. **Clone dự án**:
   ```bash
   git clone https://github.com/anhkreal/TTNT-NhanDienConTrung.git
   cd TTNT-NhanDienConTrung
2. **Cài đặt các thư viện cần thiết**: Tạo môi trường ảo và cài đặt các thư viện:

  python -m venv venv
  source venv/bin/activate  # Trên Windows: venv\Scripts\activate
  pip install -r requirements.txt

3. **Chuẩn bị mô hình và dữ liệu**:

Đặt tệp mô hình vit_best.pth ở link https://drive.google.com/drive/u/0/folders/1wecrJ6FESxUWzGUbZeJcudaw0xfxUQaR vào thư mục gốc của dự án.
Đảm bảo tệp classes.txt chứa danh sách các loài côn trùng được hỗ trợ.
Chạy ứng dụng:

Truy cập ứng dụng: Mở trình duyệt và truy cập: http://127.0.0.1:8000

4. **Cấu Trúc Dự Án**
classifier/: Chứa các tệp chính của ứng dụng Django.
views.py: Xử lý logic của ứng dụng.
forms.py: Định nghĩa form tải lên hình ảnh.
models.py: Tải mô hình học sâu.
templates/classifier/: Chứa các tệp HTML cho giao diện web.
static/: Chứa các tệp tĩnh như CSS, JS.

6. **Ghi Chú**
   
Tệp .gitignore đã được cấu hình để bỏ qua các tệp mô hình (*.pth) nhằm tránh tải lên các tệp lớn.
Đảm bảo rằng bạn đã cài đặt đầy đủ các thư viện cần thiết trước khi chạy ứng dụng.
Đóng Góp
Nếu bạn muốn đóng góp cho dự án, vui lòng tạo một Pull Request hoặc mở một Issue trên GitHub.

Liên Hệ
Tác giả: Anhkreal
Email: [anhkhoahp2004@gmail.com]
Cảm ơn bạn đã quan tâm đến dự án! ```

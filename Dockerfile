# Sử dụng Python 3.9 làm base image
FROM python:3.9-slim

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép tệp tin yêu cầu
COPY requirements.txt .

# Cài đặt các gói yêu cầu
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép mã nguồn vào container
COPY . .

# Mở cổng 8000
EXPOSE 8000

# Chạy ứng dụng
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

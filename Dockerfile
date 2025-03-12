# Sử dụng image Python chính thức làm base image
FROM python:3.9-slim

# Đặt thư mục làm việc
WORKDIR /app

# Sao chép requirements.txt vào thư mục làm việc
COPY requirements.txt .

# Cài đặt các phụ thuộc Python
RUN pip install --no-cache-dir -r requirements.txt

# Sao chép toàn bộ dự án vào thư mục làm việc
COPY . .

# Expose cổng mà ứng dụng sẽ chạy
EXPOSE 8000

# Chạy ứng dụng
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
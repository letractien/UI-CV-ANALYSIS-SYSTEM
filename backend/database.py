import requests

url ="https://zep.hcmute.fit/7778/get_cv"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)  # In toàn bộ dữ liệu
else:
    print("Lỗi khi lấy dữ liệu:", response.status_code)

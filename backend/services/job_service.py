import requests
from fastapi.responses import JSONResponse

async def fetch_jobs():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/get_jds")
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)

async def fetch_ttjobs():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/get_openjd")
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)

async def fetch_eval():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/get_eval")
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)

async def add_job(data):
    try:
        response = requests.post("https://zep.hcmute.fit/7778/add_jd", json=data)
        if response.status_code == 200:
            return JSONResponse(content={"message": "Thêm công việc thành công!"})
        else:
            return JSONResponse(content={"message": "Lỗi khi thêm công việc"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)
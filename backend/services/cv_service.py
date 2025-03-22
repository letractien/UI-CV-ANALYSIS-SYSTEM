import requests
from fastapi.responses import JSONResponse

async def fetch_totalcv():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/cv_total")
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)

async def fetch_cvs():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/get_cv")
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)
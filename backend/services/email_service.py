import requests
from fastapi.responses import JSONResponse

async def fetch_email():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/get_email")
        if response.status_code == 200:
            data = response.json()
            print (data)
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware



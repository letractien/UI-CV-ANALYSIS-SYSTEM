from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests

router = APIRouter()

@router.get("/geteval", response_class=JSONResponse)
async def get_eval():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/get_eval")
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)

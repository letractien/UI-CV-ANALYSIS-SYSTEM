from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from backend.services.email_service import fetch_email
import httpx

router = APIRouter()

@router.get("/get_email", response_class=JSONResponse)
async def get_email():
    return await fetch_email()




@router.api_route("/send_email", methods=["GET", "POST"])
async def receive_email(request: Request):
    data = await request.json()
    
    # Gửi dữ liệu sang máy khác
    async with httpx.AsyncClient() as client:
        response = await client.post("https://zep.hcmute.fit/7778/send_email", json=data)
    
    return {"message": "Email forwarded", "response": response.json()}

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from backend.services.email_service import fetch_email

router = APIRouter()

@router.get("/get_email", response_class=JSONResponse)
async def get_email():
    return await fetch_email()



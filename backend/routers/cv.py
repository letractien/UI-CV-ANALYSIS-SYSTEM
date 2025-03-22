from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from backend.services.cv_service import fetch_cv


router = APIRouter()

@router.get("/total", response_class=JSONResponse)
async def get_totalcv():
    return await fetch_cv()

    
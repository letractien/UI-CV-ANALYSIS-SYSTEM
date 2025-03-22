from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from backend.services.cv_service import fetch_totalcv, fetch_cvs

router = APIRouter()

@router.get("/total", response_class=JSONResponse)
async def get_totalcv():
    return await fetch_totalcv()

@router.get("/getcvs", response_class=JSONResponse)
async def get_cvs():
    return await fetch_cvs()


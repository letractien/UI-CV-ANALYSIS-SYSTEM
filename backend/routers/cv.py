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
@router.get("/detailcv/{job_id}", response_class=HTMLResponse)
async def get_ui_edit_job(job_id: int):
    with open("./frontend/resources/detail_cv.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)


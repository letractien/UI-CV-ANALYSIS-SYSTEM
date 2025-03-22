from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from backend.services.job_service import fetch_jobs,fetch_ttjobs

router = APIRouter()

@router.get("/getjobs", response_class=JSONResponse)
async def get_jobs():
    return await fetch_jobs()

@router.get("/getttjobs", response_class=JSONResponse)
async def get_ttjobs():
    return await fetch_ttjobs()

@router.get("/addjob", response_class=HTMLResponse)
async def add_job():
    with open("./frontend/resources/add_job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/addjob/{job_id}", response_class=HTMLResponse)
async def edit_job(job_id: int):
    with open("./frontend/resources/edit_job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.post("/addjob", response_class=JSONResponse)
async def post_add_job(request: Request):
    data = await request.json()
    job_name = data.get("name")
    result = {"status": "success", "message": f"Job '{job_name}' added successfully!"}
    return JSONResponse(content=result)

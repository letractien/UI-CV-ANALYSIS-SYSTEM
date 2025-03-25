from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from backend.services.job_service import fetch_jobs, fetch_ttjobs, fetch_eval, add_job

router = APIRouter()

@router.get("/getjobs", response_class=JSONResponse)
async def get_jobs():
    return await fetch_jobs()

@router.get("/getttjobs", response_class=JSONResponse)
async def get_ttjobs():
    return await fetch_ttjobs()

@router.get("/geteval", response_class=JSONResponse)
async def get_eval():
    return await fetch_eval()

@router.post("/addjob", response_class=JSONResponse)
async def post_add_job(request: Request):
    data = await request.json()
    return await add_job(data)



@router.get("/job", response_class=HTMLResponse)
async def get_ui_job():
    with open("./frontend/resources/job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/addjob", response_class=HTMLResponse)
async def get_ui_add_job():
    with open("./frontend/resources/add_job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/detailjob/{job_id}", response_class=HTMLResponse)
async def get_ui_detail_job(job_id: int):
    with open("./frontend/resources/detail_job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@router.get("/editjob/{job_id}", response_class=HTMLResponse)
async def get_ui_edit_job(job_id: int):
    with open("./frontend/resources/edit_job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)
@router.get("/email/{job_id}", response_class=HTMLResponse)
async def get_ui_detail_job(job_id: int):
    with open("./frontend/resources/email.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)



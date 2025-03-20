import uvicorn
import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="./frontend"), name="frontend")

# GET UI
@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard():
    with open("./frontend/resources/dashboard.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

###########################################################################################################

# GET DATA
@app.get("/getjobs", response_class=JSONResponse)
async def get_jobs():
    try:
        response = requests.get("https://zep.hcmute.fit/7778/get_jds")
        if response.status_code == 200:
            data = response.json()
            return JSONResponse(content=data)
        else:
            return JSONResponse(content={"message": "Lỗi khi lấy dữ liệu từ database"}, status_code=500)
    except Exception as e:
        return JSONResponse(content={"message": f"Lỗi: {str(e)}"}, status_code=500)

# ADD JOB
@app.get("/addjob", response_class=HTMLResponse)
async def add_job():
    with open("./frontend/resources/add_job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# POST ADD JOB TO SERVER
@app.post("/addjob", response_class=JSONResponse)
async def post_add_job(request: Request):
    data = await request.json()
    job_name = data.get("name")
    result = {"status": "success", "message": f"Job '{job_name}' added successfully!"}
    return JSONResponse(content=result)

# EDIT JOB
@app.get("/editjob/{job_id}", response_class=HTMLResponse)
async def edit_job(job_id: int):
    with open("./frontend/resources/edit_job.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# POST EDIT JOB TO SERVER
@app.post("/addjob", response_class=JSONResponse)
async def post_add_job(request: Request):
    data = await request.json()
    job_name = data.get("name")
    result = {"status": "success", "message": f"Job '{job_name}' added successfully!"}
    return JSONResponse(content=result)

###########################################################################################################

@app.get("/geteval", response_class=JSONResponse)
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

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

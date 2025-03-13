import uvicorn
import requests
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse, JSONResponse

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="./frontend"), name="frontend")

@app.get("/index", response_class=HTMLResponse)
async def read_root():
    with open("./frontend/resources/index.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.get("/get_jobs", response_class=JSONResponse)
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

@app.get("/addjob", response_class=HTMLResponse)
async def read_root():
    with open("./frontend/resources/addjob.html", "r", encoding="utf-8") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

@app.post("/addjob", response_class=JSONResponse)
async def post_add_job(request: Request):
    data = await request.json()
    job_name = data.get("name")
    result = {"status": "success", "message": f"Job '{job_name}' added successfully!"}
    return JSONResponse(content=result)

@app.get("/get_eval", response_class=JSONResponse)
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

# @app.get("/editjob/{job_id}", response_class=JSONResponse)
# async def edit_job(job_id: int):
#     print(job_id)
#     return JSONResponse(content={"message": "Done"})

# @app.get("/deletejob/{job_id}", response_class=JSONResponse)
# async def delete_job(job_id: int):
#     print(job_id)
#     return JSONResponse(content={"message": "Done"})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

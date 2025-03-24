from backend.routers import dashboard, job, eval,cv,email
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="./frontend"), name="frontend")

app.include_router(dashboard.router)
app.include_router(job.router)
app.include_router(cv.router)
app.include_router(eval.router)
app.include_router(email.router)



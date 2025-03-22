from backend.routers import dashboard, job, eval,cv
from fastapi import FastAPI

app = FastAPI()
app.include_router(dashboard.router)
app.include_router(job.router)
app.include_router(eval.router)
app.include_router(cv.router)


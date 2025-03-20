from backend.routers import dashboard, job, eval
from fastapi import FastAPI

app = FastAPI()
app.include_router(dashboard.router)
app.include_router(job.router)
app.include_router(eval.router)

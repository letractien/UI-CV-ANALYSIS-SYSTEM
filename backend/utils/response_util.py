from fastapi.responses import JSONResponse

def create_response(status: str, message: str):
    return JSONResponse(content={"status": status, "message": message})

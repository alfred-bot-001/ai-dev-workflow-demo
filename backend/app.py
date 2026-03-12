from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI(title="AI Dev Workflow Demo")

# 获取当前文件所在目录的父目录
current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_dir = os.path.join(current_dir, "static")

# 挂载静态文件目录
app.mount("/static", StaticFiles(directory=static_dir), name="static")

@app.get("/")
async def root():
    return FileResponse(os.path.join(static_dir, "index.html"))

@app.get("/health")
async def health():
    return {"status": "ok"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

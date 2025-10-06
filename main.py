from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"message": "سرور در حال کار است 🎉"}

@app.post("/audio")
async def upload_audio(file: UploadFile = File(...)):
    return JSONResponse({"filename": file.filename, "status": "فایل دریافت شد ✅"})
from fastapi import FastAPI, UploadFile, File, Request
from fastapi.responses import HTMLResponse, FileResponse, JSONResponse
import os
import pandas as pd
from openpyxl import load_workbook
from fastapi.templating import Jinja2Templates

app = FastAPI()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

templates = Jinja2Templates(directory="templates")

ALLOWED_EXTENSIONS = {".xlsx", ".xls"}  # Allowed file types

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    files = os.listdir(UPLOAD_FOLDER)
    return templates.TemplateResponse("index.html", {"request": request, "files": files})

@app.post("/upload/")
async def upload_excel(file: UploadFile = File(...)):
    file_ext = os.path.splitext(file.filename)[1]
    if file_ext not in ALLOWED_EXTENSIONS:
        return JSONResponse(status_code=400, content={"error": "Only .xlsx and .xls files are allowed!"})

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {"message": f"File '{file.filename}' uploaded successfully!"}

@app.get("/download/{filename}")
def download_excel(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return JSONResponse(status_code=404, content={"error": "File not found"})
    return FileResponse(file_path, filename=filename)

@app.delete("/delete/{filename}")
def delete_file(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        return {"message": f"File '{filename}' deleted successfully!"}
    return JSONResponse(status_code=404, content={"error": "File not found"})

@app.get("/preview/{filename}")
def preview_excel(filename: str):
    file_path = os.path.join(UPLOAD_FOLDER, filename)
    if not os.path.exists(file_path):
        return JSONResponse(status_code=404, content={"error": "File not found"})
    
    try:
        df = pd.read_excel(file_path)
        preview_data = df.head(5).to_dict(orient="records")  # Convert first 5 rows to JSON
        return {"filename": filename, "preview": preview_data}
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": f"Failed to read Excel file: {str(e)}"})

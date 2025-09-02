from fastapi import FastAPI, File, UploadFile, Form
import os
import uuid

from tools import read_blood_report
from agents import doctor_response

app = FastAPI(title="Blood Test Report Analyser")

@app.get("/")
async def root():
    return {"message": "Blood Test Report Analyser API is running"}

@app.post("/analyze")
async def analyze_blood_report(
    file: UploadFile = File(...),
    query: str = Form(default="Summarise my Blood Test Report")
):
    file_id = str(uuid.uuid4())
    file_path = f"data/blood_test_report_{file_id}.pdf"
    
    os.makedirs("data", exist_ok=True)
    content = await file.read()
    with open(file_path, "wb") as f:
        f.write(content)
    
    # Extract report text
    report_text = read_blood_report(file_path)
    
    # Get simulated doctor response
    analysis = doctor_response(report_text, query)
    
    return {
        "status": "success",
        "query": query,
        "analysis": analysis,
        "file_processed": file.filename
    }

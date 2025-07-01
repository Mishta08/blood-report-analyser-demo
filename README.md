# Blood Test Analyzer using CrewAI & FastAPI

This project is a smart medical assistant that extracts and analyzes data from uploaded blood test PDF reports using CrewAI and FastAPI.

---

## Features

- Upload a blood test report PDF
- Extract key lab values (like Hemoglobin, WBC, Glucose, etc.)
- Use LLM agent logic (via CrewAI) to simulate a response to medical queries
- FastAPI backend for easy REST integration

---

## Bugs Fixed

### 1. `tools.py`
- Issue: Did not extract any lab values properly
- Fix: Rewrote regex patterns and added fallback handling for missing values

### 2. `main.py`
- Issue: File was saved but not passed correctly to the tool
- Fix: Confirmed file path and query were correctly passed to the `BloodTestReportTool`

### 3. `crewai_tools` import error
- Added instructions to install `crewai-tools` and `pymupdf` correctly

---

## Setup Instructions

### Step 1: Install dependencies

Make sure you have Python 3.9+ installed.

Then run:

```bash
pip install fastapi uvicorn crewai crewai-tools pymupdf

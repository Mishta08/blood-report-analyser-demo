**Blood Test Report Analyser (Demo)**

A lightweight Python demo project that extracts key information from blood test PDFs and provides simulated doctor-like recommendations via a FastAPI backend.
This project is designed for portfolio/demo purposes — no heavy AI frameworks or complex dependencies are required.

**Features**
-Extracts text from uploaded PDF blood test reports
-Provides a simulated “doctor analysis” and recommendations
-REST API implemented using FastAPI
-Lightweight and easy to run on any machine

---------------

**Installation**

1. Clone the repository:
git clone https://github.com/yourusername/blood-test-analyser-demo.git
cd blood-test-analyser-demo

2. Create a virtual environment (optional but recommended):
python -m venv .venv

.venv\Scripts\activate (For windows)


source .venv/bin/activate (For mac/linux)

3. Install dependencies:
pip install -r requirements.txt

----------------

**Usage**

1. Run the FastAPI server:
uvicorn main:app --reload

2. Open the interactive docs in your browser:
http://127.0.0.1:8000/docs

3. Test the /analyze endpoint:
-Upload a PDF file (e.g., sample_report.pdf)
-Enter a query like “Summarize my blood report”
-Click Execute to see the JSON response

--------------------

**Project Structure**
blood-test-analyser-demo/
│
├─ main.py           # FastAPI backend
├─ tools.py          # PDF text extraction
├─ agents.py         # Simulated doctor responses
├─ blood_test_report.pdf # Example PDF for demo
├─ requirements.txt  # Dependencies
└─ README.md         # Project overview and instructions

---------------------

**Example Response**
{
  "status": "success",
  "query": "Summarize my blood report",
  "analysis": "Doctor's analysis for query: Summarize my blood report\n\nSummary of your blood report: ...\nRecommendations:\n- Stay hydrated\n- Eat balanced diet\n- Consult a doctor for abnormal values\n",
  "file_processed": "sample_report.pdf"
}

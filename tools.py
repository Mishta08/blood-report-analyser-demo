from pypdf import PdfReader

def read_blood_report(file_path: str) -> str:
    """Extract text from a PDF blood test report."""
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
        return text[:2000]  # limit output for demo
    except Exception as e:
        return f"Error reading PDF: {e}"

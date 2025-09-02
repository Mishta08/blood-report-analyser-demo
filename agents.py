def doctor_response(report_text: str, query: str) -> str:
    """Generate a simple doctor-like response based on PDF text."""
    if not report_text:
        return "No blood report text found."
    
    # Lightweight simulation
    response = f"Doctor's analysis for query: {query}\n\n"
    response += "Summary of your blood report:\n"
    response += report_text[:500]  # first 500 chars
    response += "\n\nRecommendations:\n- Stay hydrated\n- Eat balanced diet\n- Consult a doctor for abnormal values\n"
    return response

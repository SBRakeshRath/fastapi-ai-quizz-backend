from pypdf import PdfReader
from fastapi import File


def getTextFromPDF (file: str):
    try:
        
        reader = PdfReader(file)
        
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return {
            "text": text,
            "status": "success"
        }
    except Exception as e:
        return {
            "error": str(e),
            "status": "error"
        }
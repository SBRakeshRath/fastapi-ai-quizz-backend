from fastapi import APIRouter, UploadFile, File
from app.services.pdfDetailExtractor_s import getTextFromPDF
from app.db.storePdfDetails import storePdfTranscriptInVectorDB
from app.model.pdfDetails_output import PDFDetailsOutput
import tempfile



router = APIRouter()


@router.post("/fetch-pdf-details",  response_model = PDFDetailsOutput)
def fetch_pdf_details(file: UploadFile):
    if file.content_type != "application/pdf":
        return {
            "error": "Invalid file type. Please upload a PDF file.",
            "status": "error",
        }
        
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_file.write(file.file.read())
        temp_file_path = temp_file.name

    print("Temporary file path:", temp_file_path)  # Debugging statement
    pdfText = getTextFromPDF(temp_file_path)
    if pdfText["status"] == "error":
        return {
            "error": pdfText["error"],
            "status": "error",
        }
        
        # now the AI part 
    storeResult = storePdfTranscriptInVectorDB(pdfText["text"])
    if storeResult["status"] == "error":
        return {
            "error": storeResult["message"],
            "status": "error",
        }
    print(storeResult)
    
    
    return {
        "status": "success",
        "message": "PDF details fetched and stored successfully.",
        "id": storeResult["id"]
    }

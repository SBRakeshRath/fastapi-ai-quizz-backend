from fastapi import APIRouter, UploadFile, File
from app.services.pdfDetailExtractor_s import getTextFromPDF
from app.db.storePdfDetails import storePdfTranscriptInVectorDB
from app.model.pdfDetails_output import PDFDetailsOutput



router = APIRouter()


@router.post("/fetch-pdf-details",  response_model = PDFDetailsOutput)
def fetch_pdf_details(file: UploadFile):
    if file.content_type != "application/pdf":
        return {
            "error": "Invalid file type. Please upload a PDF file.",
            "status": "error",
        }

    pdfText = getTextFromPDF(file)
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

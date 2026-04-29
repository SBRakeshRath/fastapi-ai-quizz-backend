from pydantic import BaseModel

class PDFDetailsInput(BaseModel):
    pdf_url: str
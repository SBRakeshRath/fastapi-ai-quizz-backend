# pdfDetails_output.py
from pydantic import BaseModel, Field
from typing import Optional

class PDFDetailsOutput(BaseModel):
    status: str = Field(description="The status of the PDF processing, either 'success' or 'error'")
    message: Optional[str] = Field(description="A message providing additional information about the processing result", default=None)
    id: Optional[str] = Field(description="The unique identifier for the stored PDF transcript in the vector database", default=None)
    error: Optional[str] = Field(description="An error message if the processing failed", default=None)

# tutorExplain_output.py


from pydantic import BaseModel, Field
from typing import  Optional


class TutorExplainOutput(BaseModel):
    status: str = Field(..., description="Status of the explanation request, either 'success' or 'error'.")
    explanation: Optional[str] = Field(None, description="The generated explanation for the user's wrong answer.")
    message: Optional[str] = Field(None, description="Error message if the status is 'error'.")
    error: Optional[str] = Field(None, description="Detailed error information if the status is 'error'.")

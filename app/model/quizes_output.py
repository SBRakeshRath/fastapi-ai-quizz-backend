from pydantic import BaseModel, Field
from typing import List, Optional
from app.services.generateQuiz_s import QuizResponse

class QuizesOutput(BaseModel):
    video_id: Optional[str] = Field(default=None, description="The ID of the YouTube video")
    num_quizzes: Optional[int] = Field(default=None, description="The number of quizzes generated")
    quizzes: Optional[QuizResponse] = Field(default=None, description="A list of generated quiz questions")
    status: str = Field(description="The status, either 'success' or 'error'")
    error: Optional[str] = Field(default=None, description="An error message if it failed")
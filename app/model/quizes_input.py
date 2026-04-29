from pydantic import BaseModel

class quizzesInput(BaseModel):
    video_id: str
    num_quizzes: int
    

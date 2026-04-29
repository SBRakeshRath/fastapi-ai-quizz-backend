from pydantic import BaseModel

class TutorExplainInput(BaseModel):
    video_id: str
    question: str
    user_wrong_answer: str
    correct_answer: str
    
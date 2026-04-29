from langchain_google_genai import ChatGoogleGenerativeAI
from pydantic import BaseModel, Field
from typing import List
from app.config.aiConfig import chat_model
from app.AI.generateQuizPrompt import generate_quiz_prompt



class QuizQuestion(BaseModel):
    id: int = Field(description="The question number (1 to 10)")
    question: str = Field(description="The text of the multiple choice question")
    options: List[str] = Field(description="Exactly 4 possible options for the user to choose from")
    correct_answer: str = Field(description="The exact text of the correct option")

class QuizResponse(BaseModel):
    questions: List[QuizQuestion]

def generateQuizzes(num_questions,transcript):
    
    prompt = generate_quiz_prompt(transcript,num_questions)
    sr = chat_model.with_structured_output(QuizResponse)
    
    try:
        response = sr.invoke(prompt)
        
        return response.model_dump()
    except Exception as e:
        print(f"Error generating quiz: {e}")
        return None
    
    
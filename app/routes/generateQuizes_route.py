from fastapi import APIRouter
from app.model.quizes_input import quizzesInput
from app.services.dbTextExtractor import dbTextExtractor
from app.services.generateQuiz_s import generateQuizzes

router = APIRouter()


@router.post("/generate-quizzes")
def generate_quizzes(data: quizzesInput):
    count = data.num_quizzes
    video_id = data.video_id

    try:
        transcript = dbTextExtractor(video_id)
        if transcript["status"] == "error":
            return {
                "error": transcript["message"],
                "status": "error",
            }
            
        quizzes = generateQuizzes(count, transcript["text"])
        
        if quizzes is None:
            return {
                "error": "Failed to generate quizzes",
                "status": "error",
            }
        
        
        

        return {
            "video_id": video_id,
            "num_quizzes": count,
            "quizzes": quizzes,
            "status": "success",
        }
    except Exception as e:
        return {
            "error": str(e),
            "status": "error",
        }



from app.model.tutorExplain_input import TutorExplainInput
from fastapi import APIRouter
from app.services.tutorExplainWrong_s import tutor_explain



router = APIRouter()

@router.post("/tutor-explain")
def tutor_explain_route(input: TutorExplainInput):
    try:
        result = tutor_explain(input)
        if result["status"] == "error":
            return {"status": "error", "message": result["message"]}
        return {"status": "success", "explanation": result["explanation"]}
    except Exception as e:
        print(f"Error in tutor_explain route: {e}")
        return {"status": "error", "message": str(e)}
    
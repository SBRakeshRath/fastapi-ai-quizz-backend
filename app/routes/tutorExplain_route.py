

from app.model.tutorExplain_input import TutorExplainInput
from fastapi import APIRouter
from app.services.tutorExplainWrong_s import tutor_explain
from app.model.tutorExplain_output import TutorExplainOutput




router = APIRouter()

@router.post("/tutor-explain", response_model = TutorExplainOutput)
def tutor_explain_route(input: TutorExplainInput):
    try:
        result = tutor_explain(input)
        if result["status"] == "error":
            return {"status": "error", "error": result["message"]}
        return {"status": "success", "explanation": result["explanation"]}
    except Exception as e:
        print(f"Error in tutor_explain route: {str(e)}")
        return {"status": "error", "error": str(e)}
    
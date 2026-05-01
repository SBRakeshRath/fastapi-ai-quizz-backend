

from app.config.aiConfig import chat_model
from app.db.searchTranscriptFromVectorDB import search_transcript_from_vector_db
from app.AI.wrongAnswerTutor import wrong_answer_tutor_prompt
from app.config.aiConfig import chat_model
from pydantic import BaseModel, Field

class TutorExplainChatModelResponse(BaseModel):
    explanation: str = Field(description="The explanation for the wrong answer based on the relevant context")


def tutor_explain(input):
    try:
        relevant_context = search_transcript_from_vector_db(input.video_id, input.question)
        print("Relevant context retrieved:", relevant_context)
        if relevant_context["status"] == "error":
            return {"status": "error", "message": "Failed to retrieve relevant context."}
        relevant_context = relevant_context["data"]
        if relevant_context.strip() == "":
            return {"status": "error", "message": "No relevant context found for the given question."}
        prompt = wrong_answer_tutor_prompt(input, relevant_context)
        
        response = chat_model.with_structured_output(TutorExplainChatModelResponse).invoke(prompt)
        return {"status": "success", "explanation": response.model_dump()}
            
        
        
    except Exception as e:
        print(f"Error in tutor_explain service: {e}")
        return {"status": "error", "message": str(e)}
        
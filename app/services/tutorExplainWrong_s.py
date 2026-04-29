

from app.config.aiConfig import chat_model
from app.db.searchTranscriptFromVectorDB import search_transcript_from_vector_db
from app.AI.wrongAnswerTutor import wrong_answer_tutor_prompt
from app.config.aiConfig import chat_model


def tutor_explain(input):
    try:
        relevant_context = search_transcript_from_vector_db(input.video_id, input.question)
        print("Relevant context retrieved:", relevant_context)
        if relevant_context["status"] == "error":
            return {"status": "error", "message": "Failed to retrieve relevant context."}
        relevant_context = relevant_context["data"]
        prompt = wrong_answer_tutor_prompt(input, relevant_context)
        
        response = chat_model.invoke(prompt)
        return {"status": "success", "explanation": response.content}
            
        
        
    except Exception as e:
        return {"status": "error", "message": str(e)}
        
from app.config.aiConfig import embed_model
from langchain_community.vectorstores import Chroma


def search_transcript_from_vector_db(video_id, relevant_text):
    try:
        vectorDB = Chroma(
            collection_name=video_id,
            embedding_function=embed_model,
            persist_directory="./vectorDB",
        )
        
        search_result = vectorDB.similarity_search(relevant_text, k=3)
        combined_result = "\n\n".join([doc.page_content for doc in search_result])
        
        return {
            "status": "success",
            "message": "Transcript retrieved successfully.",
            "data": combined_result,
        }
    except Exception as e:
        print(f"Error occurred while searching transcript: {e}")
        return {"status": "error", "message": str(e)}
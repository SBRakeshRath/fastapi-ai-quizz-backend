from app.config.firebaseConfig import firebase_db



def dbTextExtractor(collection_id):
    
    try:
        docs_generator = firebase_db.collection("pdf_transcripts").where("collection_name", "==", collection_id).stream()
        print(f"Fetching transcript for video ID: {collection_id}")
        docs_list = list(docs_generator)
        if len(docs_list) == 0:
            return {"status": "error", "message": "No transcript found for the given video ID."}
        for doc in docs_list:
            data = doc.to_dict()
            return {"status": "success", "text": data["text"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
        
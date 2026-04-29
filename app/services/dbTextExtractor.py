from app.config.firebaseConfig import firebase_db



def dbTextExtractor(collection_id):
    
    try:
        docs = firebase_db.collection("pdf_transcripts").where("collection_name", "==", collection_id).stream()
        for doc in docs:
            data = doc.to_dict()
            return {"status": "success", "text": data["text"]}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
        
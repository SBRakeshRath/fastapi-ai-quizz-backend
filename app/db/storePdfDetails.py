import os
import time

# 1. Correct LangChain Imports
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.firebaseConfig import firebase_db
from app.config.aiConfig import embed_model




def storePdfTranscriptInVectorDB(pdf_text):
    try:
        textSplitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )

        chunks = textSplitter.split_text(pdf_text)
        db_collection_name = "pdf_transcripts_" + str(int(time.time()))

        # store the text in firestore
        firebase_db.collection("pdf_transcripts").add(
            {
                "collection_name": db_collection_name,
                "text": pdf_text,
                "timestamp": time.time(),
            }
        )

        # 3. store in the vector database
        vectorDB = Chroma.from_texts(
            texts=chunks,
            embedding=embed_model,
            collection_name=db_collection_name,
            persist_directory="./vectorDB",
        )

        return {
            "status": "success",
            "message": "PDF transcript stored in vector database successfully.",
            "id": vectorDB._collection.name,
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

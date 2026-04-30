import os
import time
import uuid
from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from pinecone import Pinecone
from app.config.firebaseConfig import firebase_db
from app.config.aiConfig import embed_model

load_dotenv()

def storePdfTranscriptInVectorDB(pdf_text):
    try:
        # 1. Chunking (Standard)
        textSplitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
        chunks = textSplitter.split_text(pdf_text)
        
        db_collection_name = "pdf_transcripts_" + str(int(time.time()))

        # 2. Store in Firestore (Confirmed Working)
        firebase_db.collection("pdf_transcripts").add({
            "collection_name": db_collection_name,
            "text": pdf_text,
            "timestamp": time.time(),
        })

        # --- MANUAL STABLE UPSERT START ---
        
        # 3. Manually generate embeddings
        # This uses your Gemini model to turn text into lists of numbers
        print(f"Generating embeddings for {len(chunks)} chunks...")
        embeddings = embed_model.embed_documents(chunks)

        # 4. Format vectors for Pinecone
        # Pinecone expects a list of dictionaries: {"id": str, "values": list, "metadata": dict}
        vectors = []
        for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):
            vectors.append({
                "id": str(uuid.uuid4()), # Unique ID for each chunk
                "values": embedding,
                "metadata": {"text": chunk} # We store the text in metadata so we can retrieve it later
            })

        # 5. Initialize Pinecone and Upsert directly
        pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))
        index = pc.Index(os.getenv("PINECONE_COLLECTION_NAME"))

        print(f"Upserting to Pinecone namespace: {db_collection_name}...")
        
        # This direct call is much more stable on Vercel than the LangChain wrapper
        index.upsert(vectors=vectors, namespace=db_collection_name)
        
        # --- MANUAL STABLE UPSERT END ---

        return {
            "status": "success",
            "message": "PDF stored successfully using manual upsert.",
            "id": db_collection_name,
        }

    except Exception as e:
        print(f"Manual Storage Error: {e}")
        return {"status": "error", "message": str(e)}
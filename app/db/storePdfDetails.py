import os
import time
from langchain_core.documents import Document

from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.firebaseConfig import firebase_db
from app.config.aiConfig import embed_model
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma


load_dotenv()

from langchain_pinecone import PineconeVectorStore




def storePdfTranscriptInVectorDB(pdf_text):
    try:
        textSplitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )

        splitter = textSplitter.split_text(pdf_text)
        chunks = [Document(page_content=chunk) for chunk in splitter]
        
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
        # vectorDB = Chroma.from_texts(
        #     texts=chunks,
        #     embedding=embed_model,
        #     collection_name=db_collection_name,
        #     persist_directory="./vectorDB",
        # )
        
        
        vectorDB = PineconeVectorStore.from_documents(
            index_name=os.getenv("PINECONE_COLLECTION_NAME"),
            documents=chunks,
            embedding=embed_model,
            namespace=db_collection_name,
        )

        return {
            "status": "success",
            "message": "PDF transcript stored in vector database successfully.",
            "id": vectorDB._namespace,
        }
    except Exception as e:
        print(f"Error occurred while storing PDF transcript: {e}")
        return {"status": "error", "message": str(e)}

import os
import time
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from app.config.firebaseConfig import firebase_db
from app.config.aiConfig import embed_model
from dotenv import load_dotenv
from pinecone import Pinecone

load_dotenv()

from langchain_pinecone import PineconeVectorStore




def storePdfTranscriptInVectorDB(pdf_text):
    try:
        textSplitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=100
        )
        
        print("Splitting PDF text into chunks...")  # Debugging statement

        splitter = textSplitter.split_text(pdf_text)
        
        print(f"PDF text split into {len(splitter)} chunks.")  # Debugging statement
        chunks = [Document(page_content=chunk) for chunk in splitter]
        
        print("PDF text chunks created as Document objects.")  # Debugging statement
        db_collection_name = "pdf_transcripts_" + str(int(time.time()))
        
        print(f"Storing PDF transcript in Firestore collection: {db_collection_name}")  # Debugging statement

        # store the text in firestore
        firebase_db.collection("pdf_transcripts").add(
            {
                "collection_name": db_collection_name,
                "text": pdf_text,
                "timestamp": time.time(),
            }
        )

        print(f"PDF transcript stored in Firestore collection: {db_collection_name}")  # Debugging statement
        
        api_key = os.getenv("PINECONE_API_KEY")
        index_name = os.getenv("PINECONE_COLLECTION_NAME")

        if not api_key or not index_name:
            raise ValueError("Missing Pinecone API Key or Index Name in environment variables!")

        # 3. Explicitly initialize the Pinecone client
        # This prevents the client from searching the local filesystem for config files
        pc = Pinecone(api_key=api_key)
        
        print(f"Connecting to Pinecone index: {index_name}...")
        
        
        print(f"Storing PDF transcript in Pinecone vector database... on namespace: {db_collection_name} and index: {os.getenv('PINECONE_COLLECTION_NAME')}")  # Debugging statement
        vectorDB = PineconeVectorStore.from_documents(
            index_name=os.getenv("PINECONE_COLLECTION_NAME"),
            documents=chunks,
            embedding=embed_model,
            namespace=db_collection_name,
        )
        
        print(f"PDF transcript stored in Pinecone vector database under namespace: {db_collection_name}")  # Debugging statement

        return {
            "status": "success",
            "message": "PDF transcript stored in vector database successfully.",
            "id": db_collection_name,
        }
    except Exception as e:
        print(f"Error occurred while storing PDF transcript: {e}")
        return {"status": "error", "message": str(e)}

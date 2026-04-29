from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


# 2. Use the correct Embedding Model (NOT the Chat model!)
embed_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", google_api_key=api_key
)



chat_model = ChatGoogleGenerativeAI(
    model="models/gemini-2.5-flash-lite", google_api_key=api_key
)
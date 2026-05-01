from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
import os


load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment variables.")


embed_model = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001", google_api_key=api_key
)



chat_model = ChatGoogleGenerativeAI(
    model="models/gemini-3.1-flash-lite-preview", google_api_key=api_key
)
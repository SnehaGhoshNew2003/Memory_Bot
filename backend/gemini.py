from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from backend.config import GEMINI_API_KEY


llm = ChatGoogleGenerativeAI(
model="gemini-3-flash-preview",
temperature=0.2,
google_api_key=GEMINI_API_KEY
)


embeddings = GoogleGenerativeAIEmbeddings(
model="models/embedding-001",
google_api_key=GEMINI_API_KEY
)
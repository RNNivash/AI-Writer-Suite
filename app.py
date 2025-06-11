from fastapi import FastAPI, HTTPException
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.llms import Ollama
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import uvicorn

load_dotenv()

# Load the API key from .env
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

# Define request/response schemas
class TopicRequest(BaseModel):
    topic: str

class MessageRequest(BaseModel):
    content: str

class TextResponse(BaseModel):
    content: str

# FastAPI app
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

# Models
gemini_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", streaming=False)
llm = Ollama(model="llama3.2")  

# Prompts
essay_prompt = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
poem_prompt = ChatPromptTemplate.from_template("Write me a poem about {topic} for a 5 years child with 100 words")

@app.get("/")
async def root():
    return {"message": "Langchain API Server is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "models": ["ggemini-1.5-flash", "llama3.2"]}

@app.post("/gemini/invoke", response_model=TextResponse)
async def invoke_gemini(request: MessageRequest):
    try:
        result = gemini_model.invoke(request.content)
        return TextResponse(content=result.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/essay/invoke", response_model=TextResponse)
async def generate_essay(request: TopicRequest):
    try:
        chain = essay_prompt | gemini_model
        result = chain.invoke({"topic": request.topic})
        return TextResponse(content=result.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/poem/invoke", response_model=TextResponse)
async def generate_poem(request: TopicRequest):
    try:
        chain = poem_prompt | llm
        result = chain.invoke({"topic": request.topic})
        return TextResponse(content=result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
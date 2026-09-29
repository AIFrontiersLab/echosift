from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

class QueryRequest(BaseModel):
    text: str

class QueryResponse(BaseModel):
    result: str
    hash: str

def process_query(text: str) -> str:
    if not text or not text.strip():
        raise ValueError("Text cannot be empty")
    processed = text.strip().upper()
    return processed

@app.post("/query", response_model=QueryResponse)
async def query_endpoint(req: QueryRequest):
    try:
        result = process_query(req.text)
        h = hashlib.sha256(result.encode()).hexdigest()
        return QueryResponse(result=result, hash=h)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

def demo():
    print("Demo running...")
    result = process_query("hello world")
    print(f"Result: {result}")

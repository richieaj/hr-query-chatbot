from fastapi import FastAPI
from pydantic import BaseModel
from App.rag import search, for_response
from fastapi import HTTPException
app = FastAPI()
class Query(BaseModel):
    query: str
    top_k: int = 3
@app.post("/chat")
def chat(query: Query):
    try:
        results, scores = search(query.query, query.top_k)
        narration = for_response(results, scores)
        return {"summary": narration}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
app.mount("/static", StaticFiles(directory="."), name="static")
@app.get("/")
def serve_ui():
    return FileResponse("Frontend.html")

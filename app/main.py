from fastapi import FastAPI
from fastapi.routing import APIRouter


app = FastAPI(title="RAG Service")


# ---------- Routers
router = APIRouter()
app.include_router(router)

@app.get("/")
async def health_check():
    return {"status": "ok"}


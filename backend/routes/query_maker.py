from fastapi import APIRouter, FastAPI, Request,HTTPException
from fastapi.responses import JSONResponse
from controllers.query_maker.index import query_maker


app = FastAPI()
query_maker_router = APIRouter()


@query_maker_router.post("/query-maker/")
async def make_query(request:Request):
    try:
        body = await request.json()
    except Exception as e:
        raise HTTPException(status_code=400, detail="Invalid JSON")
    text_query = body.get("text", None)
    result= await query_maker(text_query)
    return result

from fastapi import APIRouter, FastAPI, Request
from fastapi.responses import JSONResponse

from routes.index import api_router

from fastapi.middleware.cors import CORSMiddleware

# Configure CORS

# Initialize FastAPI app
server = FastAPI()
server.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Allows the React app to access the API
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
main_router = APIRouter()


# Include routers
main_router.include_router(api_router, prefix="")
server.include_router(main_router)


# Define global exception handler
@server.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    print("Internal Server Error")
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

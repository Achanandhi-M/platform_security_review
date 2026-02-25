from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Secure Platform Demo")

app.include_router(router)
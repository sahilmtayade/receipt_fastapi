from contextlib import asynccontextmanager
from fastapi import FastAPI

from app.storage import ReceiptDB
from app.routes import router


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = ReceiptDB()
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router)

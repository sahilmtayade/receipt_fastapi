from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException

from app.models import Receipt
from app.storage import ReceiptDB


@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.db = ReceiptDB()
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return {"message": "Hello, World! Go to /docs!"}


@app.post("/receipts/process")
async def process_receipts(receipt: Receipt):
    db: ReceiptDB = app.state.db
    receipt_id = db.save_receipt(receipt)
    return {"receipt_id": receipt_id}


@app.get("/receipts/{id}/points")
async def test_so_far(id: str):
    db: ReceiptDB = app.state.db
    points = db.get_receipt_by_id(id)
    if points is None:
        raise HTTPException(status_code=404, detail="Receipt not found")
    return {"points": points}

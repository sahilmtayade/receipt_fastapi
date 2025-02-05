from fastapi import APIRouter, HTTPException, Request

from app.models import Receipt
from app.storage import ReceiptDB

router = APIRouter()


@router.get("/")
async def read_root():
    return {"message": "Go to /docs to view api! Default is localhost:8000/docs"}


@router.post("/receipts/process")
async def process_receipts(receipt: Receipt, request: Request):
    db: ReceiptDB = request.app.state.db
    receipt_id = db.save_receipt(receipt)
    return {"receipt_id": receipt_id}


@router.get("/receipts/{id}/points")
async def test_so_far(id: str, request: Request):
    db: ReceiptDB = request.app.state.db
    points = db.get_receipt_by_id(id)
    if points is None:
        raise HTTPException(status_code=404, detail="Receipt id not found")
    return {"points": points}

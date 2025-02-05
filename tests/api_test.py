from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.storage import ReceiptDB
from app.main import app

# Manually initialize the database for tests
app.state.db = ReceiptDB()  # This ensures the test client has access
client = TestClient(app)


def test_process_receipt():
    receipt_payload = {
        "retailer": "Target",
        "purchaseDate": "2022-01-01",
        "purchaseTime": "13:01",
        "items": [
            {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
            {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
            {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
            {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
            {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
        ],
        "total": "35.35",
    }

    # Step 1: Submit the receipt
    response = client.post("/receipts/process", json=receipt_payload)
    assert response.status_code == 200
    receipt_id = response.json()["receipt_id"]

    # Step 2: Retrieve points
    response = client.get(f"/receipts/{receipt_id}/points")
    assert response.status_code == 200
    assert response.json() == {"points": 28}


def test_invalid_receipt():
    response = client.post("/receipts/process", json={})
    assert response.status_code == 422  # Unprocessable Entity (Validation Error)


def test_nonexistent_receipt():
    response = client.get("/receipts/nonexistent_id/points")
    assert response.status_code == 404  # Not Found

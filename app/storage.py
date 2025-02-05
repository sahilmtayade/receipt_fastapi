from app.models import Receipt
import uuid
# I am used to using MongoDB and other complete solutions so this was fun!


class ReceiptDB:
    def __init__(self):
        self.receipts_db: dict[str, Receipt] = {}

    def _generate_id(self) -> str:
        receipt_id = str(uuid.uuid4())
        return receipt_id

    def save_receipt(self, receipt: Receipt) -> Receipt:
        receipt_id = self._generate_id()
        self.receipts_db[receipt_id] = receipt
        return receipt_id

    def get_receipt_by_id(self, receipt_id: str) -> Receipt:
        if receipt_id in self.receipts_db:
            return self.receipts_db[receipt_id]
        return None

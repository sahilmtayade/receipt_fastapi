from app.models import Receipt, Item
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
        points = self.calculate_points(receipt=receipt)
        self.receipts_db[receipt_id] = points
        return receipt_id

    def calculate_points(self, receipt: Receipt) -> int:
        points = 0

        # Rule 1: One point for every alphanumeric character in the retailer name
        points += sum(c.isalnum() for c in receipt.retailer)

        # Rule 2: 50 points if total is a round dollar amount with no cents
        if receipt.total.is_integer():
            points += 50

        # Rule 3: 25 points if total is a multiple of 0.25
        if receipt.total % 0.25 == 0:
            points += 25

        # Rule 4: 5 points for every two items on the receipt
        points += (len(receipt.items) // 2) * 5

        # Rule 5: Points based on item description length (if multiple of 3)
        for item in receipt.items:
            if len(item.short_description.strip()) % 3 == 0:
                points += -(-item.price * 0.2 // 1)  # Round up (// always rounds down)

        # Rule 6: 6 points if purchase date day is odd
        if receipt.purchase_date.day % 2 == 1:
            points += 6

        # Rule 7: 10 points if purchase time is between 2:00pm and 4:00pm
        if 14 <= receipt.purchase_time.hour < 16:
            points += 10

        return points

    def get_receipt_by_id(self, receipt_id: str) -> Receipt:
        if receipt_id in self.receipts_db:
            return self.receipts_db[receipt_id]
        return None

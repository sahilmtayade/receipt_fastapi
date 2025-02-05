from pydantic import BaseModel, Field, condecimal, field_validator

from datetime import datetime


class Item(BaseModel):
    short_description: str = Field(
        ..., min_length=1, max_length=1000, alias="shortDescription"
    )
    price: float = condecimal(gt=0, decimal_places=2)

    @field_validator("short_description", mode="before")
    @classmethod
    def clean_description(cls, value: str) -> str:
        """Trim whitespace from short description."""
        return value.strip()


class Receipt(BaseModel):
    retailer: str = Field(..., min_length=1, max_length=100)
    purchase_date: datetime = Field(..., alias="purchaseDate")
    purchase_time: datetime = Field(..., alias="purchaseTime")
    items: list[Item]
    total: float = condecimal(gt=0, decimal_places=2)

    @field_validator("purchase_date", mode="before")
    @classmethod
    def validate_date(cls, value: str) -> str:
        """Ensure purchaseDate follows YYYY-MM-DD format."""
        return datetime.strptime(value, "%Y-%m-%d")

    @field_validator("purchase_time", mode="before")
    @classmethod
    def validate_time(cls, value: str) -> str:
        """Ensure purchaseTime follows HH:MM 24-hour format."""
        return datetime.strptime(value, "%H:%M")

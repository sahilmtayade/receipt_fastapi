from pydantic import BaseModel, Field, field_validator

from datetime import datetime


class Item(BaseModel):
    short_description: str = Field(
        ..., min_length=1, max_length=100, alias="shortDescription"
    )
    price: str = Field(..., pattern=r"^\d+\.\d{2}$")

    @field_validator("short_description", mode="before")
    @classmethod
    def clean_description(cls, value: str) -> str:
        """Trim whitespace from short description."""
        return value.strip()


class Receipt(BaseModel):
    retailer: str = Field(..., min_length=1, max_length=100)
    purchase_date: str = Field(..., alias="purchaseDate")
    purchase_time: str = Field(..., alias="purchaseTime")
    items: list[Item]
    total: str = Field(..., pattern=r"^\d+\.\d{2}$")

    @field_validator("purchase_date", mode="before")
    @classmethod
    def validate_date(cls, value: str) -> str:
        """Ensure purchaseDate follows YYYY-MM-DD format."""
        if not cls.is_valid_date(value, "%Y-%m-%d"):
            raise ValueError("purchaseDate must be in YYYY-MM-DD format")
        return value

    @field_validator("purchase_time", mode="before")
    @classmethod
    def validate_time(cls, value: str) -> str:
        """Ensure purchaseTime follows HH:MM 24-hour format."""
        if not cls.is_valid_date(value, "%H:%M"):
            raise ValueError("purchaseTime must be in HH:MM format")
        return value

    @staticmethod
    def is_valid_date(value: str, fmt: str) -> bool:
        """Helper function to validate date/time formats."""
        try:
            datetime.strptime(value, fmt)
            return True
        except ValueError:
            return False

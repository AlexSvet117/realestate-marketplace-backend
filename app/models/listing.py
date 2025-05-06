from datetime import datetime, timezone
from sqlalchemy import String, DateTime, Integer,Boolean, ForeignKey, Text, Enum
from sqlalchemy.orm import mapped_column, relationship
from app.extensions import db

class Listing:
    __tablename__ = "listings"
    id = mapped_column(Integer, primary_key=True)
    owner_id = mapped_column(Integer, ForeignKey("users.id"), unique=False, nullable=False)
    title = mapped_column(String(255), nullable=True)
    description = mapped_column(Text, nullable=True)
    property_type = mapped_column(Enum('house', 'appartment', 'land'))

    created_at = mapped_column(DateTime, default=lambda:datetime.now(timezone.utc), nullable=False)
    updated_at = mapped_column(DateTime, default=lambda:datetime.now(timezone.utc), onupdate = lambda:datetime.now(timezone.utc), nullable=False)
    address = mapped_column(String(255), nullable=True)
    city = mapped_column(String(100), nullable=True)
    state = mapped_column(String(100), nullable=True)
    zip_code = mapped_column(String(100), nullable=True)


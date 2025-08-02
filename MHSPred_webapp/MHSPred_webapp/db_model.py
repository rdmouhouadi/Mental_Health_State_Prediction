from datetime import datetime
import reflex as rx

import sqlalchemy
from sqlmodel import SQLModel, Field

from . import utils

# Database model
class ContactEntryModel(rx.Model, table=True):
    first_name: str
    last_name: str | None = None
    email: str
    message: str

    created_at: datetime = Field(
        default_factory=utils.timing.get_utc_now,
        sa_type=sqlalchemy.DateTime(timezone=True),
        sa_column_kwargs={"server_default": sqlalchemy.func.now()},
        nullable=False
    )

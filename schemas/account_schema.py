# --------------------------------------------------
# Account Schema
# --------------------------------------------------

from sqlalchemy import Column, UUID
from utils.database import Base


class Account(Base):
    __tablename___ = "accounts"

    id = Column(UUID, primary_key=True)

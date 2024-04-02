from sqlmodel import SQLModel, Field
from pgvector.sqlalchemy import Vector
from typing import List, Optional
from sqlalchemy import Column, BigInteger

class Item(SQLModel, table=True):
    __tablename__ = "items"
    id: Optional[int] = Field(sa_column=Column(BigInteger, primary_key=True, autoincrement=True))
    embedding: List[float] = Field(sa_column=Column(Vector(3)))
from .database import db
from sqlmodel import SQLModel
from sqlalchemy import text

async def create_all():
    async with db.engine.begin() as conn:
        # Create the 'vector' extension if it doesn't exist
        await conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
        # Use SQLModel's meta_data to create all tables
        await conn.run_sync(SQLModel.metadata.create_all)


async def drop_all():
    async with db.engine.begin() as conn:
        # Use SQLModel's metadata to drop all tables
        await conn.run_sync(SQLModel.metadata.drop_all)

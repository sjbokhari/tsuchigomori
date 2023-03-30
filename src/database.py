from databases import Database
from sqlalchemy import (
    Boolean,
    Column,
    DateTime,
    ForeignKey,
    Identity,
    Integer,
    LargeBinary,
    MetaData,
    String,
    Table,
    create_engine,
    func,
)
from sqlalchemy.dialects.postgresql import UUID

from src.config import settings
from src.constants import DB_NAMING_CONVENTION, Enviroment

DATABASE_URL = settings.DATABASE_URL

engine = create_engine(DATABASE_URL)
metadata = MetaData(naming_convention=DB_NAMING_CONVENTION)

database = Database(DATABASE_URL, force_rollback=settings.ENVIROMENT.is_testing)

auth_user = Table(
    "auth_user",
    metadata,
    Column("id", Integer, Identity(), primary_key=True),
    Column("email", String, nullable=False),
    Column("password", LargeBinary, nullable=False),
    Column("is_admin", Boolean, server_default="false", nullable=False),
    Column("created_at", DateTime, server_default=func.now(), nullable=False),
    Column("updated_at", DateTime, onupdate=func.now()),
)
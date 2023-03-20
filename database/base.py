import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_DATABASE_PEM = os.environ.get("SQLALCHEMY_DATABASE_PEM")

# Create database engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URI, connect_args={"ssl": {"key": SQLALCHEMY_DATABASE_PEM}}
)

# Create database session
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

MYSQL_URL = os.environ.get("MYSQL_URL")
MYSQL_PORT = os.environ.get("MYSQL_PORT")
MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
MYSQL_DATABASE = os.environ.get("MYSQL_DATABASE")

# Create database engine
engine = create_engine(f'mysql+mysqlconnector://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_URL}:{MYSQL_PORT}/{MYSQL_DATABASE}')

# Create database session
SessionLocal = sessionmaker(bind=engine, autoflush=False)
Base = declarative_base()
#session = Session()
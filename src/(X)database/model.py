from sqlalchemy import Column, String, Integer, Date

from database import Base


class Hotel(Base):
    __tablename__ = 'hotel'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresse = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

class Prison(Base):
    __tablename__ = 'prison'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    addresse = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class Credentials(Base):
    __tablename__ = 'credentials'
    userName = Column(String(50), primary_key=True)
    emailAddress = Column(String(50), nullable=False)
    password = Column(String(20), nullable=False)

engine = create_engine('sqlite:///peedith.db')
Base.metadata.create_all(engine)
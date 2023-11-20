# models/database_model.py
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class DataModel(Base):
    __tablename__ = 'datatable_data'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    year = Column(Integer)
    period = Column(String)
    value = Column(Float)

# Create an SQLite database engine (replace with PostgreSQL details)
DATABASE_URL = "sqlite:///../test.db"
engine = create_engine(DATABASE_URL)

# Create the table
Base.metadata.create_all(bind=engine)

# Create a function to generate a new session
def create_database_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

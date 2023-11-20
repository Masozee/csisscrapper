# config/database_config.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///../test.db"  # Update with your PostgreSQL database URL

# Create the engine
engine = create_engine(DATABASE_URL)

# Create a function to generate a new session
def create_database_session():
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return SessionLocal()

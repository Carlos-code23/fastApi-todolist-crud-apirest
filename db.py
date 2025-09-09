from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:admin@localhost:5434/fastapi_db"

#crear motor
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()

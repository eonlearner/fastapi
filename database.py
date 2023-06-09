from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import config

DATABASE_URL = "mysql+mysqlconnector://root:Aniruddha#$1994@localhost:3306/eonlearning_db"

db_engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()


def get_db():
    """
    Function to generate db session
    :return: Session
    """
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

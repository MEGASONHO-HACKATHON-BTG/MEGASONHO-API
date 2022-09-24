import logging

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from src.config.database_url import DatabaseUrl

logger = logging.getLogger(__name__)

db = DatabaseUrl(prefix='HC').get_database_url()
db_engine = create_engine(db)
db_session = sessionmaker(autocommit=False, autoflush=False, bind=db_engine)

Base = declarative_base()

def get_database():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
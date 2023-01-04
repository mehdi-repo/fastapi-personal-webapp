
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Optional


my_database_connection = "postgresql://mehdi:mehdi123@localhost/fastapi_db"



engine = create_engine(my_database_connection)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
Base.metadata.create_all(bind=engine)


DATABASE_URL: Optional[str] = None
SECRET_KEY: Optional[str] = "default"

def sess_db():
    db = SessionFactory()
    try:
        yield db
    finally:
        db.close()



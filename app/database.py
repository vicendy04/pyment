import os

import sqlalchemy as _sql
import sqlalchemy.orm as _orm
from dotenv import load_dotenv
from sqlalchemy.orm import declarative_base

load_dotenv()

postgres_host = os.environ.get("POSTGRES_HOST")
postgres_db = os.environ.get("POSTGRES_DB")
postgres_user = os.environ.get("POSTGRES_USER")
postgres_password = os.environ.get("POSTGRES_PASSWORD")

DATABASE_URL = (
    f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}/{postgres_db}"
)

engine = _sql.create_engine(DATABASE_URL)
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

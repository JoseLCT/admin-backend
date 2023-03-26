from sqlalchemy import MetaData, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config.environment import ENV


engine = create_engine(ENV['DATABASE_URL'])

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

meta = MetaData()

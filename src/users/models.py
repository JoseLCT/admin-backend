from pydantic import BaseModel
from config.database import Base
from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String


class User(Base):
    __tablename__ = 'users'
    name = Column("name", String(100))
    last_name = Column("last_name", String(100))
    email = Column("email", String(100), primary_key=True)
    phone_number = Column("phone_number", String(50))
    country = Column("country", String(50))
    password = Column("password", String(255))

class UserSchema(BaseModel):
    name: str
    last_name: str
    email: str
    phone_number: str
    country: str
    password: str

    class Config:
        orm_mode = True
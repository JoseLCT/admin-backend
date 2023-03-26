from fastapi import APIRouter, Depends
from config.database import get_db
from src.users.models import User, UserSchema
from cryptography.fernet import Fernet
from sqlalchemy.orm import Session

users = APIRouter()
key = Fernet.generate_key()
fernet = Fernet(key)


@users.get('/users')
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@users.get('/users/{email}')
def get_user(email: str, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == email).first()
    return user


@users.post('/users')
def insert_user(user: UserSchema, db: Session = Depends(get_db)):
    user_check_email = db.query(User).filter(
        User.email == user.email).first()
    if user_check_email:
        return None
    new_user = User(name=user.name, last_name=user.last_name, email=user.email,
                    phone_number=user.phone_number, country=user.country, password=user.password)
    db.add(new_user)
    db.commit()
    return new_user


@users.put('/users/{email}')
def update_user(user: UserSchema, db: Session = Depends(get_db)):
    user_update = db.query(User).filter(User.email == user.email).first()
    user_update.name = user.name
    user_update.last_name = user.last_name
    user_update.phone_number = user.phone_number
    user_update.country = user.country
    db.commit()
    return user


@users.delete('/users/{email}')
def delete_user(email: str, db: Session = Depends(get_db)):
    db.query(User).filter(User.email == email).delete()
    db.commit()
    return None

from sqlalchemy.orm import Session
from apps.models.user import User

def get_users(db: Session):
    return db.query(User).all()
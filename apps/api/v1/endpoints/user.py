from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from apps.schemas.user import UserCreate, UserOut
from apps.crud.user import create_user, get_user_by_email, get_all_users
from apps.db.deps import get_db
from apps.core.security import verify_password, create_access_token

router = APIRouter()

@router.post("/register", response_model=UserOut)
def register(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db, user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    return create_user(db, user.email, user.password)


@router.post("/login")
def login(user: UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, user.email)

    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({"sub": db_user.email})
    return {"access_token": token, "token_type": "bearer"}


@router.get("/users")
def get_users(db: Session = Depends(get_db), response_model=List[UserOut]):
    db_users = get_all_users(db)
    return {"data":db_users,"message":"Sucessfully Fetched Users", "status_code":200}

    
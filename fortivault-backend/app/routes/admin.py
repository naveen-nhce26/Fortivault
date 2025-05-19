from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import SessionLocal
from app.models.user import User

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/admin/users")
def list_users(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.post("/admin/add-user")
def add_user(username: str, password: str, is_admin: bool = False, db: Session = Depends(get_db)):
    from passlib.hash import bcrypt
    hashed = bcrypt.hash(password)
    user = User(username=username, password=hashed, is_admin=is_admin)
    db.add(user)
    db.commit()
    return {"msg": "User added"}

@router.delete("/admin/delete-user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).get(user_id)
    if user:
        db.delete(user)
        db.commit()
        return {"msg": "User deleted"}
    return {"msg": "User not found"}

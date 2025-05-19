from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.database import Base

class File(Base):
    __tablename__ = "files"
    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String)
    encrypted_path = Column(String)
    owner_id = Column(Integer, ForeignKey("users.id"))
    risk_level = Column(String)

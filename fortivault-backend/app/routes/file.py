from fastapi import APIRouter, UploadFile, File, Depends
from app.utils.encryption import encrypt_file
from app.utils.ai_analysis import analyze_file_risk
from app.models.file import File as FileModel
from app.db.database import SessionLocal
import os

router = APIRouter()
UPLOAD_FOLDER = "encrypted_files/"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = file.file.read()
    encrypted = encrypt_file(content)
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    with open(file_path, "wb") as f:
        f.write(encrypted)

    risk = analyze_file_risk(content.decode(errors="ignore"))

    file_record = FileModel(filename=file.filename, encrypted_path=file_path, owner_id=1, risk_level=risk)
    db.add(file_record)
    db.commit()

    return {"msg": "File uploaded and encrypted", "risk": risk}

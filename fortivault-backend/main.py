from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import shutil

app = FastAPI()
#Naveen test
# Allow frontend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dummy in-memory users DB
users = {}

# -----------------------------
# MODELS
# -----------------------------
class SignupData(BaseModel):
    email: str
    password: str

class LoginData(BaseModel):
    email: str
    password: str

# -----------------------------
# ROUTES
# -----------------------------

@app.post("/signup")
async def signup(data: SignupData):
    if data.email in users:
        raise HTTPException(status_code=400, detail="Email already registered")
    users[data.email] = data.password
    return {"message": "Signup successful"}

@app.post("/login")
async def login(data: LoginData):
    if data.email in users and users[data.email] == data.password:
        return {"message": "Login successful"}
    raise HTTPException(status_code=401, detail="Invalid credentials")

# -----------------------------
# FILE UPLOAD
# -----------------------------

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)
    return {"message": "File uploaded successfully"}

from fastapi import FastAPI
from app.db.database import Base, engine
from app.routes import auth, admin, file, blockchain

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(file.router)
app.include_router(blockchain.router)

from fastapi import APIRouter
from app.utils.blockchain import blockchain_log

router = APIRouter()

@router.get("/blockchain/logs")
def get_logs():
    return blockchain_log

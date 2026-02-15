from fastapi import APIRouter
from jose import JWTError, jwt
from app.core.config import Settings

router = APIRouter()


@router.post("/login")
def login():
    token = jwt.encode(
        {"user": "test_user"},
        key=Settings.JWT_SECRET_KEY,
        algorithm=Settings.JWT_ALGORITHM
    )
    return {"access_token": token, "token_type": "bearer"}

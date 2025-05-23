# main.py
from fastapi import FastAPI, HTTPException, Query, Depends, Header
from pydantic import BaseModel
from database import SessionLocal, create_tables
from models import Prompt
from datetime import datetime
import uuid
from typing import List, Optional
from ai_engine import generate_responses  # your AI logic function

app = FastAPI()

# Create tables at startup
create_tables()

# --- Mock Users and Tokens ---
USERS = {
    "alice": "password123",
    "bob": "pass456",
}

TOKENS = {}  # token:str -> username:str

# --- Pydantic models ---
class LoginRequest(BaseModel):
    username: str
    password: str

class LoginResponse(BaseModel):
    access_token: str

class GenerateRequest(BaseModel):
    query: str

class GenerateResponse(BaseModel):
    casual_response: str
    formal_response: str

class HistoryItem(BaseModel):
    id: str
    user_id: str
    query: str
    casual_response: str
    formal_response: str
    created_at: datetime

# --- Authentication dependency ---
def get_current_user(authorization: Optional[str] = Header(None)) -> str:
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Unauthorized: Missing or invalid Authorization header")
    token = authorization[7:]
    user = TOKENS.get(token)
    if not user:
        raise HTTPException(status_code=401, detail="Unauthorized: Invalid token")
    return user

# --- Routes ---

@app.post("/login", response_model=LoginResponse)
def login(data: LoginRequest):
    if USERS.get(data.username) == data.password:
        token = str(uuid.uuid4())
        TOKENS[token] = data.username
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid username or password")

@app.post("/generate", response_model=GenerateResponse)
def generate(data: GenerateRequest, user_id: str = Depends(get_current_user)):
    # user_id here is validated username from token

    if not data.query or not data.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")

    session = SessionLocal()
    try:
        casual, formal = generate_responses(data.query)

        new_prompt = Prompt(
            id=str(uuid.uuid4()),
            user_id=user_id,
            query=data.query.strip(),
            casual_response=casual,
            formal_response=formal,
            created_at=datetime.utcnow()
        )
        session.add(new_prompt)
        session.commit()

        return {"casual_response": casual, "formal_response": formal}

    except Exception as e:
        session.rollback()
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    finally:
        session.close()

@app.get("/history", response_model=List[HistoryItem])
def get_history(user_id: str = Depends(get_current_user)):
    # user_id here is validated username from token

    session = SessionLocal()
    try:
        results = (
            session.query(Prompt)
            .filter(Prompt.user_id == user_id)
            .order_by(Prompt.created_at.desc())
            .all()
        )
        return results

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")

    finally:
        session.close()

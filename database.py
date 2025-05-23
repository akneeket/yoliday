from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, User  # Make sure User model is defined in models.py
from passlib.context import CryptContext

# SQLite database URL
DATABASE_URL = "sqlite:///prompts.db"

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Session maker
SessionLocal = sessionmaker(bind=engine, autoflush=False)

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Function to create tables
def create_tables():
    Base.metadata.create_all(bind=engine)

# Function to get a user by username
def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

# Function to verify a password
def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password, hashed_password)

# Function to hash a password
def get_password_hash(password: str):
    return pwd_context.hash(password)

# Function to create a new user (used for testing/demo/mock registration)
def create_user(db: Session, username: str, password: str):
    hashed_password = get_password_hash(password)
    new_user = User(username=username, hashed_password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Run this file directly to create the DB and tables
if __name__ == "__main__":
    create_tables()
    print("✅ Database and tables created successfully.")

    # Optional: Add a mock user for login testing
    db = SessionLocal()
    if not get_user_by_username(db, "user_1"):
        create_user(db, "user_1", "test123")
        print("🧪 Mock user 'user_1' with password 'test123' created.")
    db.close()

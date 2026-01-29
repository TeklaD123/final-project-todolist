import bcrypt
from models import User

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register(session, username, password):
    if session.query(User).filter_by(username=username).first():
        print("User already exists")
        return None
    user = User(
        username=username,
        password=hash_password(password)
    )
    session.add(user)
    session.commit()
    return user

def login(session, username, password):
    user = session.query(User).filter_by(username=username).first()
    if not user or not verify_password(password, user.password):
        print("Invalid credentials")
        return None
    return user

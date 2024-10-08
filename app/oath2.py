from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from . import schemas
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer

oath_schemes = OAuth2PasswordBearer(tokenUrl="login")

# SECRET_KEY 
# ALGORITHM
# ACESS_TOKEN_EXPIRE_TIME

SECRET_KEY = "79c9e5098f43aeb8d8164b3a7bf2a45a99bb34b6b6a23ac0f1d237dac1d30656"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_TIME = 30

# creating access token 
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_TIME)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

# verify the token 
def verify_access_token(token: str, credential_exception): 
    try: 
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    except: 
        raise credential_exception
    id: str = payload.get('user_id')

    token_data = schemas.TokenData(id=str(id))

    return token_data

# get current user 
def get_current_user(token: Session = Depends(oath_schemes)): 
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='unauthorized acess')

    return verify_access_token(token, credential_exception)


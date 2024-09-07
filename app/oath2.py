from jose import jwt, JWTError
from datetime import datetime, timedelta

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

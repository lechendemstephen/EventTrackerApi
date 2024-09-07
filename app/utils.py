from passlib.context import CryptContext

# creating an instance for passlib 

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def password_hasher(password: str): 

    return pwd_context.hash(password)

def verify_password(plain_password: str, hashedpassword): 

    return pwd_context.verify(plain_password, hashedpassword)


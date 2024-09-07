from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, schemas, models, utils, oath2

router = APIRouter(
    tags= ['Authentication']

)

@router.post('/users')
def create_user(user: schemas.User, db: Session = Depends(database.get_db)): 

    email = db.query(models.Users).filter(models.Users.email == user.email)

    # if email: 
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'user with email {user.email} already exist')
    
    # create a hashed password and send to the database 
    hashed_password = utils.password_hasher(user.password)
    user.password = hashed_password

    new_user = models.Users(
        **user.dict()
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post('/login')
def login(user: schemas.Login, db: Session = Depends(database.get_db)):

    db_user = db.query(models.Users).filter(models.Users.email == user.email).first()
# checkinng if user with email exist
    if not db_user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')
    
    if not utils.verify_password(user.password, db_user.password): 

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'invalid credentials')
    
    # creating accesstoken 
    access_token = oath2.create_access_token({"user_id": db_user.id })


    return {
        "access": access_token
    }
        







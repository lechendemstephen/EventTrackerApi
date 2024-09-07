from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import database, schemas, models

router = APIRouter(
    tags= ['Events'], 
    prefix= '/events'
)


@router.get('/')
def all_events(db: Session = Depends(database.get_db)): 

    all_events = db.query(models.Events).all()

    return {
        'All_Events':  all_events
    }

# create Event
@router.post('/')
def create_event(event: schemas.Event, db: Session = Depends(database.get_db)): 

    new_event = models.Events(
        **event.dict()
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)

    return new_event

# get single event based on ID 
@router.get('/{id}')
def get_single_event(id:int, db: Session = Depends(database.get_db)): 
    event = db.query(models.Events).filter(models.Events.id == id).first()

    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no event found with ID: {id}')
    
    return event

# delete single event 
@router.delete('/{id}')
def delete_event(id: int, db: Session = Depends(database.get_db)): 
    event = db.query(models.Events).filter(models.Events.id == id)

    if not event: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'no event found with ID {id}')
    event.delete()
    db.commit()

    return {
        "message": "succcessfully deleted"
    }

# upating a particular event 
@router.put('/{id}')
def update_event(id: int, db: Session = Depends(database.get_db)): 

    event = db.query(models.Events).filter(models.Events.id == id)
    
    if not event: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post with ID: {id} not found')
    
    for key, value in event.items.dict():
        if not value: 
            setattr(event, key, value)
            
    return event


    
    




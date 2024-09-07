from fastapi import APIRouter


router = APIRouter(
    tags= ['Events'], 
    prefix= '/events'
)


@router.get('/')
def all_events(): 

    return {
        'All_Events': " All events works"
    }




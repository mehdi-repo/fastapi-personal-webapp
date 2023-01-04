from fastapi import APIRouter, Depends, HTTPException, Request, Form
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse

#themplate time
import starlette.status as status

# connect to DB
from databse.connection import sess_db
from sqlalchemy.orm import Session


# model
from models.contact import ContactModel

# repository
from repository.contact import ContactRepository

# template
from fastapi.templating import Jinja2Templates
templates=Jinja2Templates(directory="templates/")


router = APIRouter()


@router.get("/")
def root(request:Request)-> dict:
    return templates.TemplateResponse("pages/contact.html",
                                      {
                                          "request":request
                                      })                                   
        
      
@router.post("/")
def contact_message(db: Session = Depends(sess_db), email: str = Form(), title: str = Form(), description: str = Form()) :
    contactRepository = ContactRepository(db)

    contact = ContactModel(email=email, title=title,description=description)
    success = contactRepository.create_Contact(contact)
    if success:
        # return ORJSONResponse(content=jsonable_encoder(success), status_code=201)
        return RedirectResponse('/contact', status_code=status.HTTP_302_FOUND) 
 
    else:
        raise HTTPException(
            detail="message': 'create signup problem encountered"
        )
from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates



from fastapi.templating import Jinja2Templates


router = APIRouter()
templates=Jinja2Templates(directory="templates/")


@router.get("/")
def root(request:Request)-> dict:
    return templates.TemplateResponse("/pages/about.html",
                                      {
                                          "request":request
                                      })                                   
        

      
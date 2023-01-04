from fastapi import APIRouter, Depends, Request
from starlette.responses import RedirectResponse
from fastapi.responses import HTMLResponse
from models.user import UserModel
from fastapi.templating import Jinja2Templates
from scurity.secur import get_current_user_from_cookie
templates=Jinja2Templates(directory="templates/")


router = APIRouter()


@router.get("/", response_class=HTMLResponse)
def event(request: Request, user: UserModel = Depends(get_current_user_from_cookie)):
    if user is None :
        response = RedirectResponse(url='/user/signin')
        return response
    else:
        context = {
            "user": user,
            "request": request
        }
        return templates.TemplateResponse("pages/event.html", context)

        
      

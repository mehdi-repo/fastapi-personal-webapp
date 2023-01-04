from fastapi import FastAPI,Request
import uvicorn
from api import user,event,contact,about
from databse.connection import Base,engine
from fastapi.templating import  Jinja2Templates
from fastapi.staticfiles import StaticFiles
# FastAPI instance
app=FastAPI()

#db engin
Base.metadata.create_all(bind=engine)

# Routers
app.include_router(user.router,prefix="/user")
app.include_router(contact.router,prefix="/contact")
app.include_router(about.router,prefix="/about")
app.include_router(event.router,prefix="/event")
#StaticFiles
app.mount("/static",StaticFiles(directory="static",html=True),name="static")
templates=Jinja2Templates(directory="templates/")


@app.get("/")
def main(request:Request)-> dict:
    return templates.TemplateResponse("/base.html",{"request":request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080,reload=True)
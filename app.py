import uvicorn # équivalent d'un serveur web
from fastapi import FastAPI # Outils pour API
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


 



app = FastAPI() # créer une instance

#Initialiser le moteur de template
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")
#créer une route
@app.get("/home", response_class=HTMLResponse)
async def read_home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request, # Obligatoire
            "name": "Mario",
            "job":"plombier",
            "brother":"Luigi",
            "friends": ["Toad","Daisy","Yoshi","Donkey kong"]
        }

    )

@app.get("/")
async def read_root():
    return {"message":"Hello World"}

@app.get("/test")
async def read_root():
    return {"message":"Hello Worldz"}

# Lancement du serveur
if __name__=="__main__":
    uvicorn.run(app,host="127.0.0.1", port=8000)

    """
    swagger (automatique) = doc de l'api

    -   https://127.0.0.1:8000/docs
    -   https://127.0.0.1:8000/openapi.json

    """
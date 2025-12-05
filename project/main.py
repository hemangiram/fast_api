from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses  import HTMLResponse
from fastapi import Request
import os



app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Correct path to static folder
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")

# Correct path to templates folder
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))



#static api
@app.get("/about", response_class=HTMLResponse)
def about_page(request: Request):
    return templates.TemplateResponse("index.html", {"request":request})


#dynamic api
@app.get("/user/{name}", response_class=HTMLResponse)
def user_profile(name: str, request: Request):
    return templates.TemplateResponse("user.html", {
        "request": request,
        "user_name": name
    })
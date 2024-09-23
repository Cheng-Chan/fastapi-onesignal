from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from src.config.config import APP_NAME, VERSION

from src.routes import notifications

from src.routes.notifications import main


app = FastAPI(
  title=APP_NAME,
  version=VERSION
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_methods=["*"],
  allow_headers=["*"],
  allow_credentials=True,
)

app.include_router(notifications.main.router)

@app.get("/")
def docs():
  """
  Redirect to documentation (`/docs/`)
  """
  return RedirectResponse(url="/docs/")
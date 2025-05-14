from fastapi import FastAPI
from contextlib import asynccontextmanager
from starlette.responses import RedirectResponse
from app.routes import images, model, detect
#from app.routes.darknet import model
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Python Quickstart using FastAPI",
    version="1.0.1",
    description="""
    A quickstart API using Python with Couchbase, FastAPI from couchbase portal modification example.

    For details on the API, please check the tutorial on the Couchbase Developer Portal: https://developer.couchbase.com/tutorial-quickstart-fastapi-python/

    Github Repo: https://github.com/couchbase-examples/python-quickstart-fastapi/tree/main/

    """,
    #lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las fuentes (puedes restringirlo)
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)


app.include_router(images.router, prefix="/images", tags=["images"])
app.include_router(model.router, prefix="/model", tags=["model"])
app.include_router(detect.router, prefix="/detect", tags=["detect"])

# Redirect to Swagger documentation on loading the API for demo purposes
@app.get("/", include_in_schema=False)
def redirect_to_swagger():
    return RedirectResponse(url="/docs")
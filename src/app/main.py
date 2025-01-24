from fastapi import FastAPI



app = FastAPI(
    title="Python Quickstart using FastAPI",
    version="1.0.1",
    description="""
    A quickstart API using Python with Couchbase, FastAPI from couchbase portal modification example.

    For details on the API, please check the tutorial on the Couchbase Developer Portal: https://developer.couchbase.com/tutorial-quickstart-fastapi-python/

    Github Repo: https://github.com/couchbase-examples/python-quickstart-fastapi/tree/main/

    """,
    lifespan=lifespan,
)



# Redirect to Swagger documentation on loading the API for demo purposes
@app.get("/", include_in_schema=False)
def redirect_to_swagger():
    return RedirectResponse(url="/docs")
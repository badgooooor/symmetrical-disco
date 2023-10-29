from fastapi import FastAPI

from routes.keys import keyRouter
from routes.users import userRouter

app = FastAPI()

app.include_router(keyRouter)
app.include_router(userRouter)

@app.get("/")
def read_root():
    return {"Hello": "World"}

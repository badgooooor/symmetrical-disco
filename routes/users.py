from fastapi import APIRouter
from pydantic import BaseModel

class UpdateUserBody(BaseModel):
  username: str

userRouter = APIRouter(
  prefix="/users",
  tags=["key"],
  responses={404: {"description": "Not found"}}
)

@userRouter.post("/")
async def create_user():
  return {"description": "Create user"}

@userRouter.put("/user/{user_id}")
async def update_user(user_id: str, body: UpdateUserBody):
  return {"user_name": body.username, "user_id": user_id}

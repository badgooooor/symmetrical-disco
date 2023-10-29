from fastapi import APIRouter
from pydantic import BaseModel
from hashlib import blake2b
import secrets

from utils.keys import get_hashed_token

class ValidateKeyBody(BaseModel):
  token: str

keyRouter = APIRouter(
  prefix="/key",
  tags=["key"],
  responses={404: {"description": "Not found"}}
)

# Create key
# - Create token and store hashed key (with name) in database
# - Return token to user
@keyRouter.post("/")
async def create_key():
  token = secrets.token_urlsafe(16)

  # Hashed key and insert to database.
  hashed = get_hashed_token(token)

  # Return token, for hashed token is for debug.
  return {"token": token, "hashed": hashed}

# Validate key
# - Create hash token with token from body
# - Find token by hashed token and check user_id in JWT
# - Return true if it existed and is called user owned an token
@keyRouter.get("/validate")
async def validate_key(body: ValidateKeyBody):
  return {"result": True}

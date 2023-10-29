from fastapi import APIRouter
from pydantic import BaseModel

class CreateSubscriptionBody(BaseModel):
  user_id: str
  subscription_id: str

subscriptionRouter = APIRouter(
  prefix="/subscription",
  tags=["key"],
  responses={404: {"description": "Not found"}}
)

# Create subscription
# - Check customer_id in Stripe (and create if not existed)
# - Create subscription to customer_id in Stripe
# - Account to database.
@subscriptionRouter.post("/")
async def create_subscription(body: CreateSubscriptionBody):
  return {"subscription_id": body.user_id + "_" + body.subscription_id}

# Unsubscribe
# - Get customer's subscription_id in Stripe
# - Unsubscribe subscription_id in Stripe
# - Account to database.
@subscriptionRouter.delete("/{user_subscription_id}")
async def remove_subscription(user_subscription_id: str):
  return {"subscription_id": user_subscription_id}

# Get subscription
# - Get customer's subscription_id in Stripe
# - Unsubscribe subscription_id in Stripe
# - Account to database.
@subscriptionRouter.get("/user/{user_id}")
async def get_user_subscription(user_id: str):
  # should get subscription from Stripe.
  subscription_id = ["sub_1", "sub_2", "sub_3"]
  
  return {"user_id": user_id, "subscription_id": subscription_id}

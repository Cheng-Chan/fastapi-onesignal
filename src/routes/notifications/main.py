from fastapi import APIRouter
from fastapi import HTTPException

from . import schemas, controller

router = APIRouter(
  prefix="/notifications",
  tags=["Notifications"],
  responses={404: {"description": "Page not found"}}
)

@router.post("/", response_model=schemas.NotificationResponse)
async def post_notification(notification: schemas.NotificationSchema):
  success = controller.send_notification(notification)
  if not success:
    raise HTTPException(status_code=500, detail="Notification failed")
  return schemas.NotificationResponse(success=True, message="Notification sent successfully")
import os

from dotenv import load_dotenv

from onesignal_sdk.client import Client

from . import schemas

load_dotenv('.env.local')

ONESIGNAL_APP_ID = os.getenv("ONESIGNAL_APP_ID")
ONESIGNAL_API_KEY = os.getenv("ONESIGNAL_API_KEY")

onesignal_client = Client(app_id=ONESIGNAL_APP_ID, rest_api_key=ONESIGNAL_API_KEY)

def send_notification(notification: schemas.NotificationSchema):
  notification_body = {
        'headings': {'en': notification.title},
        'contents': {'en': notification.message},
        'include_player_ids': [notification.user_id]
    }
  response = onesignal_client.send_notification(notification_body)
  return response.status_code == 200
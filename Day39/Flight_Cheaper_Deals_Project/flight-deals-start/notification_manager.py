# This class is responsible for sending notifications with the deal flight details.
from twilio.rest import Client
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path='../../../.env')

account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_VIRTUAL_NUMBER = '+13345818652'
MY_NUMBER = '+917020419875'

class NotificationManager:
    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message_body):
        message = self.client.messages.create(
            from_=TWILIO_VIRTUAL_NUMBER,
            body = message_body,
            to=MY_NUMBER,
        )
        print(message.sid)

    # def send_whatsapp(self, message_body):
    #     message = self.client.messages.create(
    #         from_=f'whatsapp:{os.environ["TWILIO_WHATSAPP_NUMBER"]}',
    #         body=message_body,
    #         to=f'whatsapp:{os.environ["TWILIO_VERIFIED_NUMBER"]}'
    #     )
    #     print(message.sid)
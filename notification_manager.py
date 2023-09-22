from twilio.rest import Client
import  smtplib
TWILIO_SID = "AC9b5803d54c1b16d367885fc8d87f398b"
TWILIO_AUTH_TOKEN = "94ff5170a1002b0e67298c178bed10b7"
TWILIO_VIRTUAL_NUMBER = "+15702184141"
TWILIO_VERIFIED_NUMBER = "+91 88706 80558"
MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = "uzinaru1234@gmail.com"
MY_PASSWORD = "enoevaogbmricqkr"

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        print(message.sid)

    def send_emails(self, emails, message):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )

import os
import emails
from dotenv import load_dotenv

load_dotenv()

message = emails.html(
    html="<strong>It's there!</strong>",
    subject="SMTP test message",
    mail_from=os.getenv("FROM_MAIL"),
)


r = message.send(
    to=os.getenv("TO_MAIL"),
    smtp={
        "host": os.getenv("SMTP_HOST"),
        "port": 587,
        "user": os.getenv("SMTP_USER"),
        "password": os.getenv("SMTP_PASSWORD"),
        "tls": True,
    },
)

assert r.status_code == 250

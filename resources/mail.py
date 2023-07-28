import smtplib
import threading
from email.message import EmailMessage
from decouple import config


mail_server = None

from_email = config('VERIFICATION_EMAIL')

def mail_server_init():
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    verification_email = from_email
    verification_email_password = config('VERIFICATION_EMAIL_PASSWORD')

    global mail_server

    mail_server = smtplib.SMTP(smtp_server, smtp_port)
    mail_server.starttls()
    mail_server.login(verification_email, verification_email_password)


def make_email_message(subject, content, to_email, content_subtype=None):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(content, subtype=content_subtype)
    return msg


def send_email_message(message, to_email):
    try:
        for _ in range(3):
            try:
                mail_server.send_message(message, to_email)
                return
            except:
                mail_server_init()
    except:
        pass


def _send_email(subject, content, to_email, content_subtype=None):
    message = make_email_message(subject, content, to_email, content_subtype)
    send_email_message(message, to_email)


def send_email(*args):
    threading.Thread(target=_send_email, args=args).start()
    

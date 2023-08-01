import secrets
from resources.mail import *


def get_verification_code():
    return '123456'
    length = 6
    mx = 10**length
    mn = 10**(length-1)
    return str(secrets.randbelow(mx-mn-1)+mn)

# -----------------------------------------------------------------------------------------

def get_verification_code_as_html_content(code):
    return f'<h1> Your verification Code: {code} </h1>'


def send_verification_code_email_message(code, to_email):
    send_email(
            'Afia Verification Code', 
            get_verification_code_as_html_content(code), 
            to_email, 
            'html'
        )


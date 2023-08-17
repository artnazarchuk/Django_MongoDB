import time
import smtplib
from ServiceAPI.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from email.message import EmailMessage
from celery import shared_task

@shared_task()
def add(x, y):
    print(x + y)
    return x + y


@shared_task()
def add2(x, y):
    print(x + y)
    time.sleep(5)
    return x + y

def get_email_customer_create(email_customer: str, username: str):
    email = EmailMessage()
    email['Subject'] = 'Заявка в обработке'
    email['From'] = EMAIL_HOST_USER
    email['To'] = email_customer

    email.set_content(
        '<div>'
        f'<h1 style="color: green;">Здравствуйте {username}, ваша заявка в обработке 😊</h1>'
        '</div>',
        subtype='html'
    )
    return email

@shared_task()
def send_email_customer_create(email_customer: str, username: str):
    email = get_email_customer_create(email_customer, username)
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(email)

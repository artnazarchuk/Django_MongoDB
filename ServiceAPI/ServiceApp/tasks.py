import time
# send email without Django
import smtplib
from ServiceAPI.settings import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
# from email.message import EmailMessage
# send email with Django
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from celery import shared_task

@shared_task()
def add(x, y):
    print(x + y)
    return x + y


@shared_task()
def add2(x, y):
    print(x + y)
    time.sleep(3)
    return x + y

# send email without Django
def get_email_customer_create(email_customer: str, username: str):
    from email.message import EmailMessage
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
    # send email without Django
    time.sleep(5)
    email = get_email_customer_create(email_customer, username)
    with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT) as server:
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.send_message(email)
        return "Почта отправлена"

@shared_task()
def send_email_customer_create1(email_customer: str, username: str):
    # send email with Django
    time.sleep(10)
    send_mail(
        'Ваша заявка в обработке',
        f'Здравствуйте {username}, ваша заявка в обработке 😊',
        'settings.EMAIL_HOST_USER',
        [email_customer],
        fail_silently=False
    )
    return "Почта отправлена"

@shared_task()
def send_email_customer_create2(email_customer: str, username: str):
    # send email with Django
    time.sleep(15)
    email = EmailMessage(
        'Ваша заявка в обработке',
        f'Здравствуйте {username}, ваша заявка в обработке 😊',
        'settings.EMAIL_HOST_USER',
        [email_customer]
    )
    email.send(fail_silently=False)
    return "Почта отправлена"

@shared_task()
def send_email_customer_create3(email_customer: str, username: str):
    # send email with Django
    time.sleep(20)
    subject = 'Ваша заявка в обработке'
    from_email = 'settings.EMAIL_HOST_USER'
    html_content = f'<h1 style="color: green;">Здравствуйте {username}, ваша заявка в обработке 😊</h1>'
    msg = EmailMessage(subject, html_content, from_email, [email_customer])
    msg.content_subtype = "html"
    msg.send()
    return "Почта отправлена"

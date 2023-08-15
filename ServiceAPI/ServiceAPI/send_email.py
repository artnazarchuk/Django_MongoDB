import smtplib
from email.message import EmailMessage

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465
SMTP_USER = 'devselit@gmail.com'
SMTP_PASSWORD = 'rdbzkrrbphmunqpq'

def get_email_template_dashboard():
    email = EmailMessage()
    email['Subject'] = 'Заявка в обработке'
    email['From'] = SMTP_USER
    email['To'] = 'sel_it@tut.by'

    email.set_content(
        '<div>'
        '<h1 style="color: red;">Здравствуйте, ваша заявка в обработке 😊</h1>'
        '</div>',
        subtype='html'
    )
    return email

def send_email_report_dashboard():
    email = get_email_template_dashboard()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)

send_email_report_dashboard()


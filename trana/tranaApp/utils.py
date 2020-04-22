import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from .email_credentials import email, pwd


def send_mail(email_id, details, medicine):
    me = email
    my_password = pwd
    you = email_id

    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Alert"
    msg["From"] = me
    msg["To"] = you

    html = "<html><body><p>Hi, I have the following alerts for you!</p> The medicine {} you requested is available at the pharmacy {} located in {}.</body></html>".format(
        medicine, details[0], details[1]
    )
    part2 = MIMEText(html, "html")

    msg.attach(part2)

    s = smtplib.SMTP_SSL("smtp.gmail.com")
    s.login(me, my_password)

    s.sendmail(me, you, msg.as_string())
    s.quit()

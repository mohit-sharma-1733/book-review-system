from pydantic import EmailStr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def send_email(email: EmailStr, message: str):
    
    smtp_host = 'smtp.eastvantage.com'
    smtp_port = 587
    smtp_user = 'username'
    smtp_password = 'password'
    sender_email = 'noreply@eastvantage.com'

    # Create a MIME multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = 'Review Published'
    msg.attach(MIMEText(message, 'plain'))
    with smtplib.SMTP(smtp_host, smtp_port) as server:
        server.starttls() 
        server.login(smtp_user, smtp_password)
        text = msg.as_string()
        server.sendmail(sender_email, email, text)
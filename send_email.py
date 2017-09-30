import email
from email.mime.text import MIMEText
import smtplib

def send_email(email,height):
    #Enter the fromEmail Address
    from_email="fromemailid@email.com"
    #Password of the from Email Address
    from_password="Password"
    to_email=email;
    subject="Height Data"
    message="Hey, your height is <strong>%s</strong>"%height
    msg=MIMEText(message,'html')
    msg['Subject']=subject
    msg['To']=to_email
    msg['From']=from_email

"""
Setup for the email from which it will be sent
"""
    gmail=smtplib.SMTP('smtp.gmail.com',587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)

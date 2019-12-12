import smtplib
import os
email_username=os.environ.get('EMAIL_USERNAME')
email_password=os.environ.get('EMAIL_PASSWORD')
with smtplib.SMTP('smtp.gmail.com',587)as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(email_username,email_password)
    subject="Hello from Python"
    body="Lorem Ipsum"
    msg=f'Subject:{subject}\n\n{body}'
    smtp.sendmail(email_username,'prajapatitejendra94@gmail.com',msg)

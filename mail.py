import os
import smtplib

EMAIL_USERNAME=os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')
print(EMAIL_USERNAME)

# for Testing purpose use localhost instead of gmail -- >  python -m smtpd -c DebuggingServer -n localhost:1025
# with smtplib.SMTP('localhost',1025) as smtp:
with smtplib.SMTP('smtp.gmail.com',587) as smtp:

    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()


    smtp.login(EMAIL_USERNAME,EMAIL_PASSWORD)

    subject = 'MAIL FROM PYTHON'
    body= 'THIS IS TEST MESSAGE...'

    msg= f'Subject: {subject} \n\n{body}'
    smtp.sendmail(EMAIL_USERNAME,'samiksha.khule94@gmail.com',msg)

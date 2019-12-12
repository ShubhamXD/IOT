import os
import smtplib
import imghdr
from email.message import EmailMessage
EMAIL_USERNAME=os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')
print(EMAIL_USERNAME)

msg= EmailMessage()
msg['Subject']='Hi from Python'
msg['From']='pooja.agrawal2308@gmail.com'
msg['To']='shubhamsharma6618@live.co.uk'
msg.set_content('THIS IS TEST CONTENT FROM PYTHON APP')
print(msg)

with open('a.jpg','rb') as f:
    file_data=f.read()
    file_type=imghdr.what(f.name)
    print(file_type)
    file_name=f.name
msg.add_attachment(file_data , maintype='image', subtype=file_type ,
                    filename=file_name)
# for Testing purpose use localhost instead of gmail -- >  python -m smtpd -c DebuggingServer -n localhost:1025
# with smtplib.SMTP('localhost',1025) as smtp:
with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp:

    smtp.login(EMAIL_USERNAME,EMAIL_PASSWORD)

    smtp.send_message(msg)

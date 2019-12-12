import os
import imaplib
from email.message import EmailMessage
import email
import time
EMAIL_USERNAME=os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD') # vzknmebxljupjdwj
msg= EmailMessage()
mail= imaplib.IMAP4_SSL('imap.gmail.com',993)
mail.login(EMAIL_USERNAME,EMAIL_PASSWORD)


mail.select('inbox')
result,data = mail.uid('search',None,'ALL')
latest_email_id=data[0].split()[-1]
print(latest_email_id)
result,data=mail.uid('fetch',latest_email_id,'(RFC822)')
raw_mail=data[0][1]
email_msg=email.message_from_bytes(raw_mail)
print(email_msg['Subject']) # return subject of recieved mail

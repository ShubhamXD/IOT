import os
import smtplib
import imaplib
from email.message import EmailMessage
import email
import pprint
import time
import requests
from time import sleep
import RPi.GPIO as GPIO

EMAIL_USERNAME=os.environ.get('EMAIL_USERNAME')
EMAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD') # vzknmebxljupjdwj

motor=21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(motor,GPIO.OUT)

def deleteEmailIMAP(mail,uuid):
    #mail.uid('STORE', uuid,'+FLAGS','(\\Deleted)')
    mail.uid('STORE', uuid,'+X-GM-LABELS','(\\Trash)')
    print(mail.expunge())

    
    




msg= EmailMessage()

mail= imaplib.IMAP4_SSL('imap.gmail.com',993)
mail.login(EMAIL_USERNAME,EMAIL_PASSWORD)
mail.select('inbox')
# type,data = imap.search(None,'ALL')
# mail_ids = data[0]
# id_list = mail_ids.split()
# latest_email_id=id_list[-1]
# first_mail_id=int(id_list[0])
subject='motorON'
email_id_processed=0
motorStatus='Motor is Stopped....'
while True:
    print(motorStatus)
    time.sleep(5)
    result,data = mail.uid('search',None,'ALL')
    latest_email_id=data[0].split()[-1]
    # tmp , data =imap.fetch(latest_email_id ,'(RFC822)')
    tmp , data =mail.uid('fetch',latest_email_id ,'(RFC822)')
    raw_email=data[0][1]
    email_message=email.message_from_bytes(raw_email)
    #print(email_message['From'])
    #print(email_message['Subject'])
    if latest_email_id != email_id_processed:
        email_id_processed=latest_email_id
        if email_message['Subject']== 'motorON':
            print('Motor Run Command is Received....')
            deleteEmailIMAP(mail,latest_email_id)
            motorStatus='Motor is Runing....'
            GPIO.output(motor,1)
        elif email_message['Subject']== 'motorOFF':
            print('Motor Stop command is Received....')
            deleteEmailIMAP(mail,latest_email_id)
            GPIO.output(motor,0) 
            motorStatus='Motor is Stopped....'
    



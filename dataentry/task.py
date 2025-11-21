import time

from django.contrib.messages.context_processors import messages

from awd_main.celery import app

from django.core.management import call_command #Esto llama a los comandos de django
from django.core.mail import EmailMessage

from awd_main.settings import DEFAULT_FROM_EMAIL
from .utils import send_email_notifications


@app.task
def celery_test_task():
    time.sleep(5)
    # send an email
    mail_subject = 'Test subject'
    message = 'This is a test email'
    to_email = "superen2000@yahoo.es"
    send_email_notifications(mail_subject, message, to_email)
    return 'Email send successfuly'

@app.task
def import_data_task(file_path, model_name):
    try:
        call_command('importdata', file_path, model_name)
    except Exception as e:
        raise e
    # notify the user by email
    mail_subject = 'Import Data Complete'
    message = ' Your data import has been successful'
    to_email = DEFAULT_FROM_EMAIL
    send_email_notifications(mail_subject, message, to_email)
    return 'Data imported successfully!'
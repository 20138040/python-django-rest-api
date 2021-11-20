from celery import shared_task
from .models import TodoTask
from .serializers import TodoTaskSerializer
from datetime import datetime, timedelta, time
import pytz
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(task):

    sender = 'devwanshikrish@gmail.com'
    reciever = task["email"]

    body = ""
    body += "Dear User,\n"
    body += "\nPlease find below the details of the task which you want the reminder. \n\n"
    body += "\n Task Name : {}. \n".format(task["task_name"])
    body += "\n Task Description : {}. \n".format(task["task_description"])
    body += "\nThanks,\n"
    body += "Krishna."
    msg_body = MIMEText(body, "plain")
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Task Reminder"
    msg["From"] = sender
    msg["To"] = reciever

    msg.attach(msg_body)

    with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
        server.login("2b5953c5f4b885", "3423266593c5b8")
        server.sendmail(sender, reciever, msg.as_string())

    # smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # smtpObj.ehlo()
    # smtpObj.login(gmail_user, gmail_password)
    # smtpObj.sendmail(sender, reciever, msg)
    # smtpObj.close()


    # try:
    #     smtpObj = smtplib.SMTP('localhost')
    #     smtpObj.sendmail(sender, reciever, msg)
    #     print("Successfully sent email to {}".format(reciever))
    # except Exception:
    #     print("Error: unable to send email")



@shared_task
def hello():
    tasks = TodoTask.objects.all()
    serializer = TodoTaskSerializer(tasks, many=True)
    tasks = serializer.data

    for task in tasks:
        reminder_date = datetime.strptime(task["reminder_date"],"%Y-%m-%dT%H:%M:%S%z")
        datetime_india = datetime.now(pytz.timezone('Asia/Kolkata'))
        date = datetime_india
        prev = date - timedelta(minutes=30)

        print(reminder_date)
        print(date)
        print(prev)

        if date.date() == reminder_date.date() and (reminder_date.time() >= prev.time() and reminder_date.time() <= date.time()):
            print("this task needs to be reminded")
            send_mail(task)

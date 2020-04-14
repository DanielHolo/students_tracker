import pytz
from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime, timedelta

from students.models import Student, Logger


@shared_task
def send_mail_async(subject, message, recipient_list, student_id):
    student_obj = Student.objects.get(id=student_id)
    send_mail(subject, message,
              student_obj.email,
              recipient_list, fail_silently=False)


@shared_task
def send_confirmation_mail(mail_subject, message, to_email, recipient_list):
    send_mail(mail_subject, message, to_email, recipient_list)


@shared_task
def delete_old_objects():
    Logger.objects.filter(created__lte=datetime.now(pytz.utc) - timedelta(days=7)).delete()

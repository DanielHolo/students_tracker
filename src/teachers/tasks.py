from celery import shared_task
from django.core.mail import send_mail

from teachers.models import Teacher


# @shared_task
# def send_mail_async(subject, message, email_from, recipient_list):
#     send_mail(subject, message, email_from, recipient_list, fail_silently=False)


@shared_task
def send_mail_async(subject, message, recipient_list, student_id):
    student_obj = Teacher.objects.get(id=student_id)
    send_mail(subject, message,
              student_obj.email,
              recipient_list, fail_silently=False)

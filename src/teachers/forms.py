from django.forms import Form, ModelForm, EmailField, CharField
from django.core.mail import send_mail
from django.conf import settings
from teachers.models import Teacher
import logging


class TeachersAddForm(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        messege = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, messege, email_from, recipient_list, fail_silently=False)

        logging.basicConfig(filename="Logs.log",
                            level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s:%(message)s')
        logging.info(f"App - TEACHER, subject - {subject}, email - {email_from}")

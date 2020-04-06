from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm, EmailField, CharField
from django.core.mail import send_mail
from django.conf import settings
from students.models import Student
import logging


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(ModelForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'group')

    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        email_exists = Student.objects \
            .filter(email__iexact=email) \
            .exclude(email__iexact=self.instance.email)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]
        send_mail(subject, message, email_from, recipient_list, fail_silently=False)

        logging.basicConfig(filename="Logs.log",
                            level=logging.DEBUG,
                            format='%(asctime)s %(levelname)s:%(message)s')
        logging.info(f"App - STUDENT,subject - {subject}, email - {email_from}")

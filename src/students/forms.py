from django.forms import Form, ModelForm, EmailField, CharField
from django.core.mail import send_mail
from django.conf import settings
from students.models import Student


class StudentsAddForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class ContactForm(Form):
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

from django.forms import Form, ModelForm, EmailField, CharField
from django.conf import settings
from teachers.models import Teacher
import logging
from django.core.exceptions import ValidationError
from teachers.tasks import send_mail_async


class TeacherForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        email_exists = Teacher.objects \
            .filter(email__iexact=email) \
            .exclude(email__iexact=self.instance.email)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']

        telephone_exists = Teacher.objects \
            .filter(telephone__iexact=telephone) \
            .exclude(telephone__iexact=self.instance.telephone)

        if telephone_exists.exists():
            raise ValidationError(f'{telephone} is already used!')

        if not telephone.isdigit():
            raise ValidationError(f'{telephone} contains not only numbers')
        return telephone


class TeachersAddForm(TeacherForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class TeacherAdminForm(TeacherForm):
    class Meta:
        model = Teacher
        fields = ('id', 'email', 'first_name', 'last_name', 'telephone')


class TeacherContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    logging.basicConfig(filename="Logs.log",
                        format='%(asctime)s %(levelname)s:%(message)s')

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]

        student = Teacher.objects.get_or_create(email=email_from)[0]
        send_mail_async.delay(subject, message, student.id, recipient_list)

        logging.info(f"App - TEACHER, subject - {subject}, email - {email_from}")

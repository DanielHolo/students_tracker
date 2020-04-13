from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm, EmailField, CharField
from django.conf import settings
from students.models import Student
from students.tasks import send_mail_async
import logging
from django.contrib.auth.models import User


class StudentForm(ModelForm):
    def clean_email(self):
        email = self.cleaned_data['email'].lower()

        email_exists = Student.objects \
            .filter(email__iexact=email) \
            .exclude(email__iexact=self.instance.email)
        if email_exists.exists():
            raise ValidationError(f'{email} is already used!')
        return email

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']

        telephone_exists = Student.objects \
            .filter(telephone__iexact=telephone) \
            .exclude(telephone__iexact=self.instance.telephone)

        if telephone_exists.exists():
            raise ValidationError(f'{telephone} is already used!')

        if not telephone.isdigit():
            raise ValidationError(f'{telephone} contains not only numbers')
        return telephone


class StudentsAddForm(StudentForm):
    class Meta:
        model = Student
        fields = '__all__'


class StudentAdminForm(StudentForm):
    class Meta:
        model = Student
        fields = ('id', 'email', 'first_name', 'last_name', 'group', 'telephone')


class ContactForm(Form):
    email = EmailField()
    subject = CharField()
    text = CharField()

    logging.basicConfig(filename="Logs.log",
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s')

    def save(self):
        data = self.cleaned_data
        subject = data['subject']
        message = data['text']
        email_from = data['email']
        recipient_list = [settings.EMAIL_HOST_USER, ]

        student = Student.objects.get_or_create(email=email_from)[0]
        # student = Student.objects.create(email=email_from)
        send_mail_async.delay(subject, message, recipient_list, student.id)

        logging.info(f"App - STUDENT,subject - {subject}, email - {email_from}")


class UserRegistrationForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.set_password(self.cleaned_data['password'])
        super().save(commit)


class UserLoginForm(Form):
    username = CharField()
    password = CharField()


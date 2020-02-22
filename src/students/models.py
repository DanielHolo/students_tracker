from datetime import datetime
from faker import Faker

from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True, default=None)
    email = models.EmailField()
    telephone = models.CharField(max_length=255)
    address = models.CharField(max_length=255, null=True, blank=True)
    group = models.ForeignKey('groups.Group', null=True, blank=True, on_delete=models.CASCADE)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} '

    @classmethod
    def generate_student(cls):
        fake = Faker()
        student = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=datetime.now().date(),
                      email=fake.email(),
                      telephone=fake.phone_number(),
                      )
        student.save()
        return student

from datetime import datetime
from faker import Faker

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    birth_date = models.DateField(null=True, blank=True, default=None)
    email = models.EmailField()
    # add avatar TODO
    telephone = models.CharField(max_length=255)  # clean phone TODO
    address = models.CharField(max_length=255, null=True, blank=True)

    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.birth_date} '

    @classmethod
    def generate_teacher(cls):
        fake = Faker()
        teacher = cls(first_name=fake.first_name(),
                      last_name=fake.last_name(),
                      birth_date=datetime.now().date(),
                      email=fake.email(),
                      telephone=fake.phone_number(),
                      )
        teacher.save()
        return teacher

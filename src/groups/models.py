from datetime import datetime
from faker import Faker

from django.db import models



class Group(models.Model):
    group_name = models.CharField(max_length=20)
    group_size = models.CharField(max_length=20)
    group_creation_date = models.DateField()
    group_email = models.EmailField()
    group_telephone = models.CharField(max_length=16)  # clean phone TODO


    def get_info(self):
        return f'{self.first_name} {self.last_name} {self.birth_date} '

    @classmethod
    def generate_group(cls):
        fake = Faker()
        student = cls(group_name=fake.random_digit(),
                      group_size=fake.random_digit(),
                      group_creation_date=datetime.now().date(),
                      group_email=fake.email(),
                      group_telephone=fake.phone_number(),
                      )
        student.save()
        return student

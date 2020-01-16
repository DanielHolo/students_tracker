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
        return f'{self.group_name} {self.group_size} {self.group_email} '

    @classmethod
    def generate_group(cls):
        fake = Faker()
        group = cls(group_name=fake.word(),
                    group_size=fake.random_int(10,30),
                    group_creation_date=datetime.now().date(),
                    group_email=fake.email(),
                    group_telephone=fake.phone_number(),
                    )
        group.save()
        return group

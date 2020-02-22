from datetime import datetime
from faker import Faker

from django.db import models


class Group(models.Model):
    group_name = models.CharField(max_length=20)
    group_size = models.CharField(max_length=20)
    group_creation_date = models.DateField(null=True, blank=True, default=None)
    group_email = models.EmailField()
    group_telephone = models.CharField(max_length=255)
    curator = models.OneToOneField('teachers.Teacher', null=True, blank=True, on_delete=models.CASCADE)
    head = models.OneToOneField('students.Student', related_name='student_head',
                                null=True, blank=True, on_delete=models.CASCADE)

    def get_info(self):
        return f'{self.group_name} {self.group_size} {self.group_email} '

    def __str__(self):
        return f'{self.id} {self.group_name}'

    @classmethod
    def generate_group(cls):
        fake = Faker()
        group = cls(group_name=fake.word(),
                    group_size=fake.random_int(10, 30),
                    group_creation_date=datetime.now().date(),
                    group_email=fake.email(),
                    group_telephone=fake.phone_number(),
                    )
        group.save()
        return group

from django.core.management.base import BaseCommand, CommandError
from students.models import Student
from groups.models import Group
import random


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete'
        )

    def handle(self, *args, **options):
        # Group.objects.all().delete()
        # Student.objects.all().delete()
        groups = [Group.objects.create(group_name=f'name_{i}') for i in range(10)]
        number = int(options.get('number') or 100)
        for _ in range(100):
            student = Student.generate_student()
            student.group = random.choice(groups)
            student.save()
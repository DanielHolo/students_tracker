from django.core.management.base import BaseCommand, CommandError
from students.models import Student
from groups.models import Group
from teachers.models import Teacher
import random


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete'
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        students = Student.objects.all()
        teachers = Teacher.objects.all()
        groups = Group.objects.all()
        for group in groups:
            group.curator = random.choice(teachers)
            group.head = random.choice(students)
            group.save()

from django.core.management.base import BaseCommand, CommandError
from groups.models import Group


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        parser.add_argument(
            '--number',
            help='Delete'
        )

    def handle(self, *args, **options):
        number = int(options.get('number') or 100)
        for _ in range(100):
            Group.generate_group()

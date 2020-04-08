from django.apps import AppConfig


class TeachersConfig(AppConfig):
    name = 'teachers'

    def ready(self):
        from teachers.signals import *

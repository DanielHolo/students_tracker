from django.db.models.signals import pre_save
from django.dispatch import receiver
from teachers.models import Teacher


@receiver(pre_save, sender=Teacher)
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()

    if instance.id is None:
        print('Object is created')

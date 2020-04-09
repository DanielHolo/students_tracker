from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from students.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(sender, instance, **kwargs):
    instance.email = instance.email.lower()
    instance.first_name = instance.first_name.capitalize()
    instance.last_name = instance.last_name.capitalize()

    if instance.id is None:
        print('Object is created')


@receiver(post_save, sender=Student)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)
        instance.profile.save()

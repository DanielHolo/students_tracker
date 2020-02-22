# Generated by Django 2.2.9 on 2020-02-22 13:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0002_auto_20200222_1205'),
        ('students', '0006_auto_20200219_2007'),
        ('groups', '0006_group_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='teacher',
        ),
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='teachers.Teacher'),
        ),
        migrations.AddField(
            model_name='group',
            name='head',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='student_head', to='students.Student'),
        ),
    ]
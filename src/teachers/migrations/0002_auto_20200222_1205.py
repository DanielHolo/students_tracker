# Generated by Django 2.2.9 on 2020-02-22 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='birth_date',
            field=models.DateField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='telephone',
            field=models.CharField(max_length=255),
        ),
    ]

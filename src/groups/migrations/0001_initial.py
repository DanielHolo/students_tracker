# Generated by Django 2.2.9 on 2020-01-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=20)),
                ('group_size', models.CharField(max_length=20)),
                ('group_creation_date', models.DateField()),
                ('group_email', models.EmailField(max_length=254)),
                ('group_telephone', models.CharField(max_length=16)),
            ],
        ),
    ]
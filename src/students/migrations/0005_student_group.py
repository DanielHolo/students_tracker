# Generated by Django 2.2.9 on 2020-02-19 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_auto_20200115_1648'),
        ('students', '0004_auto_20200219_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='groups.Group'),
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-27 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_vehicle_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='display_picture',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='picture',
        ),
    ]

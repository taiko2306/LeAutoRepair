# Generated by Django 3.0.6 on 2020-05-24 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200524_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(blank=True, default='vehicle_image/placeholder.png', null=True, upload_to='vehicle_image'),
        ),
    ]

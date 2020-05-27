# Generated by Django 3.0.6 on 2020-05-26 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=30)),
                ('lname', models.CharField(max_length=30)),
                ('title', models.CharField(max_length=30)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('display_picture', models.FileField(upload_to='')),
            ],
        ),
    ]
# Generated by Django 3.0.6 on 2020-05-25 18:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20200524_1909'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.TextField(blank=True, max_length=180, null=True)),
                ('Odometer', models.IntegerField()),
                ('serviced_by', models.CharField(max_length=30)),
                ('serviced_date', models.DateField(default=datetime.datetime.now)),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Vehicle')),
            ],
        ),
    ]

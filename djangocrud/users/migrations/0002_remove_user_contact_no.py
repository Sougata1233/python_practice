# Generated by Django 2.1.2 on 2018-11-19 11:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='contact_no',
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-08 06:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todo_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todo',
            options={'permissions': [('change_priority', 'Can change priority of a task')]},
        ),
    ]

# Generated by Django 3.1.5 on 2021-02-03 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='quesion',
            new_name='question',
        ),
    ]

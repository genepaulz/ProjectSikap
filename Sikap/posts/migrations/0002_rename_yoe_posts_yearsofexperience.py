# Generated by Django 3.2 on 2021-05-03 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='YoE',
            new_name='yearsOfExperience',
        ),
    ]
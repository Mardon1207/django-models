# Generated by Django 4.2.6 on 2023-10-19 06:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='frst',
            new_name='first',
        ),
    ]
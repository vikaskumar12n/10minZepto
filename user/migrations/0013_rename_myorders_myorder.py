# Generated by Django 3.2.4 on 2023-09-21 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_auto_20230921_1710'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='myorders',
            new_name='myorder',
        ),
    ]

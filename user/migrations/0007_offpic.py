# Generated by Django 3.2.4 on 2023-09-15 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='offpic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ofpic', models.ImageField(null=True, upload_to='static/offerpic/')),
            ],
        ),
    ]

# Generated by Django 3.0.8 on 2020-07-07 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='note',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

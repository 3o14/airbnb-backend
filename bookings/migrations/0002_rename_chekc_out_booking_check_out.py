# Generated by Django 4.1.3 on 2022-12-29 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='chekc_out',
            new_name='check_out',
        ),
    ]

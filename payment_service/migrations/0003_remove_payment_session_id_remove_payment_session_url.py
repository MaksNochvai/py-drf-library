# Generated by Django 4.0.4 on 2023-08-17 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment_service', '0002_alter_payment_status_alter_payment_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='session_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='session_url',
        ),
    ]
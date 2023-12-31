# Generated by Django 4.0.4 on 2023-08-17 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payment_service", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="status",
            field=models.CharField(
                choices=[("Pending", "PENDING"), ("Paid", "PAID")], max_length=255
            ),
        ),
        migrations.AlterField(
            model_name="payment",
            name="type",
            field=models.CharField(
                choices=[("Payment", "PAYMENT"), ("Fine", "FINE")], max_length=255
            ),
        ),
    ]

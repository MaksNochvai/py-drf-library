# Generated by Django 4.0.4 on 2023-08-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('borrowings_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('PAID', 'PAID')], max_length=255)),
                ('type', models.CharField(choices=[('PAYMENT', 'PAYMENT'), ('FINE', 'FINE')], max_length=255)),
                ('session_url', models.URLField()),
                ('session_id', models.CharField(max_length=50)),
                ('money_to_pay', models.DecimalField(decimal_places=2, max_digits=10)),
                ('borrowing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='borrowings_service.borrowing')),
            ],
        ),
    ]
from enum import Enum

from django.db import models


class PaymentStatus(Enum):
    PENDING = 'PENDING', 'Pending'
    PAID = 'PAID', 'Paid'


class PaymentType(Enum):
    PAYMENT = 'PAYMENT', 'Payment'
    FINE = 'FINE', 'Fine'


class Payment(models.Model):
    status = models.CharField(max_length=255, choices=[(status.value, status.name) for status in PaymentStatus])
    type = models.CharField(max_length=255, choices=[(type.value, type.name) for type in PaymentType])
    borrowing_id = models.IntegerField()
    session_url = models.URLField()
    session_id = models.CharField(max_length=50)
    money_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment #{self.id} - {self.status} - {self.type}"

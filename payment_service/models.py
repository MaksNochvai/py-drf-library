from enum import Enum

from django.db import models

from borrowings_service.models import Borrowing


class PaymentStatus(Enum):
    PENDING = "Pending"
    PAID = "Paid"


class PaymentType(Enum):
    PAYMENT = "Payment"
    FINE = "Fine"


class Payment(models.Model):
    status = models.CharField(
        max_length=255,
        choices=[(status.value, status.name) for status in PaymentStatus],
    )
    type = models.CharField(
        max_length=255, choices=[(type.value, type.name) for type in PaymentType]
    )
    borrowing_id = models.ForeignKey(Borrowing, on_delete=models.CASCADE)
    session_url = models.URLField(blank=True, null=True)
    session_id = models.CharField(max_length=50, blank=True, null=True)
    money_to_pay = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Payment #{self.id} - {self.status} - {self.type}"

from django.db import models
from enum import Enum


class CoverType(Enum):
    HARD = 'Hardcover'
    SOFT = 'Softcover'


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    cover = models.CharField(max_length=10, choices=[(cover.value, cover.name) for cover in CoverType])
    inventory = models.PositiveIntegerField()
    daily_fee = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

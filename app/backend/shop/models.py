from django.db import models
from city.models import Street

class Shop(models.Model):
    name = models.CharField(max_length=200)
    street = models.ForeignKey(
        Street, 
        on_delete=models.CASCADE,
        related_name='street', 
        verbose_name=('Street'),
    )
    house = models.IntegerField(
        verbose_name=('House'),
    )
    opening_time = models.TimeField(
        verbose_name=('Opening time'),
    )
    closing_time = models.TimeField(
        verbose_name=('Closing time'),
    )

from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)


class Street(models.Model):
    name = models.CharField(max_length=200)
    city = models.ForeignKey(
        City, on_delete=models.CASCADE,
    )

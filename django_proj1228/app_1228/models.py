from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description1 = models.TextField(max_length=255)


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.SmallIntegerField()


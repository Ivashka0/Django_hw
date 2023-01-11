from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=100, null=False)
    price = models.DecimalField(max_digits=20, decimal_places=2, null=False, validators=[MinValueValidator(0.00)])

    def __str__(self):
        return f"{self.name}"


class Customer(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    password = models.CharField(max_length=100, unique=False, null=False)

    def __str__(self):
        return f"{self.name}"
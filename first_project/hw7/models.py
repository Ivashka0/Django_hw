from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.name}, {self.price}'


class Departments(models.Model):
    building = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=0)
    financing = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.name}"


class Diseases(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    severity = models.PositiveIntegerField(validators=[MaxValueValidator(8), MinValueValidator(1)], default=0)

    def __str__(self):
        return f"{self.name}"


class Doctors(models.Model):
    name = models.CharField(max_length=30, null=False)
    phone = models.CharField(max_length=13, null=False)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    surname = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Examinations(models.Model):
    dayofweek = models.PositiveIntegerField(validators=[MaxValueValidator(7), MinValueValidator(1)], null=0, default=0)
    endtime = models.TimeField(null=False)
    name = models.CharField(max_length=30, null=False)
    starttime = models.TimeField(null=False)

    def __str__(self):
        return f"{self.name}, {self.dayofweek}"


class Wards(models.Model):
    building = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=0)
    floor = models.PositiveIntegerField(validators=[MaxValueValidator(3), MinValueValidator(1)], default=0)
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.name}"

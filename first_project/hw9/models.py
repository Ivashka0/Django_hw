from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, ValidationError
import datetime
import base64

# Create your models here.


class Department(models.Model):
    building = models.PositiveIntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=0)
    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self):
        return f"{self.name}"


class Doctor(models.Model):
    name = models.CharField(max_length=30, null=False)
    premium = models.DecimalField(max_digits=5, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    salary = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    surname = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Examination(models.Model):
    name = models.CharField(max_length=30, null=False)

    def __str__(self):
        return f"{self.name}"


class Ward(models.Model):
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    places = models.PositiveIntegerField(validators=[MinValueValidator(1)], null=False, default=0)
    name = models.CharField(max_length=20, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class DoctorsExamination(models.Model):
    start_time = models.TimeField(null=False)
    end_time = models.TimeField(null=False)
    doctor_id = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    examination_id = models.ForeignKey(Examination, on_delete=models.SET_NULL, null=True)
    ward_id = models.ForeignKey(Ward, on_delete=models.SET_NULL, null=True)

    def clean(self):
        if self.start_time > self.end_time:
            raise ValidationError("Error")

    def __str__(self):
        return f"{self.doctor_id} {self.examination_id} {self.ward_id}"


class Sponsor(models.Model):
    name = models.CharField(max_length=100, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)], default=0)
    date = models.DateField()
    department_id = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    sponsor_id = models.ForeignKey(Sponsor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.sponsor_id} {self.amount}"


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/")
    image_base64 = models.CharField(max_length=100000, blank=True)

    def save(self, *args, **kwargs):
        self.image_base64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.price}"

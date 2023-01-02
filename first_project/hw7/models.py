from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
import base64

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="images/", blank=True)
    image_base64 = models.CharField(max_length=100000, blank=True)

    def save(self, *args, **kwargs):
        self.image_base64 = base64.b64encode(self.image.read()).decode('utf-8')
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name}, {self.price}'

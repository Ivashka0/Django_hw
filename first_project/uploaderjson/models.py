from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator, ValidationError

# Create your models here.


class Product(models.Model):
    MatchNumber = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=False, default=0)
    RoundNumber = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=False, default=0)
    DateUtc = models.DateTimeField()
    Location = models.CharField(max_length=1000, null=False)
    HomeTeam = models.CharField(max_length=1000, null=False)
    AwayTeam = models.CharField(max_length=1000, null=False)
    Group = models.CharField(max_length=1000, null=True)
    HomeTeamScore = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=True)
    AwayTeamScore = models.PositiveIntegerField(validators=[MinValueValidator(0)], null=True)

    def __str__(self):
        return f"{self.HomeTeam} - {self.AwayTeam}"

# Generated by Django 4.1.3 on 2023-01-10 18:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('MatchNumber', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('RoundNumber', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('DateUtc', models.DateTimeField()),
                ('Location', models.CharField(max_length=1000)),
                ('HomeTeam', models.CharField(max_length=1000)),
                ('AwayTeam', models.CharField(max_length=1000)),
                ('Group', models.CharField(max_length=1000)),
                ('HomeTeamScore', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('AwayTeamScore', models.PositiveIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
            ],
        ),
    ]

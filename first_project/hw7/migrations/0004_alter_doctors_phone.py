# Generated by Django 4.1.3 on 2022-12-27 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hw7', '0003_wards'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='phone',
            field=models.CharField(max_length=13),
        ),
    ]
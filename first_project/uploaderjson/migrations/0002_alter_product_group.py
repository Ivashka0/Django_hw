# Generated by Django 4.1.3 on 2023-01-10 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploaderjson', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Group',
            field=models.CharField(default='null', max_length=1000),
        ),
    ]

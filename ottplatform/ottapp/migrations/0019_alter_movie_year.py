# Generated by Django 5.0.1 on 2024-01-10 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0018_remove_upcoming_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='year',
            field=models.CharField(max_length=100),
        ),
    ]

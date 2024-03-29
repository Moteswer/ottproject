# Generated by Django 5.0.1 on 2024-01-09 05:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0009_alter_movie_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='customer_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='ottapp.customerprofile'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='avatar',
            field=models.ImageField(upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='kidprofile',
            name='avatar',
            field=models.ImageField(upload_to='media/'),
        ),
    ]

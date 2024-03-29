# Generated by Django 5.0.1 on 2024-01-12 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ottapp', '0022_moviekid_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='upcomingkid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('Duration', models.CharField(default='', max_length=50)),
                ('Genre', models.CharField(default='', max_length=100)),
                ('Director', models.CharField(default='', max_length=100)),
                ('year', models.PositiveIntegerField()),
                ('desc', models.TextField(default='')),
                ('link', models.URLField(default='')),
                ('image', models.ImageField(default='', upload_to='media/')),
            ],
        ),
    ]

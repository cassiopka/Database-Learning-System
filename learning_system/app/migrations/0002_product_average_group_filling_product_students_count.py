# Generated by Django 5.0.2 on 2024-03-03 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='average_group_filling',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='students_count',
            field=models.IntegerField(default=0),
        ),
    ]

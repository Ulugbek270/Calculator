# Generated by Django 5.0.4 on 2024-04-20 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0002_alter_calculator_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calculator',
            name='value',
            field=models.IntegerField(max_length=10),
        ),
    ]

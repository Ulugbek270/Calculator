# Generated by Django 5.0.4 on 2024-04-20 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0007_rename_values_calculator_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculator',
            name='result',
        ),
    ]

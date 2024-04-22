# Generated by Django 5.0.4 on 2024-04-20 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_alter_calculator_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='calculator',
            name='result',
            field=models.DecimalField(decimal_places=10, default=0, max_digits=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='calculator',
            name='value',
            field=models.IntegerField(),
        ),
    ]
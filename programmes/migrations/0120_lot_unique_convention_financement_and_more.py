# Generated by Django 5.1.3 on 2024-12-13 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conventions", "0100_auto_20241213_1554"),
        ("programmes", "0119_fill_lot_convention"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="lot",
            constraint=models.UniqueConstraint(
                fields=("convention_id", "financement"),
                name="unique_convention_financement",
            ),
        ),
        migrations.AddConstraint(
            model_name="lot",
            constraint=models.UniqueConstraint(
                fields=("convention_id",), name="unique_convention"
            ),
        ),
    ]

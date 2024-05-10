# Generated by Django 4.2.10 on 2024-05-10 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conventions", "0001_initial_squashed_0083_convention_fichier_override_cerfa"),
    ]

    operations = [
        migrations.AlterField(
            model_name="convention",
            name="financement",
            field=models.CharField(
                choices=[
                    ("PLUS", "PLUS"),
                    ("PLUS_CD", "PLUS_CD"),
                    ("PLAI", "PLAI"),
                    ("PLAI_ADP", "PLAI_ADP"),
                    ("PLUS-PLAI", "PLUS-PLAI"),
                    ("PLS", "PLS"),
                    ("PSH", "PSH"),
                    ("PALULOS", "PALULOS"),
                    ("SANS_FINANCEMENT", "Sans Financement"),
                    ("LLS", "LLS"),
                    ("LLTS", "LLTS"),
                    ("LLTSA", "LLTSA"),
                    ("PLUS_DOM", "PLUS_DOM"),
                ],
                default="PLUS",
                max_length=25,
            ),
        ),
    ]

# Generated by Django 3.2.7 on 2021-09-20 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conventions", "0009_convention_statut"),
    ]

    operations = [
        migrations.AlterField(
            model_name="pret",
            name="preteur",
            field=models.CharField(
                choices=[
                    ("ETAT", "Etat"),
                    ("EPCI", "EPCI"),
                    ("REGION", "Région"),
                    ("CDCF", "CDC pour le foncier"),
                    ("CDCL", "CDC pour le logement"),
                    ("AUTRE", "Autre"),
                ],
                default="AUTRE",
                max_length=25,
            ),
        ),
    ]

# Generated by Django 4.2.10 on 2024-04-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conventions", "0081_convention_gestionnaire_bloc_info_complementaire"),
    ]

    operations = [
        migrations.AddField(
            model_name="convention",
            name="fichier_override_cerfa",
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.13 on 2022-06-27 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programmes", "0045_alter_typestationnement_typologie"),
    ]

    operations = [
        migrations.AddField(
            model_name="programme",
            name="code_insee_commune",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="programme",
            name="code_insee_departement",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="programme",
            name="code_insee_region",
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name="programme",
            name="nature_logement",
            field=models.CharField(
                choices=[
                    ("SANSOBJET", "Sans Objet"),
                    ("LOGEMENTSORDINAIRES", "Logements ordinaires"),
                    ("AUTRE", "Autres logements foyers"),
                    ("HEBERGEMENT", "Hébergement"),
                    ("RESISDENCESOCIALE", "Résidence sociale"),
                    ("PENSIONSDEFAMILLE", "Pensions de famille (Maisons relais)"),
                    ("RESIDENCEDACCUEIL", "Résidence d'accueil"),
                    ("RESIDENCEUNIVERSITAIRE", "Résidence universitaire"),
                    ("RHVS", "RHVS"),
                ],
                default="LOGEMENTSORDINAIRES",
                max_length=25,
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="type_operation",
            field=models.CharField(
                choices=[
                    ("SANSOBJET", "Sans Objet"),
                    ("NEUF", "Construction Neuve"),
                    ("VEFA", "Construction Neuve > VEFA"),
                    ("ACQUIS", "Acquisition"),
                    ("ACQUISAMELIORATION", "Acquisition-Amélioration"),
                    ("REHABILITATION", "Réhabilitation"),
                    ("ACQUISSANSTRAVAUX", "Acquisition sans travaux"),
                    ("SANSTRAVAUX", "Sans aide financière (sans travaux)"),
                    ("USUFRUIT", "Usufruit"),
                ],
                default="NEUF",
                max_length=25,
            ),
        ),
    ]

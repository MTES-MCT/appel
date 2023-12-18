# Generated by Django 3.2.11 on 2022-01-20 14:06


from django.db import migrations, models


def update_type_bailleur(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("bailleurs", "0007_auto_20220119_1059"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bailleur",
            name="type_bailleur",
            field=models.CharField(
                choices=[
                    ("ASSOCIATIONS", "Associations"),
                    ("COMMERCIALES", "entreprises commerciales"),
                    ("COMMUNE", "Commune"),
                    ("COOPERATIVE_HLM_SCIC", "Sté coopérative HLM /SCIC"),
                    ("CROUS", "CROUS"),
                    ("DEPARTEMENT", "Département"),
                    ("DRE_DDE_CETE_AC_PREF", "DRE,DDE,CETE,AC,Préfect."),
                    ("EPCI", "EPCI"),
                    ("ETC_PUBLIQUE_LOCAL", "Ets public local"),
                    ("ETS_HOSTIPATIERS_PRIVES", "Ets hospitaliers privés"),
                    ("FONDATION", "Fondation"),
                    ("FONDATION_HLM", "Fondation HLM"),
                    ("FRONCIERE_LOGEMENT", "Foncière Logement"),
                    ("GIP", "GIP"),
                    ("MUTUELLE", "Mutuelle"),
                    ("NONRENSEIGNE", "Non renseigné"),
                    ("OFFICE_PUBLIC_HLM", "Office public HLM (OPH)"),
                    ("PACT_ARIM", "Pact-Arim"),
                    ("PARTICULIERS", "Particuliers"),
                    ("SA_HLM_ESH", "SA HLM / ESH"),
                    ("SACI_CAP", "SACI CAP"),
                    ("SEM_EPL", "SEM / EPL"),
                    ("UES", "UES"),
                ],
                default="NONRENSEIGNE",
                max_length=25,
            ),
        ),
        migrations.RunPython(update_type_bailleur, migrations.RunPython.noop),
    ]

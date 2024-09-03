# Generated by Django 4.2.13 on 2024-09-03 18:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("instructeurs", "0001_initial_squashed_0017_auto_20230925_1209"),
        ("programmes", "0101_programme_reassign_command_old_admin_backup"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logement",
            name="coeficient",
            field=models.DecimalField(
                blank=True,
                decimal_places=4,
                max_digits=12,
                null=True,
                verbose_name="Coefficient propre au logement",
            ),
        ),
        migrations.AlterField(
            model_name="logement",
            name="loyer",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AlterField(
            model_name="logement",
            name="loyer_par_metre_carre",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=12,
                null=True,
                verbose_name="Loyer maximum en € par m² de surface utile",
            ),
        ),
        migrations.AlterField(
            model_name="logement",
            name="surface_annexes",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AlterField(
            model_name="logement",
            name="surface_annexes_retenue",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AlterField(
            model_name="logement",
            name="surface_corrigee",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=12,
                null=True,
                verbose_name="Surface corrigée",
            ),
        ),
        migrations.AlterField(
            model_name="logement",
            name="surface_habitable",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=12,
                null=True,
                verbose_name="Surface habitable",
            ),
        ),
        migrations.AlterField(
            model_name="logement",
            name="surface_utile",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=12,
                null=True,
                verbose_name="Surface utile",
            ),
        ),
        migrations.AlterField(
            model_name="logementedd",
            name="numero_lot",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="lot",
            name="edd_classique",
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name="lot",
            name="edd_volumetrique",
            field=models.TextField(blank=True, max_length=50000, null=True),
        ),
        migrations.AlterField(
            model_name="lot",
            name="loyer_derogatoire",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Loyer dérogatoire",
            ),
        ),
        migrations.AlterField(
            model_name="lot",
            name="nb_logements",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="lot",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="programmes.lot",
            ),
        ),
        migrations.AlterField(
            model_name="lot",
            name="surface_habitable_totale",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=12, null=True
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="acquereur",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="acte_de_propriete",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="administration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="instructeurs.administration",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="annee_gestion_programmation",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="autres_locaux_hors_convention",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="certificat_adressage",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="code_insee_commune",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="code_insee_departement",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="code_insee_region",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_achat",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_achevement",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_achevement_compile",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_achevement_previsible",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_acte_notarie",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_autorisation_hors_habitat_inclusif",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_convention_location",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="date_residence_argement_gestionnaire_intermediation",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="departement_residence_argement_gestionnaire_intermediation",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="edd_classique",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="edd_volumetrique",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="effet_relatif",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="mention_publication_edd_classique",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="mention_publication_edd_volumetrique",
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="nb_bureaux",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="nb_locaux_commerciaux",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="numero_operation",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="numero_operation_pour_recherche",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="programmes.programme",
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="permis_construire",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="reassign_command_old_admin_backup",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="reference_cadastrale",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="reference_notaire",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="reference_publication_acte",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="surface_corrigee_totale",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="surface_utile_totale",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="vendeur",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="ville_signature_residence_agrement_gestionnaire_intermediation",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="programme",
            name="zone_123",
            field=models.CharField(
                blank=True,
                choices=[("1", "01"), ("2", "02"), ("3", "03"), ("1bis", "1bis")],
                default=None,
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="programme",
            name="zone_abc",
            field=models.CharField(
                blank=True,
                choices=[
                    ("A", "A"),
                    ("Abis", "Abis"),
                    ("B1", "B1"),
                    ("B2", "B2"),
                    ("C", "C"),
                    ("DROM", "DROM"),
                ],
                default=None,
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="referencecadastrale",
            name="lieudit",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="referencecadastrale",
            name="numero",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="referencecadastrale",
            name="section",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="referencecadastrale",
            name="surface",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

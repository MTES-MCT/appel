# Generated by Django 3.2.14 on 2022-09-10 08:14

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("conventions", "0033_alter_convention_parent"),
    ]

    operations = [
        migrations.AlterField(
            model_name="convention",
            name="avenant_type",
            field=models.CharField(
                blank=True,
                choices=[("Logements", "Modification des logements")],
                default="Logements",
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="convention",
            name="comments",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="date_fin_conventionnement",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="date_resiliation",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="donnees_validees",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="fond_propre",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="nom_fichier_signe",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="numero",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="parent",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="avenants",
                to="conventions.convention",
            ),
        ),
        migrations.AlterField(
            model_name="convention",
            name="premiere_soumission_le",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="soumis_le",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="televersement_convention_signee_le",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="convention",
            name="type1and2",
            field=models.CharField(
                blank=True,
                choices=[("Type1", "Type I"), ("Type2", "Type II")],
                max_length=25,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="convention",
            name="valide_le",
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="conventionhistory",
            name="commentaire",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="conventionhistory",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="valide_par",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="pret",
            name="autre",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="pret",
            name="date_octroi",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pret",
            name="duree",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="pret",
            name="numero",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]

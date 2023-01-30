# Generated by Django 4.1.5 on 2023-01-30 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("programmes", "0063_alter_logement_typologie"),
    ]

    operations = [
        migrations.AddField(
            model_name="logement",
            name="surface_corrigee",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=6,
                null=True,
                verbose_name="Surface corrigée",
            ),
        ),
    ]

# Generated by Django 4.2.9 on 2024-02-06 16:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("conventions", "0080_convention_convention_tele_signee_le_idx"),
    ]

    operations = [
        migrations.AddField(
            model_name="convention",
            name="gestionnaire_bloc_info_complementaire",
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]

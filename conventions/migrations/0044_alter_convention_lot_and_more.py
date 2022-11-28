# Generated by Django 4.1.3 on 2022-11-28 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("programmes", "0056_alter_logementedd_programme_alter_lot_programme_and_more"),
        ("conventions", "0043_remove_bailleur"),
    ]

    operations = [
        migrations.AlterField(
            model_name="convention",
            name="lot",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conventions",
                to="programmes.lot",
            ),
        ),
        migrations.AlterField(
            model_name="conventionhistory",
            name="convention",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="conventionhistories",
                to="conventions.convention",
            ),
        ),
        migrations.AlterField(
            model_name="pret",
            name="convention",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prets",
                to="conventions.convention",
            ),
        ),
    ]

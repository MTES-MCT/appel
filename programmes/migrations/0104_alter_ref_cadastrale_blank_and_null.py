# Generated by Django 4.2.13 on 2024-09-03 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    atomic = False

    dependencies = [
        ("instructeurs", "0001_initial_squashed_0017_auto_20230925_1209"),
        ("programmes", "0103_alter_lot_blank_and_null"),
    ]

    operations = [
        migrations.AlterField(
            model_name="referencecadastrale",
            name="lieudit",
            field=models.CharField(blank=True, default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="referencecadastrale",
            name="numero",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="referencecadastrale",
            name="section",
            field=models.CharField(blank=True, default="", max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="referencecadastrale",
            name="surface",
            field=models.CharField(blank=True, default="", max_length=255),
            preserve_default=False,
        ),
    ]

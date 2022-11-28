# Generated by Django 4.1.3 on 2022-11-28 15:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("instructeurs", "0008_administration_nb_convention_exemplaires"),
        ("bailleurs", "0013_bailleur_nature_bailleur"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("users", "0016_alter_user_preferences_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="role",
            name="administration",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles",
                to="instructeurs.administration",
            ),
        ),
        migrations.AlterField(
            model_name="role",
            name="bailleur",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles",
                to="bailleurs.bailleur",
            ),
        ),
        migrations.AlterField(
            model_name="role",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles",
                to="auth.group",
            ),
        ),
        migrations.AlterField(
            model_name="role",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]

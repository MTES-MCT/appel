# Generated by Django 3.2.5 on 2021-07-27 12:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bailleurs", "0003_alter_bailleur_options"),
        ("auth", "0012_alter_user_first_name_max_length"),
        ("instructeurs", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "typologie",
                    models.CharField(
                        choices=[
                            ("INSTRUCTEUR", "Instructeur"),
                            ("BAILLEUR", "Bailleur"),
                        ],
                        default="BAILLEUR",
                        max_length=25,
                    ),
                ),
                (
                    "administration",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="instructeurs.administration",
                    ),
                ),
                (
                    "bailleur",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="bailleurs.bailleur",
                    ),
                ),
                (
                    "group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="auth.group"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

# Generated by Django 3.2.12 on 2022-04-18 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("conventions", "0017_auto_20220401_1212"),
    ]

    operations = [
        migrations.AddField(
            model_name="convention",
            name="type1and2",
            field=models.CharField(
                choices=[("Type1", "Type I"), ("Type2", "Type II")],
                max_length=25,
                null=True,
            ),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-07 15:16

from django.db import migrations
from django.db.models import Count


def clear_siap_users_from_standalone(apps, schema_editor):
    User = apps.get_model("users", "User")
    duplicates = (
        User.objects.values("email")
        .annotate(email_count=Count("email"))
        .filter(email_count__gt=1)
        .values_list("email", flat=True)
    )

    for email in list(duplicates):
        print(email)

    print(f"{len(duplicates)} emails en doublons détectés")

    users_to_delete = User.objects.filter(email__in=duplicates).exclude(
        cerbere_login=None
    )
    print(f"{len(users_to_delete)} utilisateurs vont être supprimés")
    users_to_delete.delete()


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0024_remove_read_popup"),
    ]

    operations = [migrations.RunPython(clear_siap_users_from_standalone)]

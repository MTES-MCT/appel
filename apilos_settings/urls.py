from django.urls import path

from . import views

urlpatterns = [
    path(
        "administrations/",
        views.administrations,
        name="administrations",
    ),
    path(
        "administrations/<administration_uuid>",
        views.edit_administration,
        name="edit_administration",
    ),
    path(
        "bailleurs/",
        views.bailleurs,
        name="bailleurs",
    ),
    path(
        "bailleurs/<bailleur_uuid>",
        views.edit_bailleur,
        name="edit_bailleur",
    ),
    path(
        "profile/",
        views.profile,
        name="profile",
    ),
    path(
        "users/",
        views.users,
        name="users",
    ),
]

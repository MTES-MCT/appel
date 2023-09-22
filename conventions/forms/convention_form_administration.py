from django import forms
from django.core.validators import RegexValidator

from instructeurs.models import Administration


class UpdateConventionAdministrationForm(forms.Form):
    administration = forms.ModelChoiceField(
        label="Administration",
        queryset=Administration.objects.all(),
        to_field_name="uuid",
        error_messages={
            "required": "Vous devez choisir une administration",
            "min_length": "min : Vous devez choisir une administration",
            "invalid_choice": "invalid : Vous devez choisir une administration",
        },
    )

    verification = forms.CharField(
        label="Vérification",
        validators=[RegexValidator("transférer")],
        required=True,
        error_messages={
            "required": "Vous devez recopier le mot pour valider l'opération",
        },
    )

    convention = forms.CharField(widget=forms.HiddenInput())

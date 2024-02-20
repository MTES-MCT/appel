from io import BytesIO

from django.forms import FileField, forms

from apilos_settings.services.services_file import (
    BailleurListingProcessor,
    FileReadingError,
)


class BailleurListingUploadForm(forms.Form):

    file = FileField(
        error_messages={
            "required": (
                "Vous devez sélectionner un fichier avant "
                + "de cliquer sur le bouton 'Déposer'"
            ),
        }
    )

    def clean(self):
        cleaned_data = super().clean()

        try:
            cleaned_data["users"] = BailleurListingProcessor(
                filename=BytesIO(cleaned_data.get("file").read())
            ).process()
        except FileReadingError as e:
            self.add_error("file", e)

        return cleaned_data

from django import forms
from django.core.exceptions import ValidationError
from django.forms import BaseFormSet, formset_factory
from core.utils import round_half_up

from programmes.models import (
    Logement,
    LogementEDD,
    Lot,
    TypologieLogementClassique,
    TypologieLogementFoyerResidence,
    TypologieAnnexe,
    TypologieStationnement,
    FinancementEDD,
)


class ProgrammeCadastralForm(forms.Form):
    """
    Form to edit cadastral informations (step of convention builder)
    content :
    * Buildig premit
    * Notarial and end dates
    * Notarial elements (dates, files, image)
    * Cadastral references
    """

    uuid = forms.UUIDField(
        required=False,
        label="Informations cadastrales",
    )
    permis_construire = forms.CharField(
        required=False,
        label="Numéro de permis construire",
        max_length=255,
        error_messages={
            "max_length": "Le permis de construire ne doit pas excéder 255 caractères",
        },
    )
    date_acte_notarie = forms.DateField(
        required=False,
        label="Date de l'acte notarié (si différent de la date d’achat)",
    )
    date_achevement_previsible = forms.DateField(
        required=False,
        label="Date d'achèvement previsible",
    )
    date_achat = forms.DateField(required=False, label="Date d'achat")
    date_achevement = forms.DateField(
        required=False,
        label="Date d'achèvement ou d'obtention de certificat de conformité",
    )

    date_autorisation_hors_habitat_inclusif = forms.DateField(
        required=False,
        label="",
    )
    date_convention_location = forms.DateField(
        required=False,
        label="",
    )

    date_residence_argement_gestionnaire_intermediation = forms.DateField(
        required=False,
        label="",
    )
    departement_residence_argement_gestionnaire_intermediation = forms.CharField(
        required=False,
        label="",
        max_length=255,
        error_messages={
            "max_length": "Le département ne doit pas excéder 255 caractères",
        },
    )
    ville_signature_residence_argement_gestionnaire_intermediation = forms.CharField(
        required=False,
        label="",
        max_length=255,
        error_messages={
            "max_length": "La ville de signatures ne doit pas excéder 255 caractères",
        },
    )
    date_residence_agrement = forms.DateField(
        required=False,
        label="",
    )
    departement_residence_agrement = forms.CharField(
        required=False,
        label="",
        max_length=255,
        error_messages={
            "max_length": "Le département ne doit pas excéder 255 caractères",
        },
    )

    vendeur = forms.CharField(
        required=False,
        label="Vendeur",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    vendeur_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images sont acceptés dans la limite de 100 Mo",
    )
    acquereur = forms.CharField(
        required=False,
        label="Acquéreur",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    acquereur_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images sont acceptés dans la limite de 100 Mo",
    )
    reference_notaire = forms.CharField(
        required=False,
        label="Référence du notaire",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    reference_notaire_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images sont acceptés dans la limite de 100 Mo",
    )
    reference_publication_acte = forms.CharField(
        required=False,
        label="Référence de publication de l'acte",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    reference_publication_acte_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images sont acceptés dans la limite de 100 Mo",
    )
    acte_de_propriete = forms.CharField(
        required=False,
        label="Acte de propriété / Acte notarial",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    acte_de_propriete_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images et pdf sont acceptés dans la limite de 100 Mo",
    )
    certificat_adressage = forms.CharField(
        required=False,
        label="Certificat d'adressage / Autres",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    certificat_adressage_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images et pdf sont acceptés dans la limite de 100 Mo",
    )
    effet_relatif = forms.CharField(
        required=False,
        label="Effet relatif",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    effet_relatif_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images et pdf sont acceptés dans la limite de 100 Mo",
    )
    reference_cadastrale = forms.CharField(
        required=False,
        label="Références cadastrales",
        max_length=5000,
        error_messages={
            "max_length": "Le message ne doit pas excéder 5000 caractères",
        },
    )
    reference_cadastrale_files = forms.CharField(
        required=False,
        help_text="Les fichiers de type images sont acceptés dans la limite de 100 Mo",
    )


class ReferenceCadastraleForm(forms.Form):

    uuid = forms.UUIDField(
        required=False,
        label="Référence Cadastrale",
    )
    section = forms.CharField(
        required=True,
        label="",
        max_length=255,
        error_messages={
            "required": "La section est obligatoire",
            "max_length": "Le message ne doit pas excéder 255 caractères",
        },
    )
    numero = forms.IntegerField(
        required=True,
        label="",
        error_messages={
            "required": "Le numéro est obligatoire",
        },
    )
    lieudit = forms.CharField(
        required=True,
        label="",
        max_length=255,
        error_messages={
            "required": "Le lieudit est obligatoire",
            "max_length": "Le lieudit ne doit pas excéder 255 caractères",
        },
    )
    surface = forms.CharField(
        required=True,
        label="",
        max_length=255,
        error_messages={
            "required": "La surface est obligatoire",
            "max_length": "La surface ne doit pas excéder 255 caractères",
        },
    )


class BaseReferenceCadastraleFormSet(BaseFormSet):
    pass


ReferenceCadastraleFormSet = formset_factory(
    ReferenceCadastraleForm, formset=BaseReferenceCadastraleFormSet, extra=0
)


class LotLgtsOptionForm(forms.Form):

    uuid = forms.UUIDField(
        required=False,
        label="Logement du programme",
    )
    lgts_mixite_sociale_negocies = forms.IntegerField(
        required=False,
        label=(
            "Nombre de logements à louer en plus à des ménages dont les ressources"
            + " n'excèdent pas le plafond"
        ),
        help_text="""
            Plafond fixé au I de l'article D. 331-12. Ce nombre de logements doit-être
            négocié avec les services instructeurs et n'est pas obligatoire. Il sera
            reporté sur l'article de mixité sociale correspondant su le document de convention.
        """,
    )
    loyer_derogatoire = forms.DecimalField(
        required=False,
        label="Loyer dérogatoire",
        help_text="""
            Montant de loyer d'une opération d'acquisition qui n'est pas liée à la réalisation de travaux mais
            fait suite à une nouvelle acquisition pour un locataire ou un occupant de bonne foi dont les
            ressources excèdent les plafonds de ressources par dérogation et à titre transitoire
        """,
        max_digits=6,
        decimal_places=2,
        error_messages={
            "max_digits": "Le loyer dérogatoire par m² doit-être inférieur à 10000 €",
        },
    )
    nb_logements = forms.IntegerField(
        required=False,
        label="Nombre de logements",
    )


class LotFoyerResidenceLgtsDetailsForm(forms.Form):
    floor_surface_habitable_totale: float
    uuid = forms.UUIDField(
        required=False,
        label="Logement du programme",
    )
    surface_habitable_totale = forms.DecimalField(
        label="Surface habitable totale en m²",
        help_text="concerne la surface habitable de tout le bâti, y compris les locaux"
        + " auxquels ne s’applique pas la convention",
        max_digits=7,
        decimal_places=2,
        error_messages={
            "required": "La surface habitable totale est obligatoire",
            "max_digits": "La surface habitable doit-être inférieur à 100000 m²",
        },
    )

    def clean_surface_habitable_totale(self):
        surface_habitable_totale = self.cleaned_data.get("surface_habitable_totale", 0)
        if surface_habitable_totale < self.floor_surface_habitable_totale:
            raise ValidationError(
                "La surface habitable ne peut-être inférieur à la somme des surfaces"
                + f" habitables des logements ({self.floor_surface_habitable_totale} m²)"
            )

        return surface_habitable_totale


class ProgrammeEDDForm(forms.Form):

    uuid = forms.UUIDField(
        required=False,
        label="Logement du programme",
    )
    lot_uuid = forms.UUIDField(required=False)
    edd_volumetrique = forms.CharField(
        required=False,
        label="EDD volumétrique",
        max_length=50000,
        error_messages={
            "max_length": "L'EDD volumétrique ne doit pas excéder 50000 caractères",
        },
    )
    edd_volumetrique_files = forms.CharField(
        required=False,
    )
    mention_publication_edd_volumetrique = forms.CharField(
        required=False,
        label="Mention de publication de l'EDD volumétrique",
        max_length=1000,
        error_messages={
            "max_length": "La mention de publication de l'EDD volumétrique "
            + "ne doit pas excéder 1000 caractères",
        },
        help_text=(
            "Référence légale de dépôt de l'état descriptif de division "
            + "volumétrique aux services de la publicité foncière comportant "
            + "le numéro, le service, la date et les volumes du dépôt"
        ),
    )
    edd_classique = forms.CharField(
        required=False,
        label="EDD classique",
        max_length=50000,
        error_messages={
            "max_length": "L'EDD classique ne doit pas excéder 50000 caractères",
        },
    )
    edd_classique_files = forms.CharField(
        required=False,
    )
    mention_publication_edd_classique = forms.CharField(
        required=False,
        label="Mention de publication de l'EDD classique",
        max_length=1000,
        error_messages={
            "max_length": "La mention de publication de l'EDD classique "
            + "ne doit pas excéder 1000 caractères",
        },
        help_text=(
            "Référence légale de dépôt de l'état descriptif de division "
            + "classique aux services de la publicité foncière comportant "
            + "le numéro, le service, la date et les volumes du dépôt"
        ),
    )


class LogementForm(forms.Form):

    uuid = forms.UUIDField(
        required=False,
        label="Logement",
    )
    designation = forms.CharField(
        label="",
        max_length=255,
        min_length=1,
        error_messages={
            "required": "La designation du logement est obligatoire",
            "min_length": "La designation du logement est obligatoire",
            "max_length": "La designation du logement ne doit pas excéder 255 caractères",
        },
    )
    typologie = forms.TypedChoiceField(
        required=True,
        label="",
        choices=TypologieLogementClassique.choices,
        error_messages={
            "required": "Le type de logement est obligatoire",
        },
    )
    surface_habitable = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "La surface habitable est obligatoire",
            "max_digits": "La surface habitable doit-être inférieur à 10000 m²",
        },
    )
    surface_annexes = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "La surface des annexes est obligatoire",
            "max_digits": "La surface des annexes doit-être inférieur à 10000 m²",
        },
    )
    surface_annexes_retenue = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "La surface des annexes retenue est obligatoire",
            "max_digits": "La surface des annexes retenue doit-être inférieur à 10000 m²",
        },
    )
    surface_utile = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "La surface utile est obligatoire",
            "max_digits": "La surface utile doit-être inférieur à 10000 m²",
        },
    )
    loyer_par_metre_carre = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "Le loyer par m² est obligatoire",
            "max_digits": "La loyer par m² doit-être inférieur à 10000 €",
        },
    )
    coeficient = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=4,
        error_messages={
            "required": "Le coefficient est obligatoire",
            "max_digits": "La coefficient doit-être inférieur à 1000",
        },
    )
    loyer = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "Le loyer est obligatoire",
            "max_digits": "La loyer doit-être inférieur à 10000 €",
        },
    )

    def clean_loyer(self):
        surface_utile = self.cleaned_data.get("surface_utile", 0)
        loyer_par_metre_carre = self.cleaned_data.get("loyer_par_metre_carre", 0)
        coeficient = self.cleaned_data.get("coeficient", 0)
        loyer = self.cleaned_data.get("loyer", 0)

        # check that lot_id exist in DB
        if (
            abs(
                round_half_up(loyer, 2)
                - round_half_up(surface_utile * loyer_par_metre_carre * coeficient, 2)
            )
            > 1
        ):
            raise ValidationError(
                "Le loyer doit-être le produit de la surface utile,"
                + " du loyer par mètre carré et du coefficient. valeur attendue :"
                + f" {round_half_up(surface_utile*loyer_par_metre_carre*coeficient,2)} €"
                + " (tolérance de 1 €)"
            )

        return loyer


class BaseLogementFormSet(BaseFormSet):
    programme_id = None
    lot_id = None
    nb_logements = None

    def clean(self):
        self.manage_non_empty_validation()
        self.manage_designation_validation()
        self.manage_same_loyer_par_metre_carre()
        self.manage_edd_consistency()
        self.manage_nb_logement_consistency()
        self.manage_coefficient_propre()

    def manage_non_empty_validation(self):
        if len(self.forms) == 0:
            error = ValidationError("La liste des logements ne peut pas être vide")
            self._non_form_errors.append(error)

    def manage_designation_validation(self):
        designations = {}
        error_on_designation = False
        for form in self.forms:
            #            if self.can_delete() and self._should_delete_form(form):
            #                continue
            designation = form.cleaned_data.get("designation")
            if designation:
                if designation in designations:
                    error_on_designation = True
                    form.add_error(
                        "designation",
                        "Les designations de logement doivent être distinct "
                        + "lorsqu'ils sont définis",
                    )
                    if "designation" not in designations[designation].errors:
                        designations[designation].add_error(
                            "designation",
                            "Les designations de logement doivent être distinct lorsqu'ils sont "
                            + "définis",
                        )
                designations[designation] = form
        if error_on_designation:
            error = ValidationError(
                "Les designations de logement doivent être distinct lorsqu'ils sont définis !!!"
            )
            self._non_form_errors.append(error)

    def manage_same_loyer_par_metre_carre(self):
        lpmc = None
        error = None
        for form in self.forms:
            if lpmc is None:
                lpmc = form.cleaned_data.get("loyer_par_metre_carre")
            elif (
                lpmc != form.cleaned_data.get("loyer_par_metre_carre") and error is None
            ):
                error = ValidationError(
                    "Le loyer par mètre carré doit être le même pour tous les logements du lot"
                )
                self._non_form_errors.append(error)
        if error is not None:
            for form in self.forms:
                form.add_error(
                    "loyer_par_metre_carre",
                    "Le loyer par mètre carré doit être le même pour tous les logements du lot",
                )

    def manage_edd_consistency(self):
        lgts_edd = LogementEDD.objects.filter(programme_id=self.programme_id)
        lot = Lot.objects.get(id=self.lot_id)

        if lgts_edd.count() != 0:
            for form in self.forms:
                try:
                    lgt_edd = lgts_edd.get(
                        designation=form.cleaned_data.get("designation"),
                        financement=lot.financement,
                    )
                    if lgt_edd.financement != lot.financement:
                        form.add_error(
                            "designation",
                            "Ce logement est déclaré comme "
                            + f"{lgt_edd.financement} dans l'EDD simplifié "
                            + "alors que vous déclarez un lot de type "
                            + f"{lot.financement}",
                        )
                except LogementEDD.DoesNotExist:
                    form.add_error(
                        "designation", "Ce logement n'est pas dans l'EDD simplifié"
                    )
                except LogementEDD.MultipleObjectsReturned:
                    form.add_error(
                        "designation",
                        "Ce logement est présent plusieurs fois dans l'EDD simplifié",
                    )

    def manage_nb_logement_consistency(self):
        if self.nb_logements is None:
            lot = Lot.objects.get(id=self.lot_id)
            nb_logements = lot.nb_logements
        else:
            nb_logements = int(self.nb_logements)
        if nb_logements != self.total_form_count():
            error = ValidationError(
                f"Le nombre de logement a conventionner ({nb_logements}) "
                + f"ne correspond pas au nombre de logements déclaré ({self.total_form_count()})"
            )
            self._non_form_errors.append(error)

    def manage_coefficient_propre(self):
        lot = Lot.objects.get(id=self.lot_id)
        loyer_with_coef = 0
        loyer_without_coef = 0
        for form in self.forms:
            coeficient = form.cleaned_data.get("coeficient")
            surface_utile = form.cleaned_data.get("surface_utile")
            loyer_par_metre_carre = form.cleaned_data.get("loyer_par_metre_carre")
            if None in [coeficient, surface_utile, loyer_par_metre_carre]:
                # Another error is catch before and need to be managed before
                return
            loyer_with_coef += coeficient * surface_utile * loyer_par_metre_carre
            loyer_without_coef += surface_utile * loyer_par_metre_carre
        nb_logements = self.nb_logements if self.nb_logements else lot.nb_logements
        if (
            round_half_up(loyer_with_coef, 2)
            > round_half_up(loyer_without_coef, 2) + nb_logements
        ):
            error = ValidationError(
                "La somme des loyers après application des coefficients ne peut excéder "
                + "la somme des loyers sans application des coefficients, c'est à dire "
                + f"{round_half_up(loyer_without_coef,2)} € (tolérance de {nb_logements} €)"
            )
            self._non_form_errors.append(error)


LogementFormSet = formset_factory(LogementForm, formset=BaseLogementFormSet, extra=0)


class FoyerResidenceLogementForm(forms.Form):

    uuid = forms.UUIDField(
        required=False,
        label="Logement",
    )
    designation = forms.CharField(
        label="",
        max_length=255,
        min_length=1,
        error_messages={
            "required": "Le numéro du logement du logement est obligatoire",
            "min_length": "Le numéro du logement du logement est obligatoire",
            "max_length": "Le numéro du logement du logement ne doit pas excéder 255 caractères",
        },
    )
    typologie = forms.TypedChoiceField(
        required=True,
        label="",
        choices=TypologieLogementFoyerResidence.choices,
        error_messages={
            "required": "Le type de logement est obligatoire",
        },
    )
    surface_habitable = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "La surface habitable est obligatoire",
            "max_digits": "La surface habitable doit-être inférieur à 10000 m²",
        },
    )
    loyer = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "La redevance maximale est obligatoire",
            "max_digits": "La redevance maximale inférieur à 10000 €",
        },
    )


class BaseFoyerResidenceLogementFormSet(BaseFormSet):
    nb_logements = None
    lot_id = None

    def clean(self):
        self.loan_should_be_consistent()
        self.manage_nb_logement_consistency()

    def manage_nb_logement_consistency(self):
        if self.nb_logements is None:
            lot = Lot.objects.get(id=self.lot_id)
            nb_logements = lot.nb_logements
        else:
            nb_logements = int(self.nb_logements)
        if nb_logements != self.total_form_count():
            error = ValidationError(
                f"Le nombre de logement a conventionner ({nb_logements}) "
                + f"ne correspond pas au nombre de logements déclaré ({self.total_form_count()})"
            )
            self._non_form_errors.append(error)

    def loan_should_be_consistent(self):
        loan_by_type = {}
        loan_errors = {}
        for form in self.forms:
            typologie = form.cleaned_data.get("typologie", "")
            if typologie not in loan_by_type:
                loan_by_type[typologie] = form.cleaned_data.get("loyer")
            else:
                if loan_by_type[typologie] != form.cleaned_data.get("loyer"):
                    loan_errors[typologie] = ValidationError(
                        "Les loyers doivent-être identiques pour les logements de"
                        + f" typologie identique : {form.cleaned_data.get('typologie')}"
                    )
        for _, loan_error in loan_errors.items():
            self._non_form_errors.append(loan_error)


FoyerResidenceLogementFormSet = formset_factory(
    FoyerResidenceLogementForm,
    formset=BaseFoyerResidenceLogementFormSet,
    extra=0,
)


class AnnexeForm(forms.Form):

    uuid = forms.UUIDField(
        required=False,
        label="Annexe",
    )
    typologie = forms.TypedChoiceField(
        required=True,
        label="",
        choices=TypologieAnnexe.choices,
    )
    logement_designation = forms.CharField(
        label="",
        max_length=255,
        min_length=1,
        error_messages={
            "required": "La designation du logement est obligatoire",
            "min_length": "La designation du logement est obligatoire",
            "max_length": "La designation du logement ne doit pas excéder 255 caractères",
        },
    )
    logement_typologie = forms.TypedChoiceField(
        required=True, label="", choices=TypologieLogementClassique.choices
    )
    surface_hors_surface_retenue = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "La surface habitable est obligatoire",
            "max_digits": "La surface habitable doit-être inférieur à 10000 m²",
        },
    )
    loyer_par_metre_carre = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "Le loyer par m² est obligatoire",
            "max_digits": "La loyer par m² doit-être inférieur à 10000 €",
        },
    )
    loyer = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "Le loyer est obligatoire",
            "max_digits": "La loyer doit-être inférieur à 10000 €",
        },
    )

    def clean_loyer(self):
        surface_hors_surface_retenue = self.cleaned_data.get(
            "surface_hors_surface_retenue", 0
        )
        loyer_par_metre_carre = self.cleaned_data.get("loyer_par_metre_carre", 0)
        loyer = self.cleaned_data.get("loyer", 0)

        # check that lot_id exist in DB
        if round_half_up(loyer, 2) > (
            round_half_up(surface_hors_surface_retenue * loyer_par_metre_carre, 2) + 0.1
        ):
            raise ValidationError(
                "Le loyer ne peut être supérieur au produit de la surface"
                + " de l'annexe et du loyer par mètre carré. valeur attendue :"
                + f" {round_half_up(surface_hors_surface_retenue*loyer_par_metre_carre,2)} €"
                + " (tolérance de 0,1 €)"
            )

        return loyer


class BaseAnnexeFormSet(BaseFormSet):
    convention = None

    def clean(self):
        self.manage_logement_exists_validation()

    def manage_logement_exists_validation(self):
        if self.convention:
            lgts = self.convention.lot.logements.all()
            for form in self.forms:
                try:
                    lgts.get(designation=form.cleaned_data.get("logement_designation"))
                except Logement.DoesNotExist:
                    form.add_error(
                        "logement_designation", "Ce logement n'existe pas dans ce lot"
                    )


AnnexeFormSet = formset_factory(AnnexeForm, formset=BaseAnnexeFormSet, extra=0)


class TypeStationnementForm(forms.Form):

    uuid = forms.UUIDField(
        required=False,
        label="Type de stationnement",
    )
    typologie = forms.TypedChoiceField(
        required=True,
        label="",
        choices=TypologieStationnement.choices,
        error_messages={
            "required": "La typologie des stationnement est obligatoire",
        },
    )
    nb_stationnements = forms.IntegerField(
        label="",
        error_messages={
            "required": "Le nombre de stationnements est obligatoire",
        },
    )
    loyer = forms.DecimalField(
        label="",
        max_digits=6,
        decimal_places=2,
        error_messages={
            "required": "Le loyer est obligatoire",
            "max_digits": "La loyer doit-être inférieur à 10000 €",
        },
    )


class BaseTypeStationnementFormSet(BaseFormSet):
    pass


TypeStationnementFormSet = formset_factory(
    TypeStationnementForm, formset=BaseTypeStationnementFormSet, extra=0
)


class LogementEDDForm(forms.Form):

    uuid = forms.UUIDField(required=False, label="Logement de l'EDD")
    designation = forms.CharField(
        label="",
        max_length=255,
        min_length=1,
        error_messages={
            "required": "La designation du logement est obligatoire",
            "min_length": "La designation du logement est obligatoire",
            "max_length": "La designation du logement ne doit pas excéder 255 caractères",
        },
    )
    numero_lot = forms.CharField(
        label="",
        max_length=255,
        min_length=1,
        error_messages={
            "max_length": "Le numéro de lot ne doit pas excéder 255 caractères",
        },
    )
    financement = forms.TypedChoiceField(
        required=True,
        label="",
        choices=FinancementEDD.choices,
        error_messages={
            "required": "Le financement est obligatoire",
        },
    )


class BaseLogementEDDFormSet(BaseFormSet):
    programme_id = None
    optional_errors = []
    ignore_optional_errors = False

    def is_valid(self):
        return super().is_valid() and len(self.optional_errors) == 0

    def clean(self):
        self.manage_edd_consistency()

    def manage_edd_consistency(self):
        self.optional_errors = []
        if len(self.forms) == 0 or self.ignore_optional_errors:
            return
        lots = Lot.objects.filter(programme_id=self.programme_id)
        programme_financements = list(set(map(lambda x: x.financement, lots)))
        lgts_edd_financements = list(
            set(map(lambda x: x.cleaned_data.get("financement"), self.forms))
        )
        for programme_financement in programme_financements:
            if programme_financement not in lgts_edd_financements:
                if len(programme_financements) > 1:
                    financement_message = (
                        "Les financements connus pour ce programme sont "
                        + ", ".join(programme_financements)
                    )
                else:
                    financement_message = (
                        "Le seul financement connu pour ce programme est "
                        + programme_financement
                    )

                error = ValidationError(
                    "L'EDD simplifié doit comporter tous les logements du "
                    + f"programme quelquesoit leur financement. {financement_message}",
                    code=101,
                )
                self.optional_errors.append(error)
                return


LogementEDDFormSet = formset_factory(
    LogementEDDForm, formset=BaseLogementEDDFormSet, extra=0
)


class LotAnnexeForm(forms.Form):
    uuid = forms.UUIDField(required=False)
    annexe_caves = forms.BooleanField(
        required=False,
        label="Caves",
    )
    annexe_soussols = forms.BooleanField(
        required=False,
        label="Sous-sols",
    )
    annexe_remises = forms.BooleanField(
        required=False,
        label="Remises",
    )
    annexe_ateliers = forms.BooleanField(
        required=False,
        label="Ateliers",
    )
    annexe_sechoirs = forms.BooleanField(
        required=False,
        label="Séchoirs",
    )
    annexe_celliers = forms.BooleanField(
        required=False,
        label="Celliers extérieurs au logement",
    )
    annexe_resserres = forms.BooleanField(required=False, label="Resserres")
    annexe_combles = forms.BooleanField(
        required=False,
        label="Combles et greniers aménageables",
    )
    annexe_balcons = forms.BooleanField(
        required=False,
        label="Balcons",
    )
    annexe_loggias = forms.BooleanField(
        required=False,
        label="Loggias et Vérandas",
    )
    annexe_terrasses = forms.BooleanField(
        required=False,
        label="Terrasses",
        help_text=(
            "Dans la limite de 9 m2, les parties de terrasses accessibles en étage ou aménagées"
            + " sur ouvrage enterré ou à moitié enterré"
        ),
    )

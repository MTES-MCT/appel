from django.contrib.auth.decorators import permission_required
from django.urls import path
from django.views.generic import TemplateView

from . import views
from .views import (
    ConventionActivesSearchView,
    ConventionEnInstructionSearchView,
    ConventionIndexView,
    ConventionSearchView,
    ConventionTermineesSearchView,
    LoyerSimulateurView,
)

urlpatterns = [
    # Pages de premier niveau : recherche et calculette de loyer
    path(
        "",
        ConventionIndexView.as_view(),
        name="index",
    ),
    path(
        "recherche",
        ConventionSearchView.as_view(),
        name=ConventionSearchView.name,
    ),
    path(
        "en-cours",
        ConventionEnInstructionSearchView.as_view(),
        name=ConventionEnInstructionSearchView.name,
    ),
    path(
        "actives",
        ConventionActivesSearchView.as_view(),
        name=ConventionActivesSearchView.name,
    ),
    path(
        "resiliees",
        ConventionTermineesSearchView.as_view(),
        name=ConventionTermineesSearchView.name,
    ),
    path(
        "simulateur-de-loyer",
        LoyerSimulateurView.as_view(),
        name="loyer_simulateur",
    ),
    # Pages de second niveau : onglet de la vue convention
    path(
        "recapitulatif/<convention_uuid>",
        views.RecapitulatifView.as_view(),
        name="recapitulatif",
    ),
    path(
        "post_action/<convention_uuid>",
        views.post_action,
        name="post_action",
    ),
    path(
        "preview/<convention_uuid>",
        views.preview,
        name="preview",
    ),
    path(
        "journal/<convention_uuid>",
        views.journal,
        name="journal",
    ),
    # Pages pour l'ajout simplifié d'une convention finalisée, depuis une opération
    path(
        "from_operation",
        views.SelectOperationView.as_view(),
        name="from_operation_select",
    ),
    path(
        "from_operation/add_convention/<numero_operation>",
        permission_required("convention.add_convention")(
            views.AddConventionView.as_view()
        ),
        name="from_operation_add_convention",
    ),
    path(
        "from_operation/add_avenants/<uuid:convention_uuid>",
        permission_required("convention.add_convention")(
            views.AddAvenantsView.as_view()
        ),
        name="from_operation_add_avenants",
    ),
    # Pages de troisième niveau : funnel d'instruction et d'action sur les conventions et avenants
    path(
        "new_convention_choice",
        TemplateView.as_view(template_name="conventions/new_convention_choice.html"),
        name="new_convention_choice",
    ),
    path(
        "new_convention_anru",
        permission_required("convention.add_convention")(
            views.NewConventionAnruView.as_view()
        ),
        name="new_convention_anru",
    ),
    path(
        "bailleur/<convention_uuid>",
        views.ConventionBailleurView.as_view(),
        name="bailleur",
    ),
    path(
        "avenant_bailleur/<convention_uuid>",
        views.AvenantBailleurView.as_view(),
        name="avenant_bailleur",
    ),
    path(
        "programme/<convention_uuid>",
        views.ConventionProgrammeView.as_view(),
        name="programme",
    ),
    path(
        "avenant_programme/<convention_uuid>",
        views.AvenantProgrammeView.as_view(),
        name="avenant_programme",
    ),
    path(
        "cadastre/<convention_uuid>",
        views.ConventionCadastreView.as_view(),
        name="cadastre",
    ),
    path("edd/<convention_uuid>", views.ConventionEDDView.as_view(), name="edd"),
    path(
        "financement/<convention_uuid>",
        views.ConventionFinancementView.as_view(),
        name="financement",
    ),
    path(
        "avenant_financement/<convention_uuid>",
        views.AvenantFinancementView.as_view(),
        name="avenant_financement",
    ),
    path(
        "logements/<convention_uuid>",
        views.ConventionLogementsView.as_view(),
        name="logements",
    ),
    path(
        "avenant_logements/<convention_uuid>",
        views.AvenantLogementsView.as_view(),
        name="avenant_logements",
    ),
    path(
        "foyer_residence_logements/<convention_uuid>",
        views.ConventionFoyerResidenceLogementsView.as_view(),
        name="foyer_residence_logements",
    ),
    path(
        "avenant_foyer_residence_logements/<convention_uuid>",
        views.AvenantFoyerResidenceLogementsView.as_view(),
        name="avenant_foyer_residence_logements",
    ),
    path(
        "annexes/<convention_uuid>",
        views.ConventionAnnexesView.as_view(),
        name="annexes",
    ),
    path(
        "avenant_annexes/<convention_uuid>",
        views.AvenantAnnexesView.as_view(),
        name="avenant_annexes",
    ),
    path(
        "collectif/<convention_uuid>",
        views.ConventionCollectifView.as_view(),
        name="collectif",
    ),
    path(
        "avenant_collectif/<convention_uuid>",
        views.AvenantCollectifView.as_view(),
        name="avenant_collectif",
    ),
    path(
        "stationnements/<convention_uuid>",
        views.ConventionTypeStationnementView.as_view(),
        name="stationnements",
    ),
    path(
        "foyer_attribution/<convention_uuid>",
        views.ConventionFoyerAttributionView.as_view(),
        name="foyer_attribution",
    ),
    path(
        "residence_attribution/<convention_uuid>",
        views.ConventionResidenceAttributionView.as_view(),
        name="residence_attribution",
    ),
    path(
        "variantes/<convention_uuid>",
        views.ConventionFoyerVariantesView.as_view(),
        name="variantes",
    ),
    path(
        "commentaires/<convention_uuid>",
        views.ConventionCommentairesView.as_view(),
        name="commentaires",
    ),
    path(
        "avenant_commentaires/<convention_uuid>",
        views.AvenantCommentsView.as_view(),
        name="avenant_commentaires",
    ),
    path(
        "save/<convention_uuid>",
        views.save_convention,
        name="save",
    ),
    path(
        "delete/<convention_uuid>",
        views.delete_convention,
        name="delete",
    ),
    path(
        "feedback/<convention_uuid>",
        views.feedback_convention,
        name="feedback",
    ),
    path(
        "validate/<convention_uuid>",
        views.validate_convention,
        name="validate",
    ),
    path(
        "denonciation/<convention_uuid>",
        views.DenonciationView.as_view(),
        name="denonciation",
    ),
    path(
        "denonciation_start/<convention_uuid>",
        views.denonciation_start,
        name="denonciation_start",
    ),
    path(
        "denonciation_validate/<convention_uuid>",
        views.denonciation_validate,
        name="denonciation_validate",
    ),
    path(
        "resiliation/<convention_uuid>",
        views.ResiliationView.as_view(),
        name="resiliation",
    ),
    path(
        "resiliation_start/<convention_uuid>",
        views.resiliation_start,
        name="resiliation_start",
    ),
    path(
        "resiliation_acte/<convention_uuid>",
        views.ResiliationActeView.as_view(),
        name="resiliation_acte",
    ),
    path(
        "resiliation_creation/<convention_uuid>",
        views.ResiliationCreationView.as_view(),
        name="resiliation_creation",
    ),
    path(
        "resiliation_validate/<convention_uuid>",
        views.resiliation_validate,
        name="resiliation_validate",
    ),
    path(
        "generate/<convention_uuid>",
        views.generate_convention,
        name="generate",
    ),
    path(
        "load_xlsx_model/<file_type>",
        views.load_xlsx_model,
        name="load_xlsx_model",
    ),
    path(
        "sent/<convention_uuid>",
        views.sent,
        name="sent",
    ),
    path(
        "display_pdf/<convention_uuid>",
        views.display_pdf,
        name="display_pdf",
    ),
    path(
        "fiche_caf/<convention_uuid>",
        views.fiche_caf,
        name="fiche_caf",
    ),
    path(
        "new_avenant/<uuid:convention_uuid>",
        views.new_avenant,
        name="new_avenant",
    ),
    path(
        "remove_from_avenant/<uuid:convention_uuid>",
        views.remove_from_avenant,
        name="remove_from_avenant",
    ),
    path(
        "piece_jointe/<piece_jointe_uuid>",
        views.piece_jointe_access,
        name="piece_jointe",
    ),
    path(
        "piece_jointe/<piece_jointe_uuid>/promote",
        views.piece_jointe_promote,
        name="piece_jointe_promote",
    ),
    path(
        "new_avenant_start",
        TemplateView.as_view(
            template_name="conventions/avenant/new_avenant_start.html"
        ),
        name="new_avenant_start",
    ),
    path(
        "search_for_avenant",
        permission_required("convention.add_convention")(
            views.SearchForAvenantResultView.as_view()
        ),
        name="search_for_avenant",
    ),
    path(
        "new_avenants_for_avenant/<uuid:convention_uuid>",
        views.new_avenants_for_avenant,
        name="new_avenants_for_avenant",
    ),
    path(
        "form_avenants_for_avenant/<uuid:convention_uuid>",
        views.form_avenants_for_avenant,
        name="form_avenants_for_avenant",
    ),
    path(
        "avenant_champ_libre/<convention_uuid>",
        views.AvenantChampLibreView.as_view(),
        name="avenant_champ_libre",
    ),
    path(
        "expert_mode/<convention_uuid>",
        views.expert_mode,
        name="expert_mode",
    ),
]

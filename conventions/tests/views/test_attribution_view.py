from django.forms import model_to_dict
from django.test import TestCase
from django.urls import reverse

from conventions.tests.views.abstract import AbstractEditViewTestCase
from conventions.tests.fixtures import attribution_success_payload
from programmes.models import NatureLogement


class ConventionAttributionViewTests(AbstractEditViewTestCase, TestCase):
    def setUp(self):
        super().setUp()
        self.target_path = reverse(
            "conventions:attribution", args=[self.convention_75.uuid]
        )
        self.next_target_path = reverse(
            "conventions:comments", args=[self.convention_75.uuid]
        )
        self.convention_75.programme.nature_logement = NatureLogement.AUTRE
        self.convention_75.programme.save()
        self.target_template = "conventions/attribution.html"
        self.error_payload = {
            **attribution_success_payload,
            "attribution_reservation_prefectoral": "",
        }
        self.success_payload = attribution_success_payload
        self.msg_prefix = "[ConventionAttributionViewTests] "

    def _test_data_integrity(self):
        self.convention_75.refresh_from_db()
        self.assertEqual(
            self.convention_75.attribution_reservation_prefectoral,
            10,
            msg=f"{self.msg_prefix}",
        )

        self.assertDictEqual(
            model_to_dict(
                self.convention_75,
                fields=[
                    "attribution_agees_autonomie",
                    "attribution_agees_ephad",
                    "attribution_agees_desorientees",
                    "attribution_agees_petite_unite",
                    "attribution_agees_autre",
                    "attribution_agees_autre_detail",
                    "attribution_handicapes_foyer",
                    "attribution_handicapes_foyer_de_vie",
                    "attribution_handicapes_foyer_medicalise",
                    "attribution_handicapes_autre",
                    "attribution_handicapes_autre_detail",
                    "attribution_inclusif_conditions_specifiques",
                    "attribution_inclusif_conditions_admission",
                    "attribution_inclusif_modalites_attribution",
                    "attribution_inclusif_partenariats",
                    "attribution_inclusif_activites",
                    "attribution_modalites_reservations",
                    "attribution_modalites_choix_personnes",
                    "attribution_prestations_integrees",
                    "attribution_prestations_facultatives",
                    "attribution_reservation_prefectoral",
                ],
            ),
            {
                "attribution_agees_autonomie": False,
                "attribution_agees_ephad": False,
                "attribution_agees_desorientees": False,
                "attribution_agees_petite_unite": False,
                "attribution_agees_autre": True,
                "attribution_agees_autre_detail": "yo",
                "attribution_handicapes_foyer": False,
                "attribution_handicapes_foyer_de_vie": False,
                "attribution_handicapes_foyer_medicalise": False,
                "attribution_handicapes_autre": False,
                "attribution_handicapes_autre_detail": "",
                "attribution_inclusif_conditions_specifiques": "",
                "attribution_inclusif_conditions_admission": "",
                "attribution_inclusif_modalites_attribution": "",
                "attribution_inclusif_partenariats": "",
                "attribution_inclusif_activites": "",
                "attribution_modalites_reservations": "test",
                "attribution_modalites_choix_personnes": "Top !!!",
                "attribution_prestations_integrees": "OKOK",
                "attribution_prestations_facultatives": "",
                "attribution_reservation_prefectoral": 10,
            },
            msg=f"{self.msg_prefix}",
        )

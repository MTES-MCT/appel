from datetime import date

import factory
from faker import Faker

from bailleurs.models import Bailleur
from core.tests.factories import BaseFactory


class BailleurFactory(BaseFactory):
    class Meta:
        model = Bailleur
        django_get_or_create = ("siret",)

    nom = factory.Faker("company", locale="fr_FR")
    siret = factory.LazyFunction(lambda: Faker(locale="fr_FR").siret().replace(" ", ""))
    siren = factory.LazyAttribute(lambda o: o.siret[:9])

    capital_social = "123000.50"
    ville = "Marseille"
    signataire_nom = "Patrick Patoulachi"
    signataire_date_deliberation = date(2014, 10, 9)
    signataire_fonction = "PDG"
    signataire_bloc_signature = "Mon PDG"

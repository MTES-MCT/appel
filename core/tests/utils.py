import datetime
from bailleurs.models import Bailleur
from programmes.models import Programme

def create_bailleur():
    return Bailleur.objects.create(
        nom="3F",
        siret="12345678901234",
        capital_social="SA",
        ville="Marseille",
        dg_nom="Patrick Patoulachi",
        dg_fonction="PDG",
        dg_date_deliberation=datetime.date(2014, 10, 9),
    )

def create_programme(bailleur):
    return Programme.objects.create(
        nom="3F",
        bailleur = bailleur,
        code_postal = "75007",
        ville = "Paris",
        adresse = "22 rue segur",
        departement = 75,
        numero_galion = "12345",
        annee_gestion_programmation = 2018,
        zone_123 = 3,
        zone_abc = 'B1',
        surface_utile_totale = 5243.21,
        nb_locaux_commerciaux = 5,
        nb_bureaux = 25,
        autre_locaux_hors_convention = "quelques uns",
        vendeur = "identité du vendeur",
        acquereur = "identité de l'acquéreur",
        permis_construire = "123 456 789 ABC",
        date_achevement_previsible = datetime.date.today() + datetime.timedelta(days=365),
        date_achat = datetime.date.today() - datetime.timedelta(days=365),
        date_achevement = datetime.date.today() + datetime.timedelta(days=465),
    )

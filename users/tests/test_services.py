from django.test import TestCase

from bailleurs.models import Bailleur
from core.tests import utils_fixtures
from users.models import User
from users.services import UserService


class UserServiceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        utils_fixtures.create_all()

    def test_extract_username_from_email(self):
        username = UserService.extract_username_from_email("jeanne.bailleur@apilos.com")
        self.assertEqual(username, 'jeanne.bailleur')

        username = UserService.extract_username_from_email("jean.bailleur2@apilos.com")
        self.assertEqual(username, 'jean.bailleur2')

        username = UserService.extract_username_from_email("vélomoteur")
        self.assertEqual(username, '')

    def test_create_user_bailleur(self):
        bailleur = Bailleur.objects.get(nom='HLM')

        UserService.create_user_bailleur("Jeanne", "Bailleur", "jeanne.bailleur@apilos.com", bailleur, 'jeanne.bailleur')

        user = User.objects.get(email='jeanne.bailleur@apilos.com')
        self.assertEqual(user.first_name, "Jeanne")
        self.assertEqual(user.last_name, "Bailleur")
        self.assertTrue(user.is_bailleur(bailleur_id=bailleur.id))
        self.assertEqual(user.username, 'jeanne.bailleur')

        UserService.create_user_bailleur("Jean", "Bailleur", "jean.bailleur2@apilos.com", bailleur, 'jean.bailleur2')
        user = User.objects.get(email='jean.bailleur2@apilos.com')
        self.assertEqual(user.first_name, "Jean")
        self.assertEqual(user.last_name, "Bailleur")
        self.assertTrue(user.is_bailleur(bailleur_id=bailleur.id))
        self.assertEqual(user.username, 'jean.bailleur2')

        UserService.create_user_bailleur("Chantal", "Bailleur", "chantal.bailleur@apilos.com", bailleur, 'chantal.bailleur3')
        user = User.objects.get(email='chantal.bailleur@apilos.com')
        self.assertEqual(user.first_name, "Chantal")
        self.assertEqual(user.last_name, "Bailleur")
        self.assertTrue(user.is_bailleur(bailleur_id=bailleur.id))
        self.assertEqual(user.username, 'chantal.bailleur3')

import unittest
from CarteFidelite import CarteFidelite
from unittest.mock import MagicMock

class TestUnitaireCarteFidelite(unittest.TestCase):

    def setUp(self):
        self.carte= CarteFidelite() #instancie une carte fidelite vide pour le test


    def test_add_facture(self):

        facture_mock_1 = MagicMock()
        facture_mock_1.name= "Facture 1"
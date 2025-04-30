import unittest
from CarteFidelite import CarteFidelite
from unittest.mock import MagicMock

class TestUnitaireCarteFidelite(unittest.TestCase):

    def setUp(self):
        self.carte= CarteFidelite('Andy') #instancie une carte fidelite avec le nom Andy pour le test


    def test_add_facture(self):

        facture_mock_1 = MagicMock()
        facture_mock_1.name= "Facture 1"
        
        facture_mock_2 = MagicMock()
        facture_mock_2.name= "Facture 2"

        self.carte.ajouter_facture(facture_mock_1 )
        self.carte.ajouter_facture(facture_mock_2)
        
        self.assertEqual((self.carte.nb_factures()), 2) #le nombre de facture doit etre égale à 2 pour que le test réussi car j'ai insérer 2 factures

    
    def test_remettre_zero(self):
        facture_mock_1 = MagicMock()
        facture_mock_1.name= "Facture 1"
        
        facture_mock_2 = MagicMock()
        facture_mock_2.name= "Facture 2"

        facture_mock_3 = MagicMock()
        facture_mock_3.name= "Facture 3"
        
        facture_mock_4 = MagicMock()
        facture_mock_4.name= "Facture 4"

        self.carte.ajouter_facture(facture_mock_1 )
        self.carte.ajouter_facture(facture_mock_2)
        self.carte.ajouter_facture(facture_mock_3 )
        self.carte.ajouter_facture(facture_mock_4)

        self.assertEqual((self.carte.nb_factures()), 4) #Insérer 4 factures pour tester le remmetre à zero

        self.carte.remettre_a_zero() #remettre a 0 les factures
        self.assertEqual((self.carte.nb_factures()), 0)
    
    def test_niveau_fidelite(self):
        facture_mock_1 = MagicMock()
        facture_mock_1.name= "Facture 1"



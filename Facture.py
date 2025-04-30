from Fleur import Fleur

class Facture(Fleur):
    def __init__(self, nom_client, identifiant_facture, date_vente, fleur, prix_vente):
        if prix_vente < 0:
            raise ValueError("Le prix ne peut pas être négatif.")
        
        self.nom_client = nom_client
        self.identifiant_fleur = identifiant_facture
        self.date_vente = date_vente
        self.fleur = fleur
        self.prix_vente = prix_vente
from Fleur import Fleur

class Facture:
    def __init__(self, nom_client, identifiant_facture, date_vente, fleur:list[Fleur], prix_vente):
        if prix_vente < 0: ## le prix de vente ne peut pas etre négatif
            raise ValueError("Le prix ne peut pas être négatif.")
        
        self.nom_client = nom_client
        self.identifiant_fleur = identifiant_facture
        self.date_vente = date_vente
        self.fleur = fleur 
        self.prix_vente = prix_vente
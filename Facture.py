from Fleur import Fleur
from datetime import datetime

class Facture:
    def __init__(self, nom_client, identifiant_facture, date_vente, fleur:list[Fleur], prix_vente):
        
        if prix_vente < 0: ## le prix de vente ne peut pas etre négatif
            raise ValueError("Le prix ne peut pas être négatif.")
        
        self.nom_client = nom_client
        self.identifiant_fleur = identifiant_facture
        self.date_vente =  datetime.strptime(date_vente, "%Y-%m-%d")
        self.fleur = fleur 
        self.prix_vente = prix_vente
        
    def valider_date_vente(self):
        if self.date_vente < self.fleur.date_coupe:
         raise ValueError("La date de vente ne peut pas être antérieure à la date de coupe des fleurs.")
        

    def calculer_prix_total(self): #prix à payer pour le fleur
        """Calculer le prix total des fleurs + TVA de 20%."""
        somme_fleurs = sum(fleur.prix_fleur for fleur in self.fleur)
        tva = 0.20 * somme_fleurs
        prix_vente = somme_fleurs + tva
        return prix_vente
        
    
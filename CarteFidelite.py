from datetime import datetime

class CarteFidelite:
    def __init__(self, nom_client):
        self.nom_client = nom_client
        self.factures = []

    def ajouter_facture(self, facture): #aajouter une facture
        self.factures.append(facture)

    def nb_factures(self) -> int: #compter le nombre de factures insérer
        return len(self.factures)

    def remettre_a_zero(self): #remettre à zero l'historique des factures
        self.factures.clear()

    def niveau_fidelite(self) -> str: #niveau de fidelité des clients si client depense entre 2000 et 500 il est considéré commme Or
        total_depense = sum(f.total() for f in self.factures)
        if total_depense < 2000:
            return "Or"
        elif total_depense < 500:
            return "Argent"
        elif total_depense < 200:
            return "Bronze "
        else:
            return "Hors catégorie"

    def factures_dates_donn(self, date_debut: datetime, date_fin: datetime): #revoir l'ensemble des factures entre une période
        return [f for f in self.factures if date_debut <= f.date <= date_fin]

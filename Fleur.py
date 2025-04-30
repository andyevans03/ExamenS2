from datetime import datetime

class Fleur:
    def __init__(self, espece, identifiant_fleur, date_coupe, qualite_fleur, prix_fleur):
        
        self.espece = espece
        self.identifiant_fleur = identifiant_fleur
        self.date_coupe = datetime.strptime(date_coupe, "%Y-%m-%d")
        self.qualite_fleur = qualite_fleur
        self.prix_fleur = prix_fleur 
from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["Base_FloraDestock"]  # Remplace par le nom de ta base

# Exemple de données
fleurs = [
    {"espece": "Fleur1"},
]


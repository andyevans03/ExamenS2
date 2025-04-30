from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27018/")
db = client["Base_Dispo"]  # Remplace par le nom de ta base

# Exemple de données
fleurs = [
    {"espece": "Fleur2Dispo_standard"},
]
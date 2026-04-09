import pandas as pd

def charger_donnees(chemin_fichier):
    # Lecture du CSV (LON, LAT, PIR, CIR, SERVICE) [
    try:
        df = pd.read_csv(chemin_fichier)
        print(f" {len(df)} terminaux chargés.") #  87 989 
        return df
    except Exception as e:
        print(f" Erreur de chargement : {e}")
        return None
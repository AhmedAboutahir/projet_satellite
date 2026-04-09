import time
from src.core.data_loader import charger_donnees
from src.algorithms.algo_glutton_m1 import algo_glouton_m1

def run():
    # A. Charger
    df = charger_donnees('data/donnees.csv')
    
    # B. Lancer l'algo (Attention : ça peut prendre 2-3 minutes)
    print("Calcul des clusters en cours...")
    start_time = time.time()#timer

    resultats = algo_glouton_m1(df, cap_max=4000)
    
    end_time = time.time()
    duree = end_time - start_time
    
    # resultats
    print(f"Durée d'execution :{duree:.2f} secondes")
    print(f"Nombre de clusters trouvés : {len(resultats)}")

if __name__ == "__main__":
    run()
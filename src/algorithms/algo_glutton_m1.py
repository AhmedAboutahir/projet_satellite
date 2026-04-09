from src.core.geometry import verifier_distance 

def algo_glouton_m1(terminaux, cap_max=4000):
    clusters = [] #liste des clusters

    for _, t in terminaux.iterrows():
        point_assigne = False
        
        #on essaie de mettre le terminal courant dans un cluster existant
        for c in clusters:
            dist_ok = verifier_distance((t['LAT'], t['LON']), c['centre'])
            debit_ok = (c['debit_total'] + t['PIR']) <= cap_max
            
            if dist_ok and debit_ok:
                c['membres'].append(t)
                c['debit_total'] += t['PIR'] #debit total du cluster est la somme des debits des terminaux
                point_assigne = True
                break #  trouvé  passe au terminal suivant
        
        #si aucune place n'est trouvée, on crée un nouveau cluster
        if not point_assigne:
            nouveau_cluster = {
                'centre': (t['LAT'], t['LON']),
                'debit_total': t['PIR'],
                'membres': [t]
            }
            clusters.append(nouveau_cluster)
            
    return clusters
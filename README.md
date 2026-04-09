
📡 Clustering de Terminaux - Constellation de Satellites LEO
📌 Présentation du Projet
Ce projet s'inscrit dans le cadre du Projet d'Intégration Réseaux (PIR) 2025-2026 de l’ENSEEIHT.
L'objectif est de concevoir et d'implémenter des algorithmes de clustering permettant de regrouper des terminaux utilisateurs au sol afin de les desservir via les faisceaux d’une constellation de satellites en orbite basse (LEO).
Le principal défi consiste à minimiser le nombre de clusters (faisceaux) tout en respectant des contraintes géographiques et de capacité.

📊 Données d'Entrée
Le jeu de données contient 87 989 terminaux.
Chaque terminal est caractérisé par :
Sa position géographique (longitude, latitude)
Son besoin en débit (PIR / CIR)

⚙️ Contraintes du Problème
Un cluster est valide uniquement s’il respecte les conditions suivantes :
Contrainte géométrique
Diamètre maximal : 90 km
Rayon maximal : 45 km autour du centre du cluster
Contrainte de capacité
La somme des débits PIR des terminaux d’un cluster ne doit pas dépasser la capacité du faisceau
Exemple : 4 Gbps
Couverture complète
Tous les terminaux doivent être assignés à un cluster
Aucun terminal ne doit rester non attribué

🚀 Algorithmes Implémentés
🔹 Méthode 1 : Greedy (glouton)
Construction progressive des clusters
Simple et rapide, mais pas toujours optimal
🔹 Méthode 2 : Greedy par capacité maximale
Priorise les zones à forte densité
Cherche à maximiser l’utilisation de la capacité des clusters
🔹 Post-traitement : Fusion de clusters
Fusion de clusters compatibles ("2 en 1")
Permet de réduire le nombre total de faisceaux
🔹 Optimisation : Découpage en zones connexes
Partition du problème en sous-zones indépendantes
Accélération des calculs (gain jusqu’à x70)

🛠️ Installation et Utilisation
Cloner le dépôt :
git clone https://github.com/AhmedAboutahir/projet_satellite.git




from haversine import haversine, Unit

def verifier_distance(pos1, pos2):
    """
    pos1 et pos2 sont des tuples (lat, lon).
    Retourne True si la distance est <= 45 km.
    """
    dist = haversine(pos1, pos2, unit=Unit.KILOMETERS) #distance de haversine en fct de longitude et latitude
    return dist <= 45 # contrainte du sujet 
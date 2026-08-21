"""Module contenant la classe Capteur."""

import random


class Capteur:
    """Représente un capteur IoT générique (ici : niveau de nourriture restante)."""

    def __init__(self, nom, unite, valeur_min, valeur_max):
        self.nom = nom
        self.unite = unite
        self.valeur_min = valeur_min
        self.valeur_max = valeur_max
        self.historique = []

    def lire(self):
        """Simule une lecture de capteur (valeur aléatoire dans la plage)."""
        valeur = round(random.uniform(self.valeur_min, self.valeur_max), 1)
        self.historique.append(valeur)
        return valeur

    def moyenne(self):
        """Calcule la moyenne des valeurs lues jusqu'à présent."""
        if not self.historique:
            return None
        return sum(self.historique) / len(self.historique)

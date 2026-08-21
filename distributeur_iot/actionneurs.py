"""Module contenant la classe Actionneur."""


class Actionneur:
    """Représente un actionneur (ici : le moteur qui distribue la nourriture)."""

    def __init__(self, nom):
        self.nom = nom
        self.actif = False

    def activer(self):
        self.actif = True
        print(f"[{self.nom}] activé — distribution en cours")

    def desactiver(self):
        self.actif = False
        print(f"[{self.nom}] désactivé")

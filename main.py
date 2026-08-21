"""Point d'entrée : lance la simulation du distributeur de nourriture."""

import time
from distributeur_iot.actionneurs import Actionneur
from distributeur_iot.capteurs import Capteur
from distributeur_iot.distributeur import DistributeurIntelligent

SEUIL_BAS = 20
HEURE_MATIN = "08:00"
HEURE_MIDI = "12:00"
HEURE_SOIR = "18:00"
HEURE_NUIT = "22:00"


def main():
    distributeur = DistributeurIntelligent("Distributeur Rex")

    capteur_niveau = Capteur("niveau_nourriture", "%", 5, 100)
    distributeur.ajouter_capteur(capteur_niveau)

    moteur = Actionneur("moteur")
    distributeur.ajouter_actionneur(moteur)

    heures_repas = [HEURE_MATIN, HEURE_SOIR]
    heures_simulees = [HEURE_MATIN, HEURE_MIDI, HEURE_SOIR, HEURE_NUIT]

    for h in heures_simulees:
        distributeur.rapport()
        distributeur.verifier_distribution(h, heures_repas, seuil_minimum=SEUIL_BAS)
        time.sleep(0.5)


if __name__ == "__main__":
    main()

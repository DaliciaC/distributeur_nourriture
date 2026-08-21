from datetime import datetime

"""Module contenant la classe DistributeurIntelligent."""

class DistributeurIntelligent:
    """Orchestre le capteur et l'actionneur d'un distributeur de nourriture simulé."""


    
    def __init__(self,nom):

        
        self.nom=nom
        self.capteurs=[]
        self.actionneurs    =     []

    def ajouter_capteur(self, capteur):
        self.capteurs.append(capteur)
    def ajouter_actionneur(self,actionneur):
        self.actionneurs.append(actionneur)

    def verifier_distribution(self, heure_actuelle, heures_repas, seuil_minimum):
        """
        Distribue une portion si c'est l'heure du repas ET qu'il reste
        assez de nourriture dans le réservoir.
        """
        for capteur in self.capteurs:
            if not capteur.historique:                continue
            derniere_valeur=capteur.historique[-1]

            
            if capteur.nom=="niveau_nourriture" and heure_actuelle in heures_repas:
                if derniere_valeur>seuil_minimum:
                    
                    for actionneur in self.actionneurs:
                        if actionneur.nom=="moteur":actionneur.activer()







    
    def  rapport(self) :
        heure = datetime.now().strftime("%H:%M:%S")
        print(f"\n--- Rapport de {self.nom} ({heure}) ---")
        for capteur in self.capteurs:
            print(f"{capteur.nom} : {capteur.lire()} {capteur.unite}")

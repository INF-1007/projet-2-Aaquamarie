# auto.py
# auto.py
from vehicule import Vehicule
from specifications import AutoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Auto(Vehicule):

    def __init__(self, nom, position_dep, image_path):
        auto_roues = [Roue(AutoSpecs.roue_nom, AutoSpecs.roue_poids, AutoSpecs.roue_friction, AutoSpecs.roue_support),
                      Roue(AutoSpecs.roue_nom, AutoSpecs.roue_poids, AutoSpecs.roue_friction, AutoSpecs.roue_support),
                      Roue(AutoSpecs.roue_nom, AutoSpecs.roue_poids, AutoSpecs.roue_friction, AutoSpecs.roue_support),
                      Roue(AutoSpecs.roue_nom, AutoSpecs.roue_poids, AutoSpecs.roue_friction, AutoSpecs.roue_support)]
        auto_moteur = Moteur(AutoSpecs.moteur_nom, AutoSpecs.moteur_poids,AutoSpecs.moteur_acceleration)
        auto_chassis = Chassis(AutoSpecs.chassis_nom, AutoSpecs.chassis_poids, AutoSpecs.chassis_aire, AutoSpecs.chassis_trainee)

        super().__init__(nom, position_dep, auto_roues, auto_moteur, auto_chassis, AutoSpecs, image_path)
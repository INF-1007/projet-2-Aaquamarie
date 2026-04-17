from vehicule import Vehicule
from roue import Roue
from moteur import Moteur
from chassis import Chassis
from specifications import CamionSpecs

class Camion(Vehicule): 
    
    def __init__(self, nom, position_dep, image_path):
        camion_roues = [Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support),
                        Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support),
                        Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support),
                        Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support),
                        Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support),
                        Roue(CamionSpecs.roue_nom, CamionSpecs.roue_poids, CamionSpecs.roue_friction, CamionSpecs.roue_support)]
        camion_moteur = Moteur(CamionSpecs.moteur_nom, CamionSpecs.moteur_poids, CamionSpecs.moteur_acceleration)
        camion_chassis = Chassis(CamionSpecs.chassis_nom, CamionSpecs.chassis_poids, CamionSpecs.chassis_aire, CamionSpecs.chassis_trainee)
        super().__init__(nom, position_dep, camion_roues, camion_moteur, camion_chassis, CamionSpecs, image_path)
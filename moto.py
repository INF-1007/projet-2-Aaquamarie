# moto.py
from vehicule import Vehicule
from specifications import MotoSpecs
from roue import Roue
from moteur import Moteur
from chassis import Chassis

class Moto(Vehicule):

    def __init__(self, nom, position_dep, image_path):
        moto_roues = [Roue(MotoSpecs.roue_nom, MotoSpecs.roue_poids, MotoSpecs.roue_friction, MotoSpecs.roue_support),
                 Roue(MotoSpecs.roue_nom, MotoSpecs.roue_poids, MotoSpecs.roue_friction, MotoSpecs.roue_support),]
        moto_moteur = Moteur(MotoSpecs.moteur_nom, MotoSpecs.moteur_poids, MotoSpecs.moteur_acceleration)
        moto_chassis = Chassis(MotoSpecs.chassis_nom, MotoSpecs.chassis_poids, MotoSpecs.chassis_aire, MotoSpecs.chassis_trainee)

        super().__init__(nom, position_dep, moto_roues, moto_moteur, moto_chassis, MotoSpecs, image_path)
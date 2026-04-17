from composante import Composante

class Roue(Composante):

    def __init__(self, nom, poids, coefficient_friction, poids_supporte):
        super().__init__(nom, poids)
        self.__coefficient_friction = coefficient_friction
        self.__poids_supporte = poids_supporte

    def get_coefficient_friction(self):
        return self.__coefficient_friction
    
    def get_poids_supporte(self):
        return self.__poids_supporte
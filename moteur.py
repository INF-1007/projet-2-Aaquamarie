from composante import Composante

class Moteur(Composante):

    def __init__(self, nom, poids, acceleration):
        super().__init__(nom, poids)
        self.__acceleration = acceleration

    def get_acceleration(self):
        return self.__acceleration
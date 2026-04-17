class Composante:
    
    def __init__(self, nom, poids):
        self.__nom = nom
        self.__poids = poids

    def get_nom(self):
        return self.__nom
    
    def get_poids(self):
        return self.__poids
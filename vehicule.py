import numpy as np
import pygame
from specifications import DENSITE_AIR

# TODO : Créer la classe Vehicule

class Vehicule:
    
    # TODO : Créer le constructeur 
    def __init__(self, nom, position_dep, roues, moteur, chassis, Specs, image_path):

        # TODO : ajouter les attributs
        self.__nom = nom
        self.__position = np.array(position_dep, dtype=float)
        self.__vitesse = np.array([0.0, 0.0])
        self.__roues = roues
        self.__moteur = moteur
        self.__chassis = chassis
        self.__poids_total = self.calculer_poids_total()

        # TODO : ajouter un attribut pour l'image du véhicule
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (Specs.image_width, Specs.image_height))
        self.width = Specs.image_width
        self.height = Specs.image_height
    
    def get_position(self):
        return self.__position
    
    def affichage_vehicule(self, screen):
        screen.blit(self.image, (self.__position[0] - self.width, self.__position[1]))
    
    def calculer_poids_total(self):
        weight = self.__moteur.get_poids() + self.__chassis.get_poids()

        for wheel in self.__roues:
            weight += wheel.get_poids()
        return weight
    
    def calculer_traction(self):
        traction = self.__poids_total * self.__moteur.get_acceleration()
        return traction
    
    def calculer_friction(self):
        friction = 0
        for wheel in self.__roues:
            friction += wheel.get_coefficient_friction() * self.__vitesse
        return friction

    def calculer_trainee(self):
        trainee = 1/2 * self.__chassis.get_coefficient_trainee() * self.__chassis.get_aire_frontale() * DENSITE_AIR * self.__vitesse**2
        return trainee

    def accelerer(self, dt):
        acceleration = (self.calculer_traction() - self.calculer_trainee() - self.calculer_friction())/self.__poids_total
        self.__vitesse[0] += acceleration[0]*dt
        self.__position[0] += self.__vitesse[0]*dt


    def celebrer(self):
        return f"{self.__nom} remporte la course !"
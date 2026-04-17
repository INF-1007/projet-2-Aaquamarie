import random
import pygame

class Confetti: 
    
    def __init__(self, screenwidth):
        self.x = random.randint(0, screenwidth)
        self.y = 0

        self.width = random.randint(5, 20)
        self.height = self.width

        self.speed = random.randint(50,100)

        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def fall(self, dt):
        self.y += self.speed * dt

    def display(self, screen):
        self.image = pygame.draw.rect(screen, self.color, (self.x, self.y - self.height, self.width, self.height))

    def get_y(self):
        return self.y

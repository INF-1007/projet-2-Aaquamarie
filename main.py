import pygame
from moto import Moto
from auto import Auto
from camion import Camion
from confettis import Confetti
from config import WIDTH, HEIGHT, START_LINE_X, FINISH_LINE_X, START_MOTO_Y, START_AUTO_Y, START_CAMION_Y 


def main():
    
    confettis = []

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Simulation de course")

    background = pygame.image.load("projet-2-Aaquamarie\\images\\background.png").convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 24)

    # TODO : Créer une liste de véhicules qui contient une instance pour chaque
    # type de véhicule : une moto, une auto et un camion
    vehicules = [Auto("Auto", (START_LINE_X, START_AUTO_Y), "projet-2-Aaquamarie\\images\\auto.png"), 
                 Moto("Moto", (START_LINE_X, START_MOTO_Y), "projet-2-Aaquamarie\\images\\moto.png"), 
                 Camion("Camion", (START_LINE_X, START_CAMION_Y), "projet-2-Aaquamarie\\images\\camion.png")]

    running = True
    course_commencee = False
    gagnant = None

    while running:

        screen.blit(background, (0, 0))

        dt = clock.tick(60) / 1000

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    course_commencee = True


        if course_commencee:
            for vehicule in vehicules:
                vehicule.accelerer(dt)
                if vehicule.get_position()[0] >= FINISH_LINE_X and gagnant is None:
                    gagnant = vehicule

        # TODO : Pour chaque véhicule, appeler la méthode `affichage_vehicule`
        for vehicule in vehicules:
            vehicule.affichage_vehicule(screen)

        if not course_commencee and gagnant is None:
            txt = font.render("Appuyez sur ESPACE pour démarrer",
                              True, (0, 0, 0))
            screen.blit(txt, (350, 35))

        if gagnant:
            txt = font.render(gagnant.celebrer(), True, (0, 0, 0))
            screen.blit(txt, (350, 35))
            confettis.append(Confetti(WIDTH))
            for con in confettis:
                con.display(screen)
                con.fall(dt)
                if con.get_y() > HEIGHT:
                    confettis.remove(con)

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
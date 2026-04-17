# Moto
class MotoSpecs:
    # Roues
    roue_nom = "moto_wheel"
    roue_poids = 6
    roue_friction = 0.01
    roue_support = 300

    # Moteur
    moteur_nom = "moto_engine"
    moteur_poids = 200
    moteur_acceleration = 35

    # Châssis
    chassis_nom = "moto_frame"
    chassis_poids = 200
    chassis_aire = 0.6
    chassis_trainee = 0.1

    # Image
    image_width = 40
    image_height = 30


# Auto
class AutoSpecs:
    roue_nom = "car_wheel"
    roue_poids = 10
    roue_friction = 0.008
    roue_support = 500

    moteur_nom = "car_engine"
    moteur_poids = 300
    moteur_acceleration = 25

    chassis_nom = "car_frame"
    chassis_poids = 900
    chassis_aire = 1.0
    chassis_trainee = 0.2

    # Image
    image_width = 80
    image_height = 35


# Camion
class CamionSpecs:
    roue_nom = "truck_wheel"
    roue_poids = 15
    roue_friction = 0.012
    roue_support = 800

    moteur_nom = "truck_engine"
    moteur_poids = 600
    moteur_acceleration = 15

    chassis_nom = "truck_frame"
    chassis_poids = 3000
    chassis_aire = 2.0
    chassis_trainee = 0.5

    # Image
    image_width = 160
    image_height = 60

# Autres variables
DENSITE_AIR = 1.2
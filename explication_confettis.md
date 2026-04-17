Pour la classe Confetti, j'ai utilisé le même fonctionnement que la classe véhicule. J'assigne au confetti une position X random dans l'écran en utilisant SCREENWIDTH comme int max, et j'assigne 0 pour la position y.
Ensuite, je définis la taille du confetti avec un int aléatoire pour sa largeur, et j'assigne à sa hauteur la même valeur.
De même pour la vitesse, je lui assigne un int aléatoire en tant que vitesse.
Ensuite, pour la couleur, j'assigne un int aléatoire entre 0 et 255 3 fois (R G et B) (j'aurais aussi pu ajouter un facteur d'opacité aléatoire).
Avec tous les attributs prêts, je définis la méthode d'affichage et la méthode de mouvement (display(screen) et fall(dt)):
- Pour fall(dt), j'update la position du confetti l'incrémentant d'un facteur vitesse mulitpliée par le dt (même fonctionnement que pour le déplacement des véhicules)
- Pour display(screen), j'utilise la fonction pygame.draw.rect pour dessiner un rectangle en utilisant les attributs définis au niveau __init__ et rédessine le rectangle à chaque frame en utilisant la position updatée grâce à fall(dt)
- J'ai aussi ajouté un getter pour la position y pour pouvoir retirer les confettis de la liste de confettis dans main() lorsqu'ils sortent de l'écran

En faisant des recherches, je sais que j'aurais pu déplacer les rectangles à la place de les redessiner (ce qui sauve probablement de la RAM) mais pour un logiciel aussi simple, j'ai trouvé qu'il n'y avait pas besoin de se concentrer sur l'optimisation

Enfin, pour la taille des confettis et leur vitesse, j'ai simplement donné des grandes valeurs maximales pour un effet plus chaotique et festif (préférence personelle)
De même pour la fréquence d'apparition, j'ai considéré la limiter en settant frame = 0 au début de main(), l'incrémentant de 1 à chaque frame et utiliser un if frame%5 == 0 pour changer la fréquence, mais je préfère le fonctionnement illimité actuel

Pour l'appel des fonctions, j'ai créé une liste de confettis vide au début de main(). Lorsqu'un véhicule gagne la course, après l'affichage du message de célébration, j'appelle la fonction display pour dessiner les confettis, et puis la fonction fall() pour
les faire tomber. Avec confetti.get_y(), je vérifie si ils sont en dehors de l'écran, et, si oui, je les retire de la liste.
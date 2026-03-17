[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ineitDj-)
# :checkered_flag: Projet 2 – Simulateur de course :checkered_flag: 

##  Introduction
Dans ce projet, vous aurez comme tâche de développer un simulateur de course entre différents véhicules (auto, camion et moto) en utilisant la programmation orientée objet (POO). 

L’objectif est de construire votre application par étapes. À la fin du projet, vous aurez :
- Modélisé des objets
- Utilisé l’héritage et la composition
- Implémenté une simulation physique simple
- Intégré vos classes dans une interface graphique interactive

> [!Important]
> Les parties 1 et 2 ne produisent aucun affichage visible (à part l'arrière-plan du simulateur de course avec pygame).
> 
> Les véhicules apparaîtront à l’écran uniquement à partir de la Partie 3.

## Structure du projet
```
│
├── main.py                       # Contient l'interface graphique du simulateur de course ainsi que la boucle principale        
├── composante.py                 # Contiendra la classe Composante
├── moteur.py                     # Contiendra la classe Moteur, qui hérite de la classe Composante
├── chassis.py                    # Contiendra la classe Chassis, qui hérite de la classe Composante
├── roue.py                       # Contiendra la classe Roue, qui hérite de la classe Composante 
├── vehicule.py                   # Contiendra la classe Vehicule 
├── auto.py                       # Contiendra la classe Auto, qui hérite de la classe Vehicule 
├── moto.py                       # Contiendra la classe Moto, qui hérite de la classe Vehicule
├── camion.py                     # Contiendra la classe Camion, qui hérite de la classe Vehicule
├── specifications.py             # Contient les spécifications propre à chaque type de véhicule
├── config.py                     # Contient des variables pour la simulation
├── confettis.py                  # Contiendra la classe Confetti
└── explication_confettis.py      # Contiendra votre explication sur votre implémentation des confettis
```
> [!Important]
> - Vous ne devez pas modifier la structure du projet.
> - `main.py` contient déjà l'interface graphique du simulateur de course ainsi que la boucle principale.

# 🛞🔧⚙️ Partie 1 : Les composantes des véhicules

## Objectif : 
Dans cette première partie, vous aurez comme objectif de créer les classes suivantes :
- `Composante`
- `Moteur`
- `Chassis`
- `Roue`

## La classe `Composante`

La classe `Composante` permet d'instancier une composante d'un véhicule (par exemple, un moteur, un chassis, etc.). En d'autres mots, ce sera la classe "Parent" des classes `Moteur`, `Chassis` et `Roue` que vous compléterez par la suite.

Dans le fichier `composante.py`, vous devez créer la classe `Composante` afin qu'elle contienne les attributs suivants, **en privé** : 
- `nom`
- `poids`

## La classe `Moteur`

À l'intérieur du fichier `moteur.py` , vous devez créer une classe `Moteur`. Cette classe **doit hériter de la classe `Composante`**. Elle doit contenir comme  attributs **privé** supplémentaire: 
- `acceleration`

## La classe `Chassis`

à l'intérieur du fichier `chassis.py`, crééez maintenant la classe `Chassis`. Cette classe doit également **hériter de la classe `Composante`**, et doit contenir les attributs **privés** supplémentaires suivants: 
- `aire_frontale`
- `coefficient_trainee`

## La classe `Roue`

Finalement, nous avons la classe `Roue`, une autre classe fille de la classe `Composante`. 

Vous devez créer la classe `Roue` dans le fichier `roue.py`. Cette classe doit contenir les attributs **privés** supplémentaires suivants: 
- `coefficient_friction`
- `poids_supporte`

# 🚘 Partie 2 : La classe Vehicule et les types de véhicules spécialisés

Dans cette deuxième partie du projet, vous aurez comme objectif de compléter les classes suivantes : 
- `Vehicule`
- `Moto`
- `Auto`
- `Camion`

## La classe `Vehicule`

À l'intérieur du fichier `vehicule.py`, vous devez créer une classe qui s'appelle `Vehicule`. 

Cette classe doit contenir les attributs **privés** suivants: 
- `nom`
- `position`: un numpy array avec format [x, y]
- `vitesse` : un numpy array avec format [0, 0]
- `roues`
- `moteur`
- `chassis`
- `poids_total`: la somme du poids des composantes

## Les classes `Moto`, `Auto` et `Camion`

Maintenant, vous devrez créer les classes `Moto`, `Auto` et `Camion`, à l'intérieur des fichiers `moto.py`, `auto.py` et `camion.py`.

### Consignes à suivre:

- Ces classes doivent hériter de la classe `Vehicule`
- À l'intérieur du constructeur de chaque classe, vous devez ajouter les composantes (les roues, le moteur et le chassis). Pour ce faire, vous devrez créer des instances des classes `Roue`, `Moteur` et `Chassis` complétées à la partie 1.
    - Vous devez définir le nombre de roues sachant que:
        - **Une moto** possède **2 roues**
        - **Une auto** possède **4 roues**
        - **Un camion** possède **6 roues**
    - Vous devez utiliser les spécifications des composantes du fichier `specifications` 

- N'oubliez pas d'appeler le constructeur parent avec `super()`

# 🏍️ 🚗 🚛 Partie 3 : Création de véhicules pour la course

Maintenant que les classes sont créees, vous pouvez maintenant créer des instances de véhicules qui seront utilisés dans la course!

> [!Note]
> - Après avoir complété cette partie, vous devriez voir apparaître sur la ligne de départ les voitures dans l'interface pygame lorsque vous exécutez le `main.py`. 

## Gestion de l'image du véhicule dans le constructeur de `Vehicule`
À l'intérieur du constructeur de vous devez ajouter un attribut `self.image`, qui permet de charger l'image du véhicule (avec `pygame.image.load`) et son redimensionnement (avec `pygame.transform.scale`). Pour le redimensionnement, vous devez faire référence aux spécifications (`Specs`). 

## Ajout d'une méthode `affichage_vehicule()` dans `Vehicule`

Le premier objectif de cette troisième partie du projet est de compléter la méthode `images_vehicule()` à l'intérieur de la classe `Vehicule`. 

```
def affichage_vehicule(self, screen):
```

Cette méthode doit : 
- Prendre l’écran Pygame (screen) comme argument.
- Utiliser la position du véhicule (self.position) pour déterminer où afficher l’image à l’écran.
- Afficher l’image du véhicule (self.image) correctement à sa position.
- Vous pouvez choisir l’alignement de l’image : par exemple, l’image peut être alignée à droite par rapport à la position du véhicule pour que le départ soit correct sur la ligne.
- Veiller à ce que l’image soit correctement dimensionnée selon les attributs de la classe (self.taille_image).
- La méthode ne doit pas créer de nouvelles images à chaque frame, elle doit simplement blitter l’image existante sur l’écran.

> [!Note]
> Cette méthode sera appelée à chaque frame dans la boucle principale pour mettre à jour la position du véhicule.

## Instanciation des véhicules de course dans `main.py`

Par la suite, dans le fichier `main.py` , vous devrez créer la liste des véhicules qui feront la course. On veut y ajouter une moto, un camion et une auto.

Cette **liste** de véhicules devra contenir:
- Une instance de la classe `Moto` 
- Une instance de la classe `Auto`
- Une instance de la classe `Camion`
 
Les voitures devront être placées à la ligne de départ. Pour ce faire, utilisez les distances suivantes contenues dans le fichier `config.py` pour créer les instances: 
- La position en x : `START_LINE_X`
- La position en y de la moto : `START_MOTO_Y`
- La position et y de l'auto : `START_AUTO_Y`
- La position en y du camion : `START_CAMION_Y`

# ➡️💨 Partie 4 : Calculs physiques des véhicules

Maintenant que les véhicules sont placés sur ligne de départ, vous allez ajouter quelques calculs physiques qui permettront de gérer le déplacement des voitures lors de la course.

à l'intérieur de la classe `Vehicule`, vous devrez implémenter les calculs ci-dessous à l'intérieur des méthodes suivantes: 

### Traction
À l'intérieur de la méthode `calculer_traction`, la traction correspond à : 
```
poids_total * acceleration_moteur
```

### Traînée
À l'intérieur de la méthode `calculer_trainee`, la trainée correspond à : 
```
1/2 * coefficient_trainee * aire_frontale * densite_air * vitesse^2
```
Densité de l’air = 1.2 kg/m³

### Friction
À l'intérieur de la méthode `calculer_friction`, la friction correspond à la somme des :
```
coefficient_friction * vitesse
```

### Accélération

Par la suite, vous allez maintenant compléter la méthode `accelerer`. Cette méthode doit mettre à jour la vitesse et la position du véhicule pendant un intervalle de temps dt, en utilisant les forces qui s’appliquent sur lui.

```
def accelerer(self, dt):
```
```
acceleration = (traction - trainee - friction) / poids_total
vitesse += acceleration * dt
position += vitesse * dt
```

# :checkered_flag: :checkered_flag: Partie 5 : Simulation de la course

Dans cette partie, vous allez simuler la course en ajoutant certaines fonctionnalités permettant d'abord de déclencher le départ de la course, puis la fin de la course. 

## Le départ de la course

### Déclenchement de la course

Afin de déclencher la course, vous devez implémenter les fonctionnalités suivantes dans `main.py`:

- Si la course est commencée (`course_commencee = True`): 
    - Pour chacun des véhicules dans la course, appeler la méthode `accelerer`

## Gagnant de la course et message de célébration 

- Dans la classe `Vehicule` devez compléter la méthode `celebrer`, qui permettra de gérer l'affichage d'un message qui annoncera le véhicule qui a gagné la course. La classe doit retourner le 
message suivant : 
```
return f"{self.nom} remporte la course !"
```

- Dans le fichier `main.py`: 
    - Si un véhicule franchit la ligne d'arrivée (`FINISH_LINE_X`) **et qu'on a pas déjà un gagnant**, on le note comme étant le gagnant avec la méthode `gagnant`
    - Si on a un gagnant, on veut afficher le message de célébration en appelant la méthode `celebrer()` du véhicule qui a gagné. Pour ce faire, vous pouvez utiliser `font.render` : 

    ```
    txt = font.render(gagnant.celebrer(), True, (0, 0, 0))
    screen.blit(txt, (350, 35))
    ```

# 🎉🎊 Partie 6 : Confettis

Pour célébrer la victoire du véhicule qui a gagné la course, vous allez ajouter des confettis animés qui tombent du haut vers le bas de l'écran. 

Dans cet exercice, nous vous laissons une liberté créative, mais certaines contraintes doivent être respectées :

### Fichier et classe :
- Complétez la classe `Confetti` à l'intérieur du fichier `confettis.py`, qui permettra de gérer les propriétés et le comportement d’un confetti.

### Couleurs :
- Les confettis doivent être de différentes couleurs (vous choisissez combien).

### Vitesse :
- Les confettis doivent tomber à différentes vitesses

### Position initiale :
- Les confettis doivent apparaître à différentes positions x en haut de l’écran

### Taille et forme : 
- Les confettis doivent être carrés.
- La taille des confettis doit varier 

### Affichage :
- Les confettis apparaissent au moment où le premier véhicule franchit la ligne d’arrivée, en même temps que le message de célébration.
- Une fois apparus, les confettis se déplacent vers le bas à chaque frame et disparaissent lorsqu’ils sortent de l’écran.

### Autres consignes à respecter : 
- Vous êtes responsable de décider où et comment intégrer l’affichage des confettis dans les autres fichiers du projet pour qu’ils apparaissent correctement pendant la course.
- L’implémentation exacte est à votre discrétion : vous devez créer et gérer les confettis de manière cohérente avec le reste du projet et leur animation doit suivre les règles définies dans cette partie.
- Vous devez documenter vos choix et votre démarche dans le fichier `explication_confettis.md`. Ce document doit expliquer comment vous avez intégré les confettis dans le projet, les choix techniques pour l’animation, la gestion des couleurs, tailles et vitesses, et comment vous avez coordonné l’apparition des confettis avec la fin de la course.

# Barème de correction

| Partie | Critères détaillés | Points |
|--------|------------------|--------|
| **Partie 1 – Composantes** | - Classe `Composante` correctement implémentée : 1 pt<br>- Classes `Moteur`, `Chassis`, `Roue` correctement implémentées (3 pt)<br> | 4 |
| **Partie 2 – Classe Vehicule et types spécialisés** | - Classe `Vehicule` avec attributs et méthode de base (1 pt) <br>- Classes `Moto`, `Auto`, `Camion` créent les composantes et appellent `super()`, avec le bon nombre de roues et composition correcte (3 pts) <br> | 4 |
| **Partie 3 – Affichage des véhicules** | - Méthode `affichage_vehicule()` correctement implémentée (2 pt) <br>- Instanciation des véhicules de course dans main.py (1 pt) | 3 |
| **Partie 4 – Calculs physiques** | - Méthode `accelerer()` implémente traction, friction et traînée : 2 pt<br>- Accélération et mise à jour de `vitesse` et `position` (1 pt) <br> | 3 |
| **Partie 5 – Simulation de la course**  | - Départ de la course (1 pt) <br>- Message de célébration pour le gagnant de la course (1 pt) | 2 |
| **Partie 6 – Confettis** | - Affichage des confettis correctement implémentée avec respect des contraintes (2 pt) <br>- Documentation dans `explication_confettis.md` expliquant l’implémentation et les choix (1 pt) | 3 |

---






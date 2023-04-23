# IMPORT SECTION

import pygame
import pygame.display
import pygame.event
import pygame.key
import pygame.time
import pygame.sprite
import pygame.draw
import pygame.font
import pygame.image
import pygame.transform
import pygame.mixer
import pygame.mouse
import pygame.math
import pygame.rect
from random import randint

# INIT SECTION

pygame.font.init()

# VARIABLES SECTION

ALVEOLE_SPRITES = {"blue" : "alveole_bleue.png", "yellow" : "alveole_jaune.png", "orange" : "alveole_orange.png", "red" : "alveole_rouge.png", "green" : "alveole_verte.png"}
ALVEOLE_COLORS = ["blue", "green", "yellow", "orange", "red"]
USED_COLORS = ["green", "yellow"]
ALVEOLE_SIDE =  300

MOVE_SPEED = 3
SPEED_CAM = MOVE_SPEED*10

font = pygame.font.SysFont("Impact", 36)

# FUNCTIONS SECTION

operateurs = ["+", "-" , "x", ":"]

def random_basic_calculation():
    """Renvoi un couple de la forme ("calcul", resultat) généré aléatoirement"""
    indice_operator = randint(0, len(operateurs)-1)
    operator = operateurs[indice_operator]
    if operator == "+" or operator == "-":
        first_number = randint(1, 100)
        second_number = randint(1, 100)
    elif operator == "x":
        first_number = randint(1, 10)
        second_number = randint(1, 10)
    else:
        first_number = randint(1, 10)
        second_number = randint(1, 10)
        reponse = first_number * second_number
    if operator == "+":
        resultat = first_number + second_number
    elif operator == "-":
        if first_number < second_number:
            first_number, second_number = second_number, first_number
        resultat = first_number - second_number
    elif operator == "x":
        resultat = first_number * second_number
    if operator != ":":
        return (f"{first_number} {operator} {second_number}", resultat)
    else:
        return(f"{reponse} : {second_number}", first_number)
    
def topright_side_coordinates(n, couple_xy):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté SUPERIEUR DROIT d'un Anneau de côté n, la première Alvéole de ce côté a pour coordonnées couple_xy. La
    dernière paire (x, y) de la liste sont les coordonnées de la première Alvéole du côté SUPERIEUR de l'Anneau"""
    l = [couple_xy]
    for _ in range(n):
        couple_xy = (couple_xy[0] - ALVEOLE_SIDE * (76/200), couple_xy[1] - ALVEOLE_SIDE * (132/200))
        l.append(couple_xy)
    return (l)

def top_side_coordinates(n, couple_xy):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté SUPERIEUR d'un Anneau de côté n, la première Alvéole de ce côté à pour coordonnées x et y. La
    dernière paire(x, y) de la liste sont les coordonnées de la première Alvéole du côté SUPERIEUR GAUCHE de l'Anneau"""
    l = [couple_xy]
    for _ in range(n):
        couple_xy = (couple_xy[0] - ALVEOLE_SIDE * (152/200), couple_xy[1])
        l.append(couple_xy)
    return(l)

def topleft_side_coordinates(n, couple_xy):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté SUPERIEUR GAUCHE d'un Anneau de côté n, la première Alvéole de ce côté à pour coordonnées x et y. La
    dernière paire(x, y) de la liste sont les coordonnées de la première Alvéole du côté INFERIEUR GAUCHE de l'Anneau"""
    l = [couple_xy]
    for _ in range(n):
        couple_xy = (couple_xy[0] - ALVEOLE_SIDE * (76/200), couple_xy[1] + ALVEOLE_SIDE * (132/200))
        l.append(couple_xy)
    return (l)

def bottomleft_side_coordinates(n, couple_xy):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté INFERIEUR GAUCHE d'un Anneau de côté n, la première Alvéole de ce côté à pour coordonnées x et y. La
    dernière paire(x, y) de la liste sont les coordonnées de la première Alvéole du côté INFERIEUR de l'Anneau"""
    l = [couple_xy]
    for _ in range(n):
        couple_xy = (couple_xy[0] + ALVEOLE_SIDE * (76/200), couple_xy[1] + ALVEOLE_SIDE * (132/200))
        l.append(couple_xy)
    return (l)

def bottom_side_coordinates(n, couple_xy):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté INFERIEUR d'un Anneau de côté n, la première Alvéole de ce côté à pour coordonnées x et y. La
    dernière paire(x, y) de la liste sont les coordonnées de la première Alvéole du côté INFERIEUR DROIT de l'Anneau"""
    l = [couple_xy]
    for _ in range(n):
        couple_xy = (couple_xy[0] + ALVEOLE_SIDE * (152/200), couple_xy[1])
        l.append(couple_xy)
    return(l)

def bottomright_side_coordinates(n, couple_xy):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté INFERIEUR DROIT d'un Anneau de côté n, la première Alvéole de ce côté à pour coordonnées x et y. La
    dernière paire(x, y) de la liste sont les coordonnées de la première Alvéole du côté SUPERIEUR DROIT de l'Anneau"""
    l = [couple_xy]
    for _ in range(n):
        couple_xy = (couple_xy[0] + ALVEOLE_SIDE * (76/200), couple_xy[1] - ALVEOLE_SIDE * (132/200))
        l.append(couple_xy)
    return (l)

def Anneau_coordinates(n, couple_xy):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    qui consituent un anneau de côté n"""
    beginning = (couple_xy[0] + n * ALVEOLE_SIDE * (152/200), couple_xy[1])
    topright_coordinates = topright_side_coordinates(n, beginning)
    top_coordinates = top_side_coordinates(n, topright_coordinates.pop(-1))
    topleft_coordinates = topleft_side_coordinates(n, top_coordinates.pop(-1))
    bottomleft_coordinates = bottomleft_side_coordinates(n, topleft_coordinates.pop(-1))
    bottom_coordinates = bottom_side_coordinates(n, bottomleft_coordinates.pop(-1))
    bottom_right_coordinates = bottomright_side_coordinates(n, bottom_coordinates.pop(-1))
    return topright_coordinates + top_coordinates + topleft_coordinates + bottomleft_coordinates + bottom_coordinates + bottom_right_coordinates[:-1]



#####################################################################################################################
#                                               CLASS SECTION                                                       #
#####################################################################################################################



class Alveole():
    """Une Alvéole est un hexagone, reliée à d'autres Alvéoles pour former un Anneau (une bordure d'hexagone composée
    d'Alvéole) ou une Couronne (Un ensemble d'Anneau d'une certaine épaisseur)
    "coordinates" : couple(x, y) du coin supérieur gauche du sprite de l'Alvéole ; "color" : Couleur de l'Alvéole ;
    "screen" : Ecran sur lequel l'Avéole est affichée, "size" : Proportion du Sprite de l'Alvéole"""
    def __init__(self, coordinates, color, screen, size=(ALVEOLE_SIDE, ALVEOLE_SIDE)):
        self.size = size
        self.coordinnees = coordinates
        self.screen = screen
        self.color = color
        if self.color != "blue":
            self.calculation = random_basic_calculation()
            self.calculation_str = self.calculation[0]
            self.calculation_result = self.calculation_str[1]
            self.text = font.render(self.calculation_str, True, (0, 0, 0))
            self.text_rect = self.text.get_rect()
        image = pygame.image.load(ALVEOLE_SPRITES[color]).convert_alpha()
        self.image = pygame.transform.scale(image, size)
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self.image
        self.sprite.rect = self.image.get_rect()
        self.sprite.rect.x = coordinates[0]
        self.sprite.rect.y = coordinates[1]
        self.coordinate_neighbours_list = Anneau_coordinates(1, (1366/2 - ALVEOLE_SIDE/2, 768/2 - ALVEOLE_SIDE/2))
        self.neighbours_list = []

# SETTERS PART

    def set_position(self, couple_xy):
        """Défini les coordonnées de l'Alvéole à celles données sous la forme (x, y)"""
        self.sprite.rect.x = couple_xy[0]
        self.sprite.rect.y = couple_xy[1]

    def set_color(self, new_color):
        """Change la couleur de l'Avéole, et donc change de Sprite"""
        self.color = new_color
        new_image = pygame.image.load(ALVEOLE_SPRITES[new_color]).convert_alpha()
        self.image = pygame.transform.scale(new_image, self.size)
        self.sprite.image = self.image

# GETTERS PART

    def get_position(self):
        """Renvoie la position (x, y) de l'Alvéole"""
        return (self.sprite.rect.x, self.sprite.rect.y)

    def get_center(self):
        """Renvoie le centre (x, y) de l'Alvéole"""
        return (self.get_position()[0] + self.size[0]/2, self.get_position()[1] + self.size[0]/2)

    def get_sprite(self):
        """Renvoie le pygame.sprite.Sprite() de l'Alvéole"""
        return self.sprite

    def get_neighbours(self, alveoles_plate_list):
        """Renvoie la liste des voisins de l'Alvéoles non-vérouillées, "alveoles_plate_list" : la liste de toutes les alvéoles
        qui compose le Plateau"""
        for alveole in alveoles_plate_list:
            if alveole.get_position() in self.coordinate_neighbours_list and not alveole.is_lock():
                self.neighbours_list.append(alveole)
        return self.neighbours_list

    def get_neighbours_results(self):
        """Renvoie les résultats des calculs des voisins de l'Alvéoles"""
        assert len(self.neighbours_list) > 0, "Liste des voisins vide"
        l = []
        for neighbour in self.neighbours_list:
            l.append((neighbour, neighbour.get_calculation_result()))
        return l

    def get_calculation_result(self):
        """Renvoie le résultat du calcul de l'Alvéole"""
        return self.calculation[1]

    def get_text(self):
        """Renvoie le texte de l'Alvéole à afficher (Son calcul en str)"""
        return self.text
    
    def get_calculation_str(self):
        """Renvoie le calcul de l'Alvéole en str"""
        return self.calculation_str
    
    def get_text_rect(self):
        """Renvoie le rect du texte de l'Alvéole"""
        return self.get_text().get_rect()
    
    def get_color(self):
        """Renvoie la couleur de l'Avéole (Couleurs du dictionnaire)"""
        return self.color
    
    def is_lock(self):
        """Renvoie True si l'Alvéole a été vérouillée et False si non"""
        return self.color == "blue"

# ACTIONS PART

    def lock(self):
        """Vérouille la cellule"""
        self.set_color("blue")
        self.calculation = None
        self.text = None
        self.text_rect = None
        self.calculation_result = None
        self.draw()
    
    def draw(self):
        """Afficher l'Alvéole à l'écran (Juste son Sprite, pas son texte)"""
        self.screen.blit(self.image, self.image.get_rect())
        
    def good_answer(self, answer):
        """Renvoie True si la reponse donnée est la bonne"""
        return self.calculation_result == answer

    def __str__(self):
        return f"Couleur : {self.color}, Coordonnées : {self.get_center()}, calcul : {self.get_calculation_str()}"



#======================================================================================================================#



class Anneau:
    """Un Anneau d'alvéole. "side" : (int) la longeur de ses côtés de "side" alvéoles ; "color" la couleur des
    Alvéoles de cet Anneau ; "screen" : écran sur lequel il s'affiche ; "center" couple (x,y) du centre de l'Anneau"""
    def __init__(self, side, color, screen, center=(1366/2, 768/2)):
        self.screen = screen
        self.side = side
        self.color = color
        self.x = center[0] - ALVEOLE_SIDE/2
        self.y = center[1] - ALVEOLE_SIDE/2
        self.alveoles_list = []
        if self.side > 1:
            self.coordinate_alveoles_list = Anneau_coordinates(self.side-1, (self.x, self.y))
        else:
            self.coordinate_alveoles_list = [(1366/2 - ALVEOLE_SIDE/2, 768/2 - ALVEOLE_SIDE/2)]
        self.sprites_group = pygame.sprite.Group()
        for coordinates in self.coordinate_alveoles_list:
            new_alveole = Alveole(coordinates, self.color, self.screen)
            self.alveoles_list.append(new_alveole)
            self.sprites_group.add(new_alveole.get_sprite())

    def draw(self):
        """Affiche les Alvéoles qui composent l'Anneau à l'écran"""
        self.sprites_group.draw(self.screen)

    def get_sprites(self):
        """Renvoie la liste de tous les sprites qui constituent l'anneau"""
        return self.sprites_group.sprites()
    
    def get_alveoles(self):
        """Renvoie la liste de Alvéoles qui composent l'Anneau"""
        return self.alveoles_list
    


#======================================================================================================================#



class Couronne:
    """Couronne d'Alvéoles est un ensemble d'Anneau, ce qui donne un Anneau avec une certaine épaisseur
    "color" : Couleur des Alvéoles de l'Anneau ; "layer_size" : l'épaisseur de l'anneau ; "beginning" : la couche 
    où l'anneau démarre ; """
    def __init__(self, color, layer_size, beginning, screen, center=(1366/2, 768/2)):
        self.screen = screen
        self.color = color
        self.layer_size = layer_size
        self.beginnning = beginning
        self.center = center
        self.alveoles_list = []
        self.anneaux_list = []
        for indice in range(beginning, beginning + layer_size):
            self.anneaux_list.append(Anneau(indice, self.color, self.screen, self.center))
        self.sprites_group = pygame.sprite.Group()
        for Anneau_ in self.anneaux_list:
            self.alveoles_list += Anneau_.get_alveoles()
            self.sprites_group.add(Anneau_.get_sprites())

    def draw(self):
        """Affiche les Alveoles qui composent la Couronne à l'écran"""
        self.sprites_group.draw(self.screen)

    def get_sprites(self):
        """Renvoie la liste des Sprites qui composent la Couronne"""
        return self.sprites_group.sprites()
    
    def get_layer_size(self):
        """Renvoie l'épaisseur de la Couronne"""
        return self.layer_size
    
    def get_beginning(self):
        """Renvoie la couche à laquelle commence la Couronne"""
        return self.beginnning
    
    def get_alveoles(self):
        """Renvoie la liste des Alvéoles qui composent la Couronne"""
        return self.alveoles_list



#======================================================================================================================#



class Plateau1:
    """Plateau de jeu, Consitué de Couronnes, "difficulty" : (int) Difficulté du Plateau (Epaisseur des Couronnes)
    """
    def __init__(self, difficulty, screen, center=(1366/2, 768/2)):
        self.difficulty = difficulty
        self.screen = screen
        self.alveoles_list = []
        self.center = center
        self.courronnes_list = [Couronne("blue", 1, 1, screen, self.center)]
        for indice in range(len(USED_COLORS)):
            self.courronnes_list.append(Couronne(USED_COLORS[indice], difficulty, self.courronnes_list[-1].get_layer_size() + self.courronnes_list[-1].get_beginning(), self.screen, self.center))
        self.sprites_group = pygame.sprite.Group()
        for Courrone in self.courronnes_list:
            self.alveoles_list += Courrone.get_alveoles()
            self.sprites_group.add(Courrone.get_sprites())
        for Alveole in self.alveoles_list:
            if Alveole.is_lock():
                self.main_alveole = Alveole
        self.neighbours_main_alveole_list = self.main_alveole.get_neighbours(self.alveoles_list)
        self.main_results_list = self.main_alveole.get_neighbours_results()
        self.player_input = ""


    def draw(self):
        """Affiche les ALvéoles du Plateau avec leur calcul"""
        self.screen.fill((200, 0, 0))
        self.sprites_group.draw(self.screen)
        for Alveole in self.neighbours_main_alveole_list:
            if not Alveole.is_lock():
                self.screen.blit(Alveole.get_text(), (Alveole.get_position()[0] + ALVEOLE_SIDE/2 - len(Alveole.get_calculation_str())*6, Alveole.get_position()[1] + ALVEOLE_SIDE/2 - 10))
        pygame.display.update()

    def get_sprites(self):
        """Renvoie la liste des Sprites du Plateau"""
        return self.sprites_group.sprites()
    
    def get_alveoles(self):
        """Renvoie la liste des Alvéoles qui composent le Plateau"""
        return self.alveoles_list
    
    def get_alveole_with_color(self, color):
        """Renvoie la première liste des Alveoles de couleur "color" du Plateau"""
        l = []
        for Alveole in self.alveoles:
            if Alveole.get_color() == color:
                l.append(Alveole)
        return l

    def get_alveole_with_position(self, couple_xy):
        """Renvoie l'Alveole située aux cordonnées "couple_xy" du Plateau"""
        for Alveole in self.alveoles_list:
            if Alveole.get_position() == couple_xy:
                return Alveole
            
    def erase(self):
        """Efface le Plateau de l'écran"""
        self.screen.fill((50, 170, 20))

    def get_center(self):
        """Renvoie les coordonnées du centre du Plateau sous la forme (x, y)"""
        return self.center

    def move(self, x, y):
        """Déplace le Plateau de x (abscisse) et y (ordonnée) pixels"""
        for alveole in self.alveoles_list:
            alveole.get_sprite().rect.move_ip(x, y)
        self.draw()

    def set_main_alveole(self, new_alveole):
        """Défini la nouvelle Alvéole principale (au centre de l'écran, et la vérouille)"""
        self.main_alveole = new_alveole
        new_alveole.lock()
        self.centering_on_alveole(self.main_alveole)
        self.neighbours_main_alveole_list = self.main_alveole.get_neighbours(self.alveoles_list)
        self.main_results_list = self.main_alveole.get_neighbours_results()
        self.player_input = ""

    def add_player_input(self, number):
        """Ajoute le nombre aux entrées du joueur"""
        self.player_input += str(number)
        self.check_good_answer()

    def check_good_answer(self):
        """Defini l'Alveole voisine de la principale dont le joueur a donné 
        le résultat"""
        for alveole_and_results in self.main_results_list:
            if str(alveole_and_results[1]) in self.player_input:
                self.set_main_alveole(alveole_and_results[0])

    def centering_on_alveole(self, new_alveole):
        """Centre l'Alveole "new_alveole" au centre de l'écran"""
        direction = (self.center[0] - new_alveole.get_center()[0], self.center[1] - new_alveole.get_center()[1])
        direction_x = direction[0]/SPEED_CAM
        direction_y = direction[1]/SPEED_CAM
        for _ in range(SPEED_CAM-1):
            self.move(direction_x, direction_y)
        ecart_finalx = self.center[0] - new_alveole.get_center()[0]
        ecart_finaly = self.center[1] - new_alveole.get_center()[1]
        self.move(ecart_finalx, ecart_finaly)
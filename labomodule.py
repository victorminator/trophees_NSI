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
import time
from random import randint

# INIT SECTION

pygame.font.init()

# VARIABLES SECTION

LARGEUR_ECRAN = 1366
HAUTEUR_ECRAN  = 768
DIMENSION_ECRAN = (LARGEUR_ECRAN, HAUTEUR_ECRAN)

ALVEOLE_POINT = {"green" : 10, "yellow" : 50, "orange" : 100, "red" : 300}
ALVEOLE_BORDER = {"blanc" : "bord_alveole_blanc.png", "gris" : "bord_alveole.png"}
ALVEOLE_SPRITES = {"blue" : "alveole_bleue.png", "yellow" : "alveole_jaune.png", "orange" : "alveole_orange.png", "red" : "alveole_rouge.png", "green" : "alveole_verte.png"}
ALVEOLE_COLORS = ["blue", "green", "yellow", "orange", "red"]
USED_COLORS = ["green", "yellow", "orange", "red"]
ALVEOLE_SIDE =  300
INPUT_LIMIT = 6
BEGINNING_TIMER = 60

MOVE_SPEED = 3
SPEED_CAM = MOVE_SPEED*10

# FUNCTIONS SECTION

operators = ["+", "-" , "x", ":"]

def show_text(text, couple_xy, surface, police="Impact", size=36, color=(0, 0, 0)):
    """Affiche text à l'écran aux coordonnées coupl_xy de la forme (x, y)"""
    font = pygame.font.SysFont(police, size)
    text = font.render(text, True, color)
    surface.blit(text, couple_xy)


def random_hard_calculation():
    """Renvoi un couple de la forme ("calcul", resultat) généré aléatoirement, de difficulté normale"""
    indice_operator = randint(0, len(operators)-1)
    operator = operators[indice_operator]
    if operator == "+" or operator == "-":
        first_number = randint(200, 1000)
        second_number = randint(200, 1000)
    elif operator == "x":
        first_number = randint(5, 50)
        second_number = randint(5, 50)
    else:
        first_number = randint(5, 50)
        second_number = randint(5, 50)
        answer = first_number * second_number
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
        return(f"{answer} : {second_number}", first_number) 

def random_difficult_calculation():
    """Renvoi un couple de la forme ("calcul", resultat) généré aléatoirement, de difficulté normale"""
    indice_operator = randint(0, len(operators)-1)
    operator = operators[indice_operator]
    if operator == "+" or operator == "-":
        first_number = randint(40, 100)
        second_number = randint(40, 100)
    elif operator == "x":
        first_number = randint(7, 10)
        second_number = randint(7, 10)
    else:
        first_number = randint(7, 10)
        second_number = randint(7, 10)
        answer = first_number * second_number
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
        return(f"{answer} : {second_number}", first_number) 

def random_basic_calculation():
    """Renvoi un couple de la forme ("calcul", resultat) généré aléatoirement, de difficulté normale"""
    indice_operator = randint(0, len(operators)-1)
    operator = operators[indice_operator]
    if operator == "+" or operator == "-":
        first_number = randint(3, 50)
        second_number = randint(3, 50)
    elif operator == "x":
        first_number = randint(2, 7)
        second_number = randint(2, 7)
    else:
        first_number = randint(2, 7)
        second_number = randint(2, 7)
        answer = first_number * second_number
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
        return(f"{answer} : {second_number}", first_number)   

def random_easy_calculation():
    """Renvoi un couple de la forme ("calcul", resultat) généré aléatoirement, de difficulté facile"""
    indice_operator = randint(0, len(operators)-3)
    operator = operators[indice_operator]
    first_number = randint(1, 10)
    second_number = randint(1, 10)
    if operator == "+":
        resultat = first_number + second_number
    elif operator == "-":
        if first_number < second_number:
            first_number, second_number = second_number, first_number
        resultat = first_number - second_number
    return (f"{first_number} {operator} {second_number}", resultat)
    
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
        self.coordinates = coordinates
        self.screen = screen
        self.color = color
        if self.color != "blue":
            if self.color == "red":
                self.calculation = random_hard_calculation()
            elif self.color == "orange":
                self.calculation = random_difficult_calculation()
            elif self.color == "yellow":
                self.calculation = random_basic_calculation()
            elif self.color == "green":
                self.calculation = random_easy_calculation()
            self.calculation_str = self.calculation[0]
            self.calculation_result = self.calculation_str[1]
            self.text = self.calculation_str
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

    def set_text(self, new_text):
        """Défini le texte qui sera affiché au centre de l'Alvéole"""
        self.text = new_text

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

    def set_border_color(self, border_color):
        """Change la couleur de la bordure de l'Alvéole"""
        image = pygame.image.load(ALVEOLE_BORDER[border_color])
        new_bordure = pygame.transform.scale(image, self.size)
        self.screen.blit(new_bordure, (self.coordinates[0], self.coordinates[1]))

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
    
    def get_color(self):
        """Renvoie la couleur de l'Avéole (Couleurs du dictionnaire)"""
        return self.color
    
    def is_lock(self):
        """Renvoie True si l'Alvéole a été vérouillée et False si non"""
        return self.color == "blue"
    
    def get_size(self):
        """Renvoie les proportions de l'Alvéole sous la forme (x, y)"""
        return self.size

# ACTIONS PART

    def lock(self):
        """Vérouille la cellule"""
        self.set_color("blue")
        self.calculation = None
        self.text = None
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
            self.sprites_group.draw(self.screen)
            pygame.display.update()

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
    def __init__(self, difficulty, center=(1366/2, 768/2)):
        self.active = False
        self.difficulty = difficulty
        self.screen = pygame.display.set_mode(DIMENSION_ECRAN)
        self.alveoles_list = []
        self.center = center
        self.courronnes_list = [Couronne("blue", 1, 1, self.screen, self.center)]
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
        self.is_moving = False
        self.score_number = 0
        self.score_texte = "Score : " + str(self.score_number)
        self.timer_duration = BEGINNING_TIMER
        self.timer_text = str(self.timer_duration)
        self.beginning_timer = 0

    def activate(self):
        """Active le Plateau"""
        self.active = True

    def desactivate(self):
        """Désactive le Plateau"""
        self.active = False

    def main_function(self):
        """Cette fonction est celle appelée à chaque appelle de la boucle"""
        if self.active:
            self.draw()
            if len(self.player_input) > 0:
                self.check_answer()


    def draw(self):
        """Affiche les ALvéoles du Plateau avec leur calcul"""
        self.screen.fill((100, 100, 100))
        self.sprites_group.draw(self.screen)
        self.draw_graphics()
        if not self.is_moving:
            for Alveole in self.neighbours_main_alveole_list:
                if not Alveole.is_lock():
                    show_text(Alveole.get_text(), (Alveole.get_position()[0] + ALVEOLE_SIDE/2 - len(Alveole.get_calculation_str())*6, Alveole.get_position()[1] + ALVEOLE_SIDE/2 - 10), self.screen)
            self.main_alveole.set_text(self.player_input)
            show_text(self.main_alveole.get_text(), (self.main_alveole.get_position()[0] + ALVEOLE_SIDE/2 - len(self.player_input)*6, self.main_alveole.get_position()[1] + ALVEOLE_SIDE/2 - 10), self.screen, color=(10, 10, 10))
        self.draw_main_parameters()
        pygame.display.update()

    def draw_main_parameters(self):
        """Dessine les paramètres de la partie (score, minuteur...)"""
        self.show_score((20, 20))
        self.show_timer((1310,20))
        if self.get_timer_value() == 0:
            show_text("GAME OVER", (self.center[0] - 90, self.center[1]), self.screen, size=62, color=(255, 10, 10))

    def show_score(self, couple_xy):
        """Affiche le score aux coordonnées couple_xy de la forme (x, y)"""
        show_text(f"Score : {self.score_number}", couple_xy, self.screen)

    def show_timer(self, couple_xy):
        """Affiche le minuteur aux coordonées couple_xy de la forme (x, y)"""
        if self.get_timer_value() > 0:
            if self.get_timer_value() < 10:
                text = str(self.get_timer_value())[:3]
            elif self.get_timer_value() >= 10:
                text = str(self.get_timer_value())[:2]
        else:
            text = "0"
        show_text(text, couple_xy, self.screen)

    def draw_graphics(self):
        """Affiche les graphismes en plus"""
        if not self.is_moving:
            for Alveole in  self.neighbours_main_alveole_list:
                if not Alveole.is_lock():
                    couple_xy = Alveole.get_position()
                    image = pygame.image.load(ALVEOLE_BORDER["blanc"])
                    new_bordure = pygame.transform.scale(image, self.get_alveole_with_position(couple_xy).get_size())
                    self.screen.blit(new_bordure, (couple_xy[0], couple_xy[1]))

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
        if self.is_moving:
            for alveole in self.alveoles_list:
                alveole.get_sprite().rect.move_ip(x, y)
            self.draw()

    def set_main_alveole(self, new_alveole):
        """Défini la nouvelle Alvéole principale (au centre de l'écran, et la vérouille)"""
        self.is_moving = True
        self.main_alveole = new_alveole
        self.lock_alveoles(self.all_good_alveole())
        self.centering_on_alveole(self.main_alveole)
        self.neighbours_main_alveole_list = self.main_alveole.get_neighbours(self.alveoles_list)
        self.main_results_list = self.main_alveole.get_neighbours_results()
        self.player_input = ""
        self.is_moving = False

    def check_answer(self):
        """Vérifie la réponse donnée par le joueur et agis en conséquence"""
        if self.check_player_input() and self.new_main_alveole() != -1:
            self.set_main_alveole(self.new_main_alveole())
        elif self.check_player_input():
            pass
        else:
            self.restart_player_input()

    def add_player_input(self, input):
        """Ajoute le chiffre donné par le joueur à ses entrées"""
        if self.get_timer_value() > 0:
            self.start_timer()
            if len(self.player_input) < INPUT_LIMIT and not self.is_moving:
                self.player_input += str(input)
                self.draw()

    def start_timer(self):
        """Démarre le minuteur"""
        if self.beginning_timer <= 0:
            self.beginning_timer = time.time()

    def get_elapsed_time(self):
        """Renvoie le temps écoulé après la première entrée du joueur"""
        if self.beginning_timer > 0:
            return time.time() - self.beginning_timer
        else:
            return 0
        
    def get_timer_value(self):
        """Renvoie la valeur du minuteur qui s'enclenche après la première entrée du joueur"""
        if self.timer_duration - self.get_elapsed_time() > 0:
            return self.timer_duration - self.get_elapsed_time()
        else:
            return 0

    def restart_player_input(self):
        """Déclenché lorsque le joueur à entrer un chiffre non valide, et efface son entrée
        pour lui permettre de réessayer"""
        self.player_input = ""

    def check_player_input(self):
        """Renvoie True si l'input donné est valide (c'est-à-dire si le caractère correspond
        à une partie des réponses attendues)"""
        for results in self.main_results_list:
            if len(str(results[1])) >= len(self.player_input)-1:
                if str(results[1])[:len(self.player_input)] == self.player_input:
                    return True
        return False

    def all_good_alveole(self):
        """Renvoie une liste de toutes les alveoles qui ont le résultat donné par le joueur"""
        l = []
        for results in self.main_results_list:
            if self.player_input == str(results[1]):
                l.append(results[0])
        return l

    def lock_alveoles(self, list_alveole):
        """Vérouille les Alvéoles de list_alveole"""
        for Alveole in list_alveole:
            self.score_number += ALVEOLE_POINT[Alveole.get_color()]
            Alveole.lock()

    def new_main_alveole(self):
        """Renvoie l'alveole du couple (alveole, resultat) dont alveole sera la nouvelle
        main_alveole si son résultat a été donné par le joueur"""
        for alveole_and_results in self.main_results_list:
            if str(alveole_and_results[1]) == self.player_input:
                return alveole_and_results[0]
        return -1

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
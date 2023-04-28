# IMPORT SECTION

import pygame
import pygame.display
import pygame.event
import pygame.key
from pygame.sprite import AbstractGroup
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
import os
from random import randint

# INIT SECTION

pygame.init()

# VARIABLES SECTION

BLUE = "blue"
GREEN = "green"
YELLOW = "yellow"
ORANGE = "orange"
RED = "red"

LARGEUR_ECRAN = 1366
HAUTEUR_ECRAN  = 768
DIMENSION_ECRAN = (LARGEUR_ECRAN, HAUTEUR_ECRAN)

SCREEN_CENTRE = (LARGEUR_ECRAN // 2, HAUTEUR_ECRAN // 2)

ALVEOLE_POINT = {GREEN : 10, YELLOW : 50, ORANGE : 100, RED : 300}
ALVEOLE_SPRITES = {BLUE : "Images/Alveoles/alveole_bleue.png", YELLOW : "Images/Alveoles/alveole_jaune.png",ORANGE : "Images/Alveoles/alveole_orange.png", RED : "Images/Alveoles/alveole_rouge.png",GREEN : "Images/Alveoles/alveole_verte.png"}

ALVEOLE_COLORS = [BLUE, GREEN, YELLOW, ORANGE, RED]
USED_COLORS = ALVEOLE_COLORS[1:]
ALVEOLE_SIDE =  300
INPUT_LIMIT = 6
TIMER_DURATION = 60

MOVEMENT_CUT = 9
STAR_SCORE = [800, 1400, 2000]

INPUT_DELAY = 0.435

CROSS_DURATION = 0.3

POS_ETOILES_X = [[SCREEN_CENTRE[0]], [SCREEN_CENTRE[0] - 55, SCREEN_CENTRE[0] + 55], [SCREEN_CENTRE[0] - 55, SCREEN_CENTRE[0], SCREEN_CENTRE[0] + 55]]

GAME_OVER_SLIDE_SPEED = LARGEUR_ECRAN // 20
STAR_GROWTH_SPEED = 1
STAR_MAX_SIZE = 150

## Sounds
SOUND_DING = pygame.mixer.Sound("Audio/dingding.wav")
SOUND_GAME_OVER = pygame.mixer.Sound("Audio/Windows XP Critical Stop.wav")
SOUND_FAIL = pygame.mixer.Sound("Audio/Windows XP Ding.wav")

# FUNCTIONS SECTION

operators = ["+", "-" , "x", ":"]

def generate_images():
    return {color: pygame.transform.scale(pygame.image.load(ALVEOLE_SPRITES[color]), (ALVEOLE_SIDE, ALVEOLE_SIDE)).convert_alpha() for color in ALVEOLE_SPRITES}

def show_text(text, couple_xy, surface, police="Impact", size=36, color=(0, 0, 0), anchor="topleft"):
    """Affiche text à l'écran aux coordonnées coupl_xy de la forme (x, y)"""
    font = pygame.font.SysFont(police, size)
    text = font.render(text, True, color)
    text_rect = eval(f"text.get_rect({anchor}={couple_xy})")
    surface.blit(text, text_rect)


def get_images(folder):
    return [pygame.image.load(folder + "/" + img_name).convert_alpha() for img_name in os.listdir(folder)]
        
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


COLORS_DIFFICULTY = {BLUE: lambda:None, GREEN:random_easy_calculation, YELLOW:random_basic_calculation, ORANGE:random_difficult_calculation, RED:random_hard_calculation}

##################################################################################################################
#                                               CLASS SECTION                                                       #
#####################################################################################################################



class Alveole(pygame.sprite.Sprite):
    """Une Alvéole est un hexagone, reliée à d'autres Alvéoles pour former un Anneau (une bordure d'hexagone composée
    d'Alvéole) ou une Couronne (Un ensemble d'Anneau d'une certaine épaisseur)
    "coordinates" : couple(x, y) du coin supérieur gauche du sprite de l'Alvéole ; "color" : Couleur de l'Alvéole ;
    "screen" : Ecran sur lequel l'Avéole est affichée, "size" : Proportion du Sprite de l'Alvéole"""
    def __init__(self, coordinates, color, screen, size=(ALVEOLE_SIDE, ALVEOLE_SIDE)):
        super().__init__()
        self.size = size
        self.coordinates = coordinates
        self.screen = screen
        self.initial_color = color
        #self.set_color(color)
        self.rect = pygame.Surface((ALVEOLE_SIDE, ALVEOLE_SIDE)).get_rect(topleft=coordinates)
        self.coordinate_neighbours_list = Anneau_coordinates(1, (SCREEN_CENTRE[0] - ALVEOLE_SIDE//2, SCREEN_CENTRE[1] - ALVEOLE_SIDE//2))
        self.neighbours_list = []
        self.is_shining = False

# SETTERS PART

    def set_text(self, new_text):
        """Définit le texte qui sera affiché au centre de l'Alvéole"""
        self.text = new_text

    def set_position(self, couple_xy):
        """Définit les coordonnées de l'Alvéole à celles données sous la forme (x, y)"""
        self.rect.topleft = couple_xy
    
    def set_color(self, new_color, pre_loaded_images):
        """Change la couleur de l'Avéole, et donc change de Sprite"""
        self.color = new_color
        self.image = pre_loaded_images[self.color]
        if self.color != BLUE:
            self.calculation = COLORS_DIFFICULTY[self.color]() # Simplifié à l'aide d'un dictionnaire
            self.calculation_str = self.calculation[0]
            self.calculation_result = self.calculation_str[1]
            self.text = self.calculation_str

# GETTERS PART

    def get_position(self):
        """Renvoie la position (x, y) de l'Alvéole"""
        return self.rect.topleft

    def get_center(self):
        """Renvoie le centre (x, y) de l'Alvéole"""
        return self.rect.center

    def get_neighbours(self, alveoles_plate_list):
        """Renvoie la liste des voisins de l'Alvéoles non-vérouillées, "alveoles_plate_list" : la liste de toutes les alvéoles
        qui compose le Plateau"""
        self.neighbours_list.clear()
        for alveole in alveoles_plate_list:
            if alveole.get_position() in self.coordinate_neighbours_list and not alveole.is_lock():
                self.neighbours_list.append(alveole)
        return self.neighbours_list

    def get_neighbours_results(self):
        """Renvoie les résultats des calculs des voisins de l'Alvéoles"""
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
        return self.color == BLUE
    
    def get_size(self):
        """Renvoie les proportions de l'Alvéole sous la forme (x, y)"""
        return self.size

# ACTIONS PART

    def lock(self, img_list):
        """Vérouille la cellule"""
        self.set_color(BLUE, img_list)
        self.calculation = None
        self.text = None
        self.calculation_result = None
        #self.draw() Semble être inutile
    
    def unlock(self, img_list):
        self.set_color(self.initial_color, img_list)
    
    def draw(self):
        """Afficher l'Alvéole à l'écran (Juste son Sprite, pas son texte)"""
        self.screen.blit(self.image, self.image.get_rect())
        
    def good_answer(self, answer):
        """Renvoie True si la reponse donnée est la bonne"""
        return self.calculation_result == answer
    
    def apply_vector(self, applied_vector):
        """
        Déplace l'alvéole au cours du temps en fonction du vecteur vitesse passé en paramètre
        """
        self.rect.topleft += applied_vector

    def __str__(self):
        return f"Couleur : {self.color}, Coordonnées : {self.get_center()}, calcul : {self.get_calculation_str()}"



#======================================================================================================================#



class Anneau:
    """Un Anneau d'alvéole. "side" : (int) la longeur de ses côtés de "side" alvéoles ; "color" la couleur des
    Alvéoles de cet Anneau ; "screen" : écran sur lequel il s'affiche ; "center" couple (x,y) du centre de l'Anneau"""
    def __init__(self, side, color, screen):
        self.screen = screen
        self.side = side
        self.color = color
        self.x = SCREEN_CENTRE[0] - ALVEOLE_SIDE/2
        self.y = SCREEN_CENTRE[1] - ALVEOLE_SIDE/2
        self.alveoles_list = []
        if self.side > 1:
            self.coordinate_alveoles_list = Anneau_coordinates(self.side-1, (self.x, self.y))
        else:
            self.coordinate_alveoles_list = [(1366/2 - ALVEOLE_SIDE/2, 768/2 - ALVEOLE_SIDE/2)]
        self.sprites_group = pygame.sprite.Group()
        for coordinates in self.coordinate_alveoles_list:
            new_alveole = Alveole(coordinates, self.color, self.screen)
            self.alveoles_list.append(new_alveole)
            self.sprites_group.add(new_alveole)
            #self.sprites_group.draw(self.screen)
            #pygame.display.update()

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
    def __init__(self, color, layer_size, beginning, screen):
        self.screen = screen
        self.color = color
        self.layer_size = layer_size
        self.beginnning = beginning
        self.alveoles_list = []
        self.anneaux_list = []
        for indice in range(beginning, beginning + layer_size):
            self.anneaux_list.append(Anneau(indice, self.color, self.screen))
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
class StarSprite(pygame.sprite.Sprite):
    def __init__(self, image_etoile, star_pos, max_size=STAR_MAX_SIZE) -> None:
        super().__init__()
        self.image = image_etoile
        self.center_pos = star_pos
        self.max_size = max_size
        self.rect = self.image.get_rect(center=self.center_pos)
    
    def grow(self, amount):
        self.image = pygame.transform.scale(self.image,(self.rect.width + amount, self.rect.height + amount)).convert_alpha()
        self.rect = self.image.get_rect(center=self.center_pos)
    
    def set_pos(self, new_pos):
        self.rect.center = new_pos

    """
    Ne fonctionne pas comme prévu
    def update(self):
        print(self.rect.width, self.rect.height)
        if self.rect.width < self.max_size:
            self.grow(1)
        elif self.rect.width > self.max_size:
            self.grow(self.rect.width - self.max_size)
    """

class Bouton(pygame.sprite.Sprite):

    def __init__(self, couple_xy, function, standard_surface, hovered_surface):
        """Crée un bouton utilisé pour les Menu"""
        super().__init__()
        self.coordinates = couple_xy
        self.function = function
        self.standard_surface = standard_surface
        self.hovered_surface = hovered_surface
        self.image = self.standard_surface
        self.rect = self.image.get_rect(center=couple_xy)
        self.activation = False
        self.currently_hovered = False
        self.may_press = False
    
    def mouse_collision(self):
        return self.rect.collidepoint(pygame.mouse.get_pos())

    def get_height(self):
        """Renvoie la hauteur du bouton"""
        return self.rect.height
    
    def get_width(self):
        """Renvoie la largeur du bouton"""
        return self.rect.width


    def activate(self):
        """Active le bouton"""
        self.activation = True

    def desactivate(self):
        """Désactive le bouton"""
        self.activation = False

    def get_rect(self):
        """Renvoie le rect du bouton"""
        return self.rect

    def get_function(self):
        """Renvoie la fonction du bouton"""
        return self.function
    
    def check_if_pressed(self):
        if True in pygame.mouse.get_pressed():
            if self.may_press:
                self.function()
        else:
            self.may_press = True
        
    
    def update(self):
        collides_mouse = self.mouse_collision()
        if self.currently_hovered != collides_mouse:
            self.currently_hovered = collides_mouse
            if collides_mouse:
                self.image = self.hovered_surface
            else:
                self.image = self.standard_surface
        if self.currently_hovered:
            self.check_if_pressed()
            

class Plateau1:
    """Plateau de jeu, Consitué de Couronnes, "difficulty" : (int) Difficulté du Plateau (Epaisseur des Couronnes)
    """
    def __init__(self, difficulty):
        self.active = False
        self.on_game_over = False
        self.difficulty = difficulty
        self.screen = pygame.display.set_mode(DIMENSION_ECRAN)
        self.game_over_bg = pygame.Surface((LARGEUR_ECRAN, HAUTEUR_ECRAN // 2))
        self.game_over_bg.fill((255, 255, 255))
        self.game_over_rect = self.game_over_bg.get_rect(center=(-LARGEUR_ECRAN // 2, HAUTEUR_ECRAN / 2))
        self.images_alveoles = generate_images()
        self.image_rejouer = pygame.image.load("Images/replay.png").convert_alpha()
        self.image_rejouer_survole = pygame.image.load("Images/replay_hovered.png").convert_alpha()
        self.bouton_rejouer = Bouton((SCREEN_CENTRE[0], SCREEN_CENTRE[1] * 1.25), self.start_game, self.image_rejouer, self.image_rejouer_survole)
        self.bouton_groupe = pygame.sprite.GroupSingle(self.bouton_rejouer)
        self.images_bordures = {"blanc" : pygame.transform.scale(pygame.image.load("Images/bord_alveole_blanc.png"), (ALVEOLE_SIDE, ALVEOLE_SIDE)).convert_alpha(), "gris" : pygame.transform.scale(pygame.image.load("Images/bord_alveole.png"), (ALVEOLE_SIDE, ALVEOLE_SIDE)).convert_alpha()}
        self.star_image = pygame.image.load("Images/star.png").convert_alpha()
        self.star_pos_y = self.game_over_rect.top * 1.2
        self.alveoles_list = []
        self.courronnes_list = [Couronne("blue", 1, 1, self.screen)]
        self.premiere_alveole = self.courronnes_list[0].alveoles_list[0] 
        for indice in range(len(USED_COLORS)):
            self.courronnes_list.append(Couronne(USED_COLORS[indice], difficulty, self.courronnes_list[-1].get_layer_size() + self.courronnes_list[-1].get_beginning(), self.screen))
        self.sprites_group = pygame.sprite.Group()
        for Courrone in self.courronnes_list: 
            self.alveoles_list += Courrone.get_alveoles()
            self.sprites_group.add(Courrone.get_sprites())
        self.timer_duration = TIMER_DURATION
        self.timer_text = str(TIMER_DURATION)
        self.beginning_timer = 0
        self.cross_image = pygame.image.load("Images/croix_erreur.png").convert_alpha()
        self.is_displaying_cross = False
        self.cross_timer = 0
        self.movement_frame_count = 0
        self.vecteur_deplacement_plateau = pygame.math.Vector2(0, 0)
        self.start_game()
        self.last_input_moment = 0
        self.neighbours_main_alveole_list = self.main_alveole.get_neighbours(self.alveoles_list)
        self.main_results_list = self.main_alveole.get_neighbours_results()
    
    def refresh_problems(self):
        for alv in self.alveoles_list:
            alv.unlock(self.images_alveoles)
    
    def is_moving(self):
        return self.vecteur_deplacement_plateau.x != 0 or self.vecteur_deplacement_plateau.y != 0
    
    def start_game(self):
        self.score_number = 0
        self.score_texte = "Score : " + str(self.score_number)
        self.refresh_problems()
        self.set_main_alveole(self.premiere_alveole, should_lock=False)
        if self.on_game_over: 
            self.on_game_over = False
            self.game_over_rect.right = 0
        self.start_timer()
        

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
            self.update()
            if not self.on_game_over:
                self.check_game_over()
                if self.is_displaying_cross:
                    self.update_cross()
                elif len(self.player_input) > 0 and time.time() - self.last_input_moment > INPUT_DELAY:
                    self.check_answer()


    def draw(self):
        """Affiche les ALvéoles du Plateau avec leur calcul"""
        self.screen.fill((100, 100, 100))
        self.sprites_group.draw(self.screen)
        if self.on_game_over:
            self.screen.blit(self.game_over_bg, self.game_over_rect)
            show_text(f"Game Over : {self.score_number} pts", (LARGEUR_ECRAN // 2, HAUTEUR_ECRAN // 2.5), self.screen, size=62, color=(0, 0, 0), anchor="center")
        else:
            self.draw_graphics()
            if not self.is_moving():
                for Alveole in self.neighbours_main_alveole_list:
                    if not Alveole.is_lock():
                        show_text(Alveole.get_text(), Alveole.rect.center, self.screen, anchor="center")
                self.main_alveole.set_text(self.player_input)
                show_text(self.main_alveole.get_text(), self.main_alveole.rect.center, self.screen, color=(10, 10, 10), anchor="center")
            self.draw_main_parameters()
            if self.is_displaying_cross: # Ajout de la croix lorsque le joueur s'est trompé
                self.screen.blit(self.cross_image, self.cross_image.get_rect(center=self.main_alveole.rect.center))
        #pygame.display.update()

    def check_game_over(self):
        self.on_game_over = self.get_timer_value() == 0
        if self.on_game_over:
            self.start_game_over()

    def start_game_over(self):    
        SOUND_GAME_OVER.play()
        self.is_displaying_cross = False
        self.generate_final_stars()
    
    def draw_main_parameters(self):
        """Dessine les paramètres de la partie (score, minuteur...)"""
        self.show_score((20, 20))
        self.show_timer((1310,20))

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
        if not self.is_moving():
            for Alveole in  self.neighbours_main_alveole_list:
                if not Alveole.is_lock():
                    self.screen.blit(self.images_bordures["blanc"], Alveole.get_position())

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

    def move(self, x, y):
        """Déplace le Plateau de x (abscisse) et y (ordonnée) pixels"""
        for alveole in self.alveoles_list:
            alveole.rect.move_ip(x, y)

    def set_main_alveole(self, new_alveole, should_lock=True):
        """Défini la nouvelle Alvéole principale (au centre de l'écran, et la vérouille)"""
        self.main_alveole = new_alveole
        if should_lock:    
            self.lock_alveoles(self.all_good_alveole())
        self.centering_on_alveole(self.main_alveole)
        self.player_input = ""
    
    def update_cross(self):
        """
        Enlève l'image de la croix au bout d'un certain délai
        """
        if time.time() - self.cross_timer > CROSS_DURATION:
            self.is_displaying_cross = False

    def check_answer(self):
        """Vérifie la réponse donnée par le joueur et agis en conséquence"""
        #if self.check_player_input():
        new_alv = self.new_main_alveole()
        if new_alv != -1: # Plus propre sans le pass
            SOUND_DING.play()
            self.set_main_alveole(new_alv)
        else:
            SOUND_FAIL.play()
            self.is_displaying_cross = True
            self.cross_timer = time.time()
            self.restart_player_input()

    def add_player_input(self, input):
        """Ajoute le chiffre donné par le joueur à ses entrées"""
        if not self.is_displaying_cross:
            if self.get_timer_value() > 0:
                if len(self.player_input) < INPUT_LIMIT and not self.is_moving():
                    self.player_input += str(input)
                    self.last_input_moment = time.time()

    def start_timer(self):
        """Démarre le minuteur"""
        self.beginning_timer = time.time()

    def get_elapsed_time(self):
        """Renvoie le temps écoulé après la première entrée du joueur"""
        if self.beginning_timer > 0:
            return time.time() - self.beginning_timer
        return 0
        
    def get_timer_value(self):
        """Renvoie la valeur du minuteur qui s'enclenche après la première entrée du joueur"""
        val_timer = TIMER_DURATION - self.get_elapsed_time() # Simplifié
        if val_timer > 0:
            return val_timer
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
            if self.player_input == str(results[1]) and not results[0].is_lock():
                #print(results[0].color)
                l.append(results[0])
        return l

    def lock_alveoles(self, list_alveole):
        """Vérouille les Alvéoles de list_alveole"""
        for Alveole in list_alveole:
            #print(Alveole.calculation)
            self.score_number += ALVEOLE_POINT[Alveole.get_color()]
            Alveole.lock(self.images_alveoles)

    def new_main_alveole(self):
        """Renvoie l'alveole du couple (alveole, resultat) dont alveole sera la nouvelle
        main_alveole si son résultat a été donné par le joueur"""
        for alveole_and_results in self.main_results_list:
            if str(alveole_and_results[1]) == self.player_input:
                return alveole_and_results[0]
        return -1

    def get_board_displacement_vector(self, new_alveole:Alveole):
        """
        Utilisation de la relation de Chasles pour déterminer le vecteur qui se
        dirige du centre de l'écran vers l'alvéole cible.
        """
        return pygame.math.Vector2(SCREEN_CENTRE) - pygame.math.Vector2(list(map(int, new_alveole.get_center())))
    
    def update(self):
        if self.on_game_over:
            if self.game_over_rect.right < LARGEUR_ECRAN:
                self.game_over_rect.right += GAME_OVER_SLIDE_SPEED
            elif self.game_over_rect.right > LARGEUR_ECRAN:
                self.game_over_rect.right = LARGEUR_ECRAN
            else:
                self.stars.draw(self.screen)
                self.bouton_rejouer.update()
                self.bouton_groupe.draw(self.screen)
        if self.is_moving():
            if self.movement_frame_count == MOVEMENT_CUT:
                self.vecteur_deplacement_plateau = self.remaining_vector
            
            for alv in self.alveoles_list:
                alv.apply_vector(self.vecteur_deplacement_plateau)
            
            self.movement_frame_count += 1
            if self.movement_frame_count > MOVEMENT_CUT:
                self.vecteur_deplacement_plateau = pygame.math.Vector2(0, 0)
                self.movement_frame_count = 0
                self.fix_position()
                self.neighbours_main_alveole_list = self.main_alveole.get_neighbours(self.alveoles_list)
                print(len(self.neighbours_main_alveole_list))
                self.main_results_list = self.main_alveole.get_neighbours_results()
                if self.main_results_list == []:
                    self.on_game_over = True
                    self.beginning_timer = 0
                    self.start_game_over()
                #print(self.main_results_list)
    
    def generate_final_stars(self):
       star_number = (self.score_number - 200) // 600
       self.stars = pygame.sprite.Group(*[StarSprite(self.star_image, (POS_ETOILES_X[star_number - 1][i],self.star_pos_y)) for i in range(star_number)])   

    def fix_position(self):
        deplacement_final_x, deplacement_final_y = SCREEN_CENTRE
        deplacement_final_x -= self.main_alveole.rect.centerx
        deplacement_final_y -= self.main_alveole.rect.centery
        self.move(deplacement_final_x, deplacement_final_y)

    def centering_on_alveole(self, new_alveole):
        """Centre l'Alveole "new_alveole" au centre de l'écran"""
        total_displacement = self.get_board_displacement_vector(new_alveole)
        self.vecteur_deplacement_plateau = total_displacement // MOVEMENT_CUT
        self.remaining_vector = pygame.math.Vector2(total_displacement.x % MOVEMENT_CUT, total_displacement.y % MOVEMENT_CUT)

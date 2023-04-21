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

pygame.font.init()

CENTRE = "center"
HAUT_GAUCHE = "topleft"
HAUT_DROIT = "topright"
BAS_GAUCHE = "bottomleft"
BAS_DROIT = "bottomright"

ALVEOLE = {"blue" : "alveole_bleue.png", "yellow" : "alveole_jaune.png", "orange" : "alveole_orange.png", "red" : "alveole_rouge.png", "green" : "alveole_verte.png"}
COLOR = ["blue", "green", "yellow", "orange", "red"]

DIFFICULT_COLOR = ["green", "yellow"]

SIDE =  300 # C'est la taille des alveoles (Le côté de leur image)

operateurs = ["+", "-" , "x", ":"]

font = pygame.font.SysFont("Arial", 36)

def generate_key_dict():
    key_dict = {"espace":pygame.K_SPACE}
    for i in list(range(48, 48 + 10)) + list(range(97, 97 +26)):
        key_dict[chr(i)] = eval("pygame.K_" + chr(i))
    return  key_dict

touches_lettres = generate_key_dict()

ancrages = [CENTRE, HAUT_DROIT, HAUT_GAUCHE, BAS_GAUCHE, BAS_DROIT]

class Son:
    def __init__(self, chemin_fichier, volume=1):
        self.volume = volume
        self.fichier = pygame.mixer.Sound(chemin_fichier)
        self.changer_volume(volume)
    
    def jouer(self):
        self.fichier.play()
    
    def arreter(self):
        self.fichier.stop()
    
    def changer_volume(self, nouveau_volume):
        self.fichier.set_volume(nouveau_volume)
    
    def jouer_en_boucle(self):
        self.fichier.play(-1)

class Jeu:
    def __init__(self, largeur_ecran, hauteur_ecran, titre_jeu="", fps=60) -> None:
        pygame.init()
        self.largeur_ecran = largeur_ecran
        self.hauteur_ecran = hauteur_ecran
        self.titre_jeu = titre_jeu
        self.fps = fps

    
    def lancer(self):
        self.ecran = pygame.display.set_mode((self.largeur_ecran, self.hauteur_ecran))
        self.horloge = pygame.time.Clock()
        pygame.display.set_caption(self.titre_jeu)
    
    def evenements(self):
        for entree in pygame.event.get():
            if entree.type == pygame.QUIT:
                self.arret()
            if entree.type in touches_lettres.values():
                pass # A completer
    
    def arret(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
    
    def boucle(self):
        self.evenements()
        self.draw()
        self.update()
        pygame.display.update()
        self.horloge.tick(self.fps)

########################################################################################################################################################
# PARTIE MODIFIEE
########################################################################################################################################################

def normal_calcul_generator():
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
    else:
        resultat = first_number
    if operator != ":":
        return (f"{first_number} {operator} {second_number}", resultat)
    else:
        return(f"{reponse} : {second_number}", resultat)

def topright_side_XY(n, x, y):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté supérieur droit d'un anneau de côté n"""
    l = [(x, y)]
    for _ in range(n):
        x -= SIDE * (76/200)
        y -= SIDE * (132/200)
        l.append((x, y))
    return (l)

def topleft_side_XY(n, x, y):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté supérieur gauche d'un anneau de côté n"""
    l = [(x, y)]
    for _ in range(n):
        x -= SIDE * (76/200)
        y += SIDE * (132/200)
        l.append((x, y))
    return (l)

def bottomright_side_XY(n, x, y):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté inférieur droit d'un anneau de côté n"""
    l = [(x, y)]
    for _ in range(n):
        x += SIDE * (76/200)
        y -= SIDE * (132/200)
        l.append((x, y))
    return (l)

def bottomleft_side_XY(n, x, y):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté inférieur gauche d'un anneau de côté n"""
    l = [(x, y)]
    for _ in range(n):
        x += SIDE * (76/200)
        y += SIDE * (132/200)
        l.append((x, y))
    return (l)

def top_side_XY(n, x, y):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté supérieur d'un anneau de côté n"""
    l = [(x, y)]
    for _ in range(n):
        x -= SIDE * (152/200)
        l.append((x, y))
    return(l)

def bottom_side_XY(n, x, y):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    d'un coté inférieur d'un anneau de côté n"""
    l = [(x, y)]
    for _ in range(n):
        x += SIDE * (152/200)
        l.append((x, y))
    return(l)

def Anneau(n, x, y):
    """Renvoie une liste de coordonnées, sous la forme [(x,y), (x,y)...] qui correspondent aux coordonnées des alvéoles
    qui consituent un anneau de côté n"""
    debut = x + n * SIDE * (152/200)
    cote_haut_droit_XY = topright_side_XY(n, debut, y)
    cote_haut_XY = top_side_XY(n, cote_haut_droit_XY[-1][0],cote_haut_droit_XY[-1][1])
    cote_haut_gauche_XY = topleft_side_XY(n, cote_haut_XY[-1][0], cote_haut_XY[-1][1])
    cote_bas_gauche_XY = bottomleft_side_XY(n, cote_haut_gauche_XY[-1][0], cote_haut_gauche_XY[-1][1])
    cote_bas_XY = bottom_side_XY(n, cote_bas_gauche_XY[-1][0], cote_bas_gauche_XY[-1][1])
    cote_bas_droit_XY = bottomright_side_XY(n, cote_bas_XY[-1][0], cote_bas_XY[-1][1])
    return cote_haut_droit_XY[:-1] + cote_haut_XY[:-1] + cote_haut_gauche_XY[:-1] + cote_bas_gauche_XY[:-1] + cote_bas_XY[:-1] + cote_bas_droit_XY[:-1]

class Anneau_Alveole:
    """Un Anneau d'alvéole, où "side" correspond à la longeur de ses côtés de "side" alvéoles ; "color" correspond
    à la couleur des alvéoles de cet anneau ; "screen" est l'écran sur lequel il s'affiche ; "centre" est un tuple des
    coordonnées (x,y du centre de l'anneau"""
    def __init__(self, side, color, screen, centre=(1366/2, 768/2)):
        self.screen = screen
        self.side = side
        self.color = color
        self.x = centre[0] - SIDE/2
        self.y = centre[1] - SIDE/2
        self.alveoles = []
        if self.side > 1:
            self.coordonnee = Anneau(self.side-1, self.x, self.y)
        else:
            self.coordonnee = [(1366/2 - SIDE/2, 768/2 - SIDE/2)]
        self.groupe_sprite = pygame.sprite.Group()
        for coordonnee in self.coordonnee:
            new_alveole = Alveole(coordonnee, self.color, self.screen)
            self.alveoles.append(new_alveole)
            self.groupe_sprite.add(new_alveole.get_sprite())

    def Afficher(self):
        """Affiche à l'écran l'anneau"""
        self.groupe_sprite.draw(self.screen)

    def get_sprite(self):
        """Renvoie la liste de tous les sprites qui constituent l'anneau"""
        return self.groupe_sprite.sprites()
    
    def get_alveoles(self):
        return self.alveoles
    
class Courronne_Alveole:
    """Une courronne d'alvéoles et un anneau avec une certaine épaisseur d'alvéoles"""
    def __init__(self, color, epaisseur, debut, ecran, centre=(1366/2, 768/2)):
        self.screen = ecran
        self.color = color
        self.size = epaisseur
        self.begin = debut
        self.centre = centre
        self.alveoles = []
        self.anneaux = []
        for indice in range(debut, debut + epaisseur):
            self.anneaux.append(Anneau_Alveole(indice, self.color, self.screen, self.centre))
        self.groupe_sprite = pygame.sprite.Group()
        for anneau in self.anneaux:
            self.alveoles += anneau.get_alveoles()
            self.groupe_sprite.add(anneau.get_sprite())

    def Afficher(self):
        self.groupe_sprite.draw(self.screen)

    def get_sprite(self):
        return self.groupe_sprite.sprites()
    
    def get_epaisseur(self):
        return self.size
    
    def get_debut(self):
        return self.begin
    
    def get_alveoles(self):
        return self.alveoles


class Alveole():
    def __init__(self, coordonne, color, ecran, size=(SIDE, SIDE)):
        self.coordonnees = coordonne
        self.size = size[0]
        self.screen = ecran
        self.color = color
        if self.color != "blue":
            self.calcul = normal_calcul_generator()
            self.calcul_str = self.calcul[0]
            self.texte = font.render(self.calcul_str, True, (0, 0, 0))
            self.texte_rect = self.texte.get_rect()
            self.reponse = self.calcul_str[1]
        else:
            self.calcul = ""
            self.texte = ""
            self.texte_rect = 0
            self.reponse = None
        image = pygame.image.load(ALVEOLE[color]).convert_alpha() #image d'origine
        self.image = pygame.transform.scale(image, size) #redimension image
        self.dessin = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.dessin.add(self.sprite)
        self.sprite.image = self.image
        self.sprite.rect = self.image.get_rect()
        self.sprite.rect.x = coordonne[0]
        self.sprite.rect.y = coordonne[1]
        self.position_voisin = Anneau(1, 1366/2 - SIDE/2, 768/2 - SIDE/2)
        self.liste_voisin = []

    def setCoord(self, x, y):
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    def set_blue_color(self):
        self.color = "blue"
        new_image = pygame.image.load(ALVEOLE["blue"]).convert_alpha()
        self.image = pygame.transform.scale(new_image, (self.size, self.size))
        self.sprite.image = self.image
        self.calcul = ""
        self.texte = ""
        self.texte_rect = 0
        self.reponse = None
        self.Afficher()

    def getCoord(self):
        return (self.sprite.rect.x, self.sprite.rect.y)

    def get_centre(self):
        return (self.getCoord()[0] + self.size/2, self.getCoord()[1] + self.size/2)

    def get_sprite(self):
        return self.sprite
    
    def Afficher(self):
        self.dessin.draw(self.screen)

    def get_voisin(self, liste_plateau_alveole):
        for alveole in liste_plateau_alveole:
            if alveole.getCoord() in self.position_voisin and alveole.get_color() != "blue":
                self.liste_voisin.append(alveole)
        return self.liste_voisin

    def get_alveole_resultat(self):
        assert len(self.liste_voisin) > 0, "Liste des voisins vide"
        l = []
        for alveole_voisine in self.liste_voisin:
            tuple = (alveole_voisine, alveole_voisine.get_resultat_calcul())
            l.append(tuple)
        return l

    def get_resultat_calcul(self):
        return self.calcul[1]

    def get_texte(self):
        return self.texte
    
    def get_calcul_str(self):
        return self.calcul_str
    
    def get_texte_rect(self):
        return self.texte_rect
    
    def get_color(self):
        return self.color
    
    def __str__(self):
        return f"Couleur = {self.color}, Coordonnées = {self.getCoord()}, calcul = {self.texte}"
    
    def bonne_reponse(self, reponse):
        """Renvoie True si la reponse donnée est la bonne"""
        return self.reponse == reponse

class Plateau:
    """Crée le plateau de jeu, "difficulty" est la difficulté du niveau ce qui correspond aux nombres de couches du jeu ;
    "ecran" l'ecran sur lequel s'affiche le Plateau"""
    def __init__(self, difficulty, ecran, centre=(1366/2, 768/2)):
        self.difficulty = difficulty
        self.screen = ecran
        self.alveoles = []
        self.centre = centre
        self.courronnes = [Courronne_Alveole("blue", 1, 1, ecran, self.centre)]
        for indice in range(len(DIFFICULT_COLOR)):
            self.courronnes.append(Courronne_Alveole(DIFFICULT_COLOR[indice], difficulty, self.courronnes[-1].get_epaisseur() + self.courronnes[-1].get_debut(), self.screen, self.centre))
        self.groupe_sprite = pygame.sprite.Group()
        for courrone in self.courronnes:
            self.alveoles += courrone.get_alveoles()
            self.groupe_sprite.add(courrone.get_sprite())
        for alveole in self.alveoles:
            if alveole.get_color() == "blue":
                self.alveole_active = alveole
        self.alveoles_active_voisins = self.alveole_active.get_voisin(self.alveoles)


    def Afficher(self):
        self.screen.fill((200, 0, 0))
        self.groupe_sprite.draw(self.screen)
        for alveole in self.alveoles_active_voisins:
            if alveole.get_texte() == "":
                print(alveole)
            if alveole.get_color() != "blue":
                self.screen.blit(alveole.get_texte(), (alveole.getCoord()[0] + SIDE/2 - len(alveole.get_calcul_str())*6, alveole.getCoord()[1] + SIDE/2 - 10))
        pygame.display.update()

    def get_sprite(self):
        return self.groupe_sprite
    
    def get_alveoles(self):
        return self.alveoles
    
    def get_alveole_with_color(self, color):
        for alveoles in self.alveoles:
            if alveoles.get_color() == color:
                return alveoles

    def get_alveole_with_coordonnee(self, x, y):
        for alveoles in self.alveoles:
            if alveoles.getCoord()[0] == x and alveoles.getCoord()[1] == y:
                return alveoles
            
    def erase_plateau(self):
        self.screen.fill((50, 170, 20))

    def get_centre(self):
        return self.centre

    def Move(self, x, y):
        for alveole in self.alveoles:
            alveole.get_sprite().rect.move_ip(x, y)
        self.Afficher()

    def proche(self, tuple2):
        if (self.centre[0] < tuple2[0] + 10 and self.centre[0] > tuple2[0] - 10) and (self.centre[1] < tuple2[1] + 10 and self.centre[1] > tuple2[1] -10):
            return True

    def change_alveole_active(self, new_alveole):
        self.alveole_active = new_alveole
        new_alveole.set_blue_color()
        self.centrer_alveole(self.alveole_active)
        self.alveoles_active_voisins = self.alveole_active.get_voisin(self.alveoles)
        self.Afficher()

    def centrer_alveole(self, other):
        """other de type alveole"""
        direction = (self.centre[0] - other.get_centre()[0], self.centre[1] - other.get_centre()[1])
        direction_x = direction[0]/10
        direction_y = direction[1]/10
        for _ in range(9):
            self.Move(direction_x, direction_y)
        ecart_finalx = self.centre[0] - other.get_centre()[0]
        ecart_finaly = self.centre[1] - other.get_centre()[1]
        self.Move(ecart_finalx, ecart_finaly)
        
        


class Jeu:
    def __init__(self, difficulte, ecran):
        pass 

##########################################################################################################################################
####################################################################################################################################################
#########################################################################################################################################

class PySprite(pygame.sprite.Sprite):
    def __init__(self, chemin_image, position, point_ancrage=HAUT_GAUCHE, vecteur_vitesse=(0, 0), vecteur_acceleration=(0, 0), *groups):
        assert point_ancrage in ancrages, "erreur : le point d'ancrage doit être parmi " + str(ancrages)
        super().__init__(*groups)
        self.image = pygame.image.load(chemin_image).convert_alpha()
        self.set_vitesse(*vecteur_vitesse)
        self.set_acceleration(*vecteur_acceleration)
        self.placer_sprite(position, point_ancrage)
    
    def placer_sprite(self, position, point_ancrage=HAUT_GAUCHE):
        self.rect = self.image.get_rect(eval(f"{point_ancrage}={position}"))
    
    def changer_image(self, chemin_image):
        self.image = pygame.image.load(chemin_image).convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)
    
    def set_vitesse(self, vitesse_x, vitesse_y):
        self.vecteur_vitesse = pygame.math.Vector2(vitesse_x, vitesse_y)
    
    def set_acceleration(self, acceleration_x, acceleration_y):
        self.vecteur_acceleration = pygame.math.Vector2(acceleration_x, acceleration_y)
    
    def deplacer(self, deplacement_x=0, deplacement_y=0):
        self.rect.x += deplacement_x
        self.rect.y += deplacement_y
    
    def accelerer(self, acceleration_x=0, acceleration_y=0):
        self.vecteur_vitesse.x += acceleration_x
        self.vecteur_vitesse.y += acceleration_y

    def tester_collision(self, autre_sprite):
        return self.rect.colliderect(autre_sprite.rect)

    def update(self):
        self.rect += self.vecteur_vitesse
        self.vecteur_vitesse += self.vecteur_acceleration
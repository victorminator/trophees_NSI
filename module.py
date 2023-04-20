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

CENTRE = "center"
HAUT_GAUCHE = "topleft"
HAUT_DROIT = "topright"
BAS_GAUCHE = "bottomleft"
BAS_DROIT = "bottomright"

ALVEOLE = {"blue" : "alveole_bleue.png", "yellow" : "alveole_jaune.png", "orange" : "alveole_orange.png", "red" : "alveole_rouge.png", "green" : "alveole_verte.png"}
COLOR = ["blue", "green", "yellow", "orange", "red"]

DIFFICULT_COLOR = ["green", "yellow", "orange", "red"]

SIDE =  300 # C'est la taille des alveoles (Le côté de leur image)

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
        if self.side > 1:
            self.coordonnee = Anneau(self.side-1, self.x, self.y)
        else:
            self.coordonnee = [(1366/2 - SIDE/2, 768/2 - SIDE/2)]
        self.alveole = pygame.sprite.Group()
        for coordonnee in self.coordonnee:
            new_alveole = Alveole(coordonnee, self.color, self.screen)
            self.alveole.add(new_alveole.get_sprite())

    def Afficher(self):
        """Affiche à l'écran l'anneau"""
        self.alveole.draw(self.screen)

    def get_sprite(self):
        """Renvoie la liste de tous les sprites qui constituent l'anneau"""
        return self.alveole.sprites()
    
class Courronne_Alveole:
    """Une courronne d'alvéoles et un anneau avec une certaine épaisseur d'alvéoles"""
    def __init__(self, color, epaisseur, debut, ecran, centre=(1366/2, 768/2)):
        self.screen = ecran
        self.color = color
        self.size = epaisseur
        self.begin = debut
        self.centre = centre
        self.anneaux = []
        for indice in range(debut, debut + epaisseur):
            self.anneaux.append(Anneau_Alveole(indice, self.color, self.screen, self.centre))
        self.groupe_sprite = pygame.sprite.Group()
        for anneau in self.anneaux:
            self.groupe_sprite.add(anneau.get_sprite())

    def Afficher(self):
        self.groupe_sprite.draw(self.screen)

    def get_sprite(self):
        return self.groupe_sprite.sprites()
    
    def get_epaisseur(self):
        return self.size
    
    def get_debut(self):
        return self.begin


class Alveole():
    def __init__(self, coordonne, color, ecran, size=(SIDE, SIDE)):
        self.screen = ecran
        image = pygame.image.load(ALVEOLE[color]).convert_alpha() #image d'origine
        self.image = pygame.transform.scale(image, size) #redimension image
        self.groupe_voisin = pygame.sprite.Group()
        self.sprite = pygame.sprite.Sprite()
        self.groupe_voisin.add(self.sprite)
        self.sprite.image = self.image
        self.sprite.rect = self.image.get_rect()
        self.sprite.rect.x = coordonne[0]
        self.sprite.rect.y = coordonne[1]
        self.pos = (self.sprite.rect.x, self.sprite.rect.y)
        self.pos_topleft = (self.sprite.rect.x - self.sprite.rect.height // 2.5, self.sprite.rect.y - self.sprite.rect.width // 1.5)
        self.pos_topright = (self.sprite.rect.x + self.sprite.rect.height // 2.5, self.sprite.rect.y - self.sprite.rect.width // 1.5)
        self.pos_bottomleft = (self.sprite.rect.x - self.sprite.rect.height // 2.5, self.sprite.rect.y + self.sprite.rect.width // 1.5)
        self.pos_bottomright = (self.sprite.rect.x + self.sprite.rect.height // 2.5, self.sprite.rect.y + self.sprite.rect.width // 1.5)
        self.pos_left = (self.sprite.rect.x - self.sprite.rect.height // 1.3, self.sprite.rect.y)
        self.pos_right = (self.sprite.rect.x + self.sprite.rect.height // 1.3, self.sprite.rect.y)
        self.coordonnee_voisin = [self.pos, self.pos_topleft, self.pos_topright, self.pos_right, self.pos_bottomright, self.pos_bottomleft, self.pos_left]
        self.liste_voisin = [self]

    def setCoord(self, x, y):
        self.sprite.rect.x = x
        self.sprite.rect.y = y

    def getCoord(self):
        return (self.sprite.rect.x, self.sprite.rect.y)

    def get_sprite(self):
        return self.sprite
    
    def Afficher(self):
        print(self.sprite.rect.x, self.sprite.rect.y)
        self.groupe_voisin.draw(self.screen)
        

class Plateau:
    """Crée le plateau de jeu, "difficulty" est la difficulté du niveau ce qui correspond aux nombres de couches du jeu ;
    "ecran" l'ecran sur lequel s'affiche le Plateau"""
    def __init__(self, difficulty, ecran):
        self.difficulty = difficulty
        self.screen = ecran
        self.courronnes = [Courronne_Alveole("blue", 1, 1, ecran)]
        for indice in range(len(DIFFICULT_COLOR)):
            self.courronnes.append(Courronne_Alveole(DIFFICULT_COLOR[indice], difficulty, self.courronnes[-1].get_epaisseur() + self.courronnes[-1].get_debut(), self.screen))
        self.groupe_sprite = pygame.sprite.Group()
        for courrone in self.courronnes:
            self.groupe_sprite.add(courrone.get_sprite())

    def Afficher(self):
        self.groupe_sprite.draw(self.screen)

    def get_sprite(self):
        return self.groupe_sprite

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
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
import pygame
from projectile import Projectile


# premier class qui va representer notre joueur
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_healh = 100
        self.attack = 10
        self.velocity = 5
        self.all_projectiles = pygame.sprite.Group()
        self.image = pygame.image.load('assets/MacGyver.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500


    def lanch_projectile(self):
        # cree une nouvelle instance de la classe Projectile
        self.all_projectiles.add(Projectile(self))

    def move_right(self):
        self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity
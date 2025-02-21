import pygame
from classes.Post import Post
from constants import *
from helpers import screen

class ImagePost(Post):
    def _init_(self, username, location, description, img_path, sound=None):
        super()._init_(username, location, description, sound)
        self.img_path = img_path

    def display(self):
        super().display()

        image = pygame.image.load(self.img_path)
        image = pygame.transform.scale(image, (POST_WIDTH, POST_HEIGHT))
        screen.blit(image, (POST_X_POS, POST_Y_POS))
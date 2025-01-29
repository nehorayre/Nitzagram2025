from constants import *
from Post import Post
import pygame


class ImagePost(Post):
    def __init__(self, username, location, description, image_path):
        super().__init__(username, location, description)
        self.image_path = image_path

    def post_display(self):
        img = pygame.image.load(self.image_path)
        img = pygame.transform.scale(img, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img, (POST_X_POS, POST_Y_POS))

from constants import *
from Post import Post
import pygame


class ImagePost(Post):
    def __init__(self, username, location, description):
        super().__init__(username, location, description)


    def image_post(self):
        img_noa = pygame.image.load(IMAGE_PATH_NOA)
        img_noa = pygame.transform.scale(img_noa,(POST_WIDTH , POST_HEIGHT))
        screen.blit(img_noa, (POST_X_POS, POST_Y_POS))

        img_ronaldo = pygame.image.load(IMAGE_PHAT_RONALDO)
        img_ronaldo = pygame.transform.scale(img_ronaldo, (POST_WIDTH, POST_HEIGHT))
        screen.blit(img_ronaldo, (POST_X_POS, POST_Y_POS))
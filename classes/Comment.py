import pygame

from constants import *
from helpers import screen


class Comment:
    def _init_(self, text):
        self.text = text

    def display(self, position_index):
        font = pygame.font.SysFont('chalkduster.ttf', COMMENT_TEXT_SIZE)
        comment_text = font.render(self.text, True, BLACK)
        screen.blit(comment_text, (FIRST_COMMENT_X_POS, FIRST_COMMENT_Y_POS + COMMENT_LINE_HEIGHT * position_index))
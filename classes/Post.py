import pygame

from helpers import screen
from constants import *

class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self, username, location, description): #TODO: add parameters
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

    def add_like(self):
        self.likes_counter = self.likes_counter + 1



    def username_display(self):
        username_font = pygame.font.SysFont("Arial" ,UI_FONT_SIZE)
        username_display = username_font.render(self.username, True, BLACK)
        screen.blit(username_display, [USER_NAME_X_POS, USER_NAME_Y_POS])

    def likes_display(self):

        like_font = pygame.font.SysFont("Arial", LINE_MAX_LENGTH)
        like_display = like_font.render(self.location, True, BLACK)
        screen.blit((like_display, [LIKE_TEXT_X_POS, LIKE_TEXT_Y_POS]))

    def location_display(self):
        location_font = pygame.font.SysFont("Arial" ,UI_FONT_SIZE)
        location_display = location_font.render(self.location, True, BLACK)
        screen.blit((location_display , [LOCATION_TEXT_X_POS, LOCATION_TEXT_Y_POS]))

    def description_display(self):
        description_font = pygame.font.SysFont("Arial", UI_FONT_SIZE)
        description_display = description_font.render(self.description, True, BLACK)
        screen.blit((description_display, [DESCRIPTION_TEXT_X_POS, DESCRIPTION_TEXT_Y_POS]))

    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break




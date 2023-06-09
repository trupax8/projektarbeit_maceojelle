import pygame

from settings import black

def text_object(text, font):
    # Set color of the message
    text_surface = font.render(text, True, black)
    # After that, restart the game and ready to give some input
    return text_surface, text_surface.get_rect()

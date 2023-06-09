import pygame
from settings import display

def background(backgroundleft, backgroundright):
    # Define the position of the background image for the left side in x-axis and y-axis
    display.blit(backgroundleft, (0, 0))
    # Define the position of the background image for the right side in x-axis and y-axis
    display.blit(backgroundright, (700, 0))
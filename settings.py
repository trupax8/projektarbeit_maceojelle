import pygame

# Color code in RGB form
gray = (60, 60, 60)
# Color code in RGB form
black = (255, 0, 0)
# Set width and height of the display
DISPLAY_WIDTH = 830
DISPLAY_HEIGHT = 600
# Set name of the game window
WINDOW_CAPTION = "Racing Game Built with Python"

# Define car image paths
carimg = pygame.image.load("car1.png")
backgroundleft = pygame.image.load("left.png")
backgroundright = pygame.image.load("right.png")
# Define car width
car_width = 23
display = pygame.display.set_mode((830, 600))
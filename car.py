import pygame

def car(x, y, display, carimg):
        # Set position of the car
    display.blit(carimg, (x, y))

def policecar(police_startx, police_starty, police, display):
    if police == 0:
        # Police car no 2
        police_come = pygame.image.load("car2.png")
    elif police == 1:
        # Police car no 3
        police_come = pygame.image.load("car3.png")
    elif police == 2:
        # Police car no 1
        police_come = pygame.image.load("car1.png")
    # Display the police car
    display.blit(police_come, (police_startx, police_starty))
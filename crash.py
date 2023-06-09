import pygame
from text import text_object

def message_display(text, player_rank, difficulty_level):
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
def crash(score, player_rank, difficulty_level):
    message_display("Game Over", player_rank, difficulty_level)
    pygame.time.wait(2000)  # Pause for 2 seconds
    return score
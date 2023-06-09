import pygame
from text import text_object
from settings import display

def message_display(text, player_rank, difficulty_level):
    restart = False

    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Display the game over message
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        text_surf, text_rect = text_object(text, large_text)
        text_rect.center = (400, 200)
        display.blit(text_surf, text_rect)

        # Display the player's rank
        rank_text = pygame.font.Font("freesansbold.ttf", 40)
        rank_surf, rank_rect = text_object(f"Your Rank: {player_rank}", rank_text)
        rank_rect.center = (400, 300)
        display.blit(rank_surf, rank_rect)

        # Draw the restart button
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        restart_surf, restart_rect = text_object("Restart", small_text)
        restart_rect.center = (400, 400)
        display.blit(restart_surf, restart_rect)

        # Check for mouse click events
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 < mouse[0] < 450 and 380 < mouse[1] < 420 and click[0] == 1:
            restart = True

        pygame.display.update()

def crash(score, player_rank, difficulty_level):
    message_display("Game Over", player_rank, difficulty_level)
    pygame.time.wait(2000)  # Pause for 2 seconds
    return score
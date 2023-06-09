import pygame
from text import text_object
from settings import gray
from settings import display

def start_menu(display):
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(gray)
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        title_surf, title_rect = text_object("Racing Game", large_text)
        title_rect.center = (400, 200)
        display.blit(title_surf, title_rect)

        small_text = pygame.font.Font("freesansbold.ttf", 20)
        start_surf, start_rect = text_object("Start", small_text)
        start_rect.center = (400, 300)
        display.blit(start_surf, start_rect)

        scoreboard_surf, scoreboard_rect = text_object("Scoreboard", small_text)
        scoreboard_rect.center = (400, 360)
        display.blit(scoreboard_surf, scoreboard_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 < mouse[0] < 450 and 280 < mouse[1] < 320 and click[0] == 1:
            return "play", get_player_name(display)
        elif 325 < mouse[0] < 475 and 340 < mouse[1] < 380 and click[0] == 1:
            return "scoreboard", None

        pygame.display.update()

def get_player_name(display):
    name = ""
    input_active = True
    while input_active:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    input_active = False
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode

        display.fill(gray)
        large_text = pygame.font.Font("freesansbold.ttf", 40)
        title_surf, title_rect = text_object("Enter Your Name:", large_text)
        title_rect.center = (400, 200)
        display.blit(title_surf, title_rect)

        name_text = pygame.font.Font("freesansbold.ttf", 30)
        name_surf, name_rect = text_object(name, name_text)
        name_rect.center = (400, 300)
        display.blit(name_surf, name_rect)

        pygame.display.update()

    return name

def level_selection(display):
    level = None
    level_selected = False

    while not level_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(gray)
        large_text = pygame.font.Font("freesansbold.ttf", 40)
        title_surf, title_rect = text_object("Select Level", large_text)
        title_rect.center = (400, 100)
        display.blit(title_surf, title_rect)

        small_text = pygame.font.Font("freesansbold.ttf", 20)
        level1_surf, level1_rect = text_object("Level 1", small_text)
        level1_rect.center = (400, 300)
        display.blit(level1_surf, level1_rect)

        level2_surf, level2_rect = text_object("Level 2", small_text)
        level2_rect.center = (400, 360)
        display.blit(level2_surf, level2_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 < mouse[0] < 450 and 280 < mouse[1] < 320 and click[0] == 1:
            level = "level1"
            level_selected = True
        elif 325 < mouse[0] < 475 and 340 < mouse[1] < 380 and click[0] == 1:
            level = "level2"
            level_selected = True

        pygame.display.update()

    return level
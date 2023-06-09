import pygame
import random
from scoreboard import load_scores, save_scores, display_scoreboard
from menu import start_menu, get_player_name, level_selection
from car import car, policecar
from crash import crash
from text import text_object
from background import background
from score import score_display, highest_score_display, update_scores_and_get_rank
from settings import gray
from settings import display
from settings import backgroundleft
from settings import backgroundright
from settings import carimg

def game():
    pygame.init()

    pygame.display.set_caption("Racing Game Built with Python")

    car_width = 23

    game_state = ("menu", None)
    scores = load_scores()

    while True:
        if game_state[0] == "menu":
            game_state = start_menu(display)
        elif game_state[0] == "play":
            level = level_selection(display)
            if level:
                player_name = get_player_name(display)
                if player_name:
                    player_score = loop(display, scores, player_name, level, car_width, backgroundleft, backgroundright)
                    scores[player_name] = player_score
                    save_scores(scores)
                    game_state = ("scoreboard", None)
        elif game_state[0] == "scoreboard":
            display_scoreboard(display, scores)
            game_state = ("menu", None)
        elif game_state[0] == "exit":
            break

def loop(display, scores, player_name, difficulty_level, car_width, backgroundleft, backgroundright):
    x = 400
    y = 540
    x_change = 0
    y_change = 0
    policecar_speed = 9
    if difficulty_level == "level2":
        policecar_speed += 2
    police = 0
    police_startx = random.randrange(130, (700 - car_width))
    police_starty = -600
    police_width = 23
    police_height = 47
    score = 0

    bumped = False
    while not bumped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -1
                if event.key == pygame.K_RIGHT:
                    x_change = 1
            if event.type == pygame.KEYUP:
                x_change = 0
        x += x_change

        display.fill(gray)
        background(display, backgroundleft, backgroundright)
        police_starty -= (policecar_speed / 1.2)
        policecar(police_startx, police_starty, police, display)
        police_starty += policecar_speed
        car(x, y, display, carimg)

        highest_score_display(scores, display)

        if x < 130 or x > 700 - car_width or y < police_starty + police_height:
            if (x > police_startx and x < police_startx + police_width) or (x + car_width > police_startx and x + car_width < police_startx + police_width):
                player_rank = update_scores_and_get_rank(scores, player_name, score, difficulty_level)
                bumped = True
                break

        if police_starty > 600:
            police_starty = 0 - police_height
            police_startx = random.randrange(130, (1000 - 300))
            police = random.randrange(0, 2)
            score += 1

        if y < police_starty + police_height:
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width:
                player_rank = update_scores_and_get_rank(scores, player_name, score, difficulty_level)
                return crash(score, player_rank, difficulty_level)

        score_display(score, display)
        pygame.display.update()
    return crash(score, player_rank, difficulty_level)

def main():
    game()

if __name__ == "__main__":
    main()
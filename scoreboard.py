import pygame
import json
from text import text_object
from settings import gray

def load_scores():
    try:
        with open('scores.json', 'r') as file:
            scores = json.load(file)
            for key in scores:
                if not isinstance(scores[key], dict):
                    scores[key] = {'score': int(scores[key]), 'level': 'level1'}
                else:
                    if isinstance(scores[key]['score'], list):
                        scores[key]['score'] = int(scores[key]['score'][0])
                    else:
                        scores[key]['score'] = int(scores[key]['score'])
    except (FileNotFoundError, json.JSONDecodeError):
        scores = {}
    return scores

def save_scores(scores):
    scores_to_save = {}
    for key, value in scores.items():
        if isinstance(value, dict):
            scores_to_save[key] = {'score': value['score'], 'level': value['level']}
        else:
            scores_to_save[key] = {'score': value, 'level': 'level1'}  # Update 'level1' to the desired default level
    with open('scores.json', 'w') as file:
        json.dump(scores_to_save, file)

def display_scoreboard(scores, display):
    scoreboard = True
    sorted_scores = []
    for name, value in scores.items():
        if isinstance(value, dict):
            sorted_scores.append((name, value))
        else:
            sorted_scores.append((name, {'score': value, 'level': 'level1'}))

    sorted_scores = sorted(sorted_scores, key=lambda x: x[1]['score'], reverse=True)
    small_text = pygame.font.Font("freesansbold.ttf", 20)

    while scoreboard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(gray)

        large_text = pygame.font.Font("freesansbold.ttf", 40)
        title_surf, title_rect = text_object("Scoreboard", large_text)
        title_rect.center = (400, 100)
        display.blit(title_surf, title_rect)

        y_offset = 200
        for name, data in sorted_scores:
            score = data.get('score', 0)
            level = data.get('level', 'level1')
            score_surf, score_rect = text_object(f"{name}: {score}, Level: {level}", small_text)
            score_rect.center = (400, y_offset)
            display.blit(score_surf, score_rect)
            y_offset += 40

        # Draw the return to menu button
        back_surf, back_rect = text_object("Back to Menu", small_text)
        back_rect.center = (400, 500)
        display.blit(back_surf, back_rect)

        # Check for mouse click events
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 300 < mouse[0] < 500 and 480 < mouse[1] < 520 and click[0] == 1:
            scoreboard = False
        pygame.display.update()
import pygame
from settings import black

def score_display(score, display):
    # Set font style and size for the score
    font = pygame.font.Font("freesansbold.ttf", 20)
    # Render the score text
    score_text = font.render(f"Score: {score}", True, black)
    # Display the score text on the screen
    display.blit(score_text, (720, 10))

def highest_score_display(scores, display):
    highest_score = max(scores.values(), key=lambda x: x['score'], default={'score': 0})['score']
    font = pygame.font.Font("freesansbold.ttf", 20)
    highest_score_text = font.render(f"Highscore: {highest_score}", True, black)
    display.blit(highest_score_text, (10, 10))

def update_scores_and_get_rank(scores, player_name, player_score, difficulty_level):
    player_data = scores.get(player_name)
    if player_data is None or not isinstance(player_data, dict):
        player_data = {'score': 0, 'level': 'level1'}
    player_data['score'] = max(player_data.get('score', 0), player_score)
    player_data['level'] = max(player_data.get('level', 'level1'), difficulty_level, key=lambda x: int(x.replace('level', '')))
    scores[player_name] = player_data

    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)
    rank = 1
    for i, (name, data) in enumerate(sorted_scores):
        if name == player_name:
            rank = i + 1
            break

    return rank

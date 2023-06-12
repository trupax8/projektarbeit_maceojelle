import pygame
import random
import json

pygame.init()

gray = (60, 60, 60)
black = (255, 0, 0)
# Festlegen der Breite und Höhe des Displays
display = pygame.display.set_mode((830, 600))
# Namen des Spielefensters festlegen
pygame.display.set_caption("Rennspiel mit Python erstellt")
# Laden des Autobildes
carimg = pygame.image.load("car1.png")
# Laden des Hintergrundbildes für die linke Seite
backgroundleft = pygame.image.load("left.png")
# Laden des Hintergrundbildes für die rechte Seite
backgroundright = pygame.image.load("right.png")
# Breite des Autos festlegen
car_width = 23

def game():
    """
    Die Hauptfunktion des Spiels, die den Spielablauf steuert.
    """
    game_state = ("menu_name", None)
    scores = load_scores()
    player_name = ""
    level = ""

    while True:
        if game_state[0] == "menu_name":
            game_state = start_menu()
            player_name = game_state[1]
        elif game_state[0] == "menu_level":
            game_state = level_selection()
            level = game_state[1]
        elif game_state[0] == "play":
            player_score = loop(scores, player_name, level)
            scores[player_name] = {"score": player_score, "level": level}
            save_scores(scores)
            game_state = ("scoreboard", None)
        elif game_state[0] == "scoreboard":
            game_state = display_scoreboard(scores)
            if game_state[0] == "menu":
                continue
        elif game_state[0] == "exit":
            break

        pygame.display.update()

    pygame.quit()
    quit()

def level_selection():
    """
    Funktion zur Auswahl des Schwierigkeitsgrads.
    Gibt den ausgewählten Schwierigkeitsgrad zurück.
    """
    level = None
    level_selected = False

    while not level_selected:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(gray)
        large_text = pygame.font.Font("freesansbold.ttf", 40)
        title_surf, title_rect = text_object("Wähle das Level", large_text)
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

    return "play", level

def start_menu():
    """
    Funktion zur Anzeige des Startmenüs.
    Gibt den Spielzustand und den ausgewählten Spielernamen zurück.
    """
    menu = True

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        display.fill(gray)
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        title_surf, title_rect = text_object("Car Game", large_text)
        title_rect.center = (400, 200)
        display.blit(title_surf, title_rect)

        small_text = pygame.font.Font("freesansbold.ttf", 20)
        start_surf, start_rect = text_object("Start", small_text)
        start_rect.center = (400, 300)
        display.blit(start_surf, start_rect)

        scoreboard_surf, scoreboard_rect = text_object("Bestenliste", small_text)
        scoreboard_rect.center = (400, 360)
        display.blit(scoreboard_surf, scoreboard_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 < mouse[0] < 450 and 280 < mouse[1] < 320 and click[0] == 1:                           
            return "menu_level", get_player_name()
        elif 325 < mouse[0] < 475 and 340 < mouse[1] < 380 and click[0] == 1:
            return "scoreboard", None

        pygame.display.update()

def load_scores():
    """
    Funktion zum Laden der Bestenliste aus einer JSON-Datei.
    Gibt ein Wörterbuch mit den Spielernamen und Punktzahlen zurück.
    """
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
    """
    Funktion zum Speichern der Bestenliste in einer JSON-Datei.
    """
    for key, value in scores.items():
        if not isinstance(value, dict):
            scores[key] = {'score': value, 'level': 'level1'}
    with open('scores.json', 'w') as file:
        json.dump(scores, file)

def highest_score_display(scores):
    """
    Funktion zum Anzeigen der höchsten Punktzahl in der Bestenliste.
    """
    highest_score = max(scores.values(), key=lambda x: x['score'], default={'score': 0})['score']
    font = pygame.font.Font("freesansbold.ttf", 20)
    highest_score_text = font.render(f"Highscore: {highest_score}", True, black)
    display.blit(highest_score_text, (10, 10))

def get_player_name():
    """
    Funktion zum Eingeben des Spielernamens.
    Gibt den eingegebenen Spielernamen zurück.
    """
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
        title_surf, title_rect = text_object("Gib deinen Namen ein:", large_text)
        title_rect.center = (400, 200)
        display.blit(title_surf, title_rect)

        name_text = pygame.font.Font("freesansbold.ttf", 30)
        name_surf, name_rect = text_object(name, name_text)
        name_rect.center = (400, 300)
        display.blit(name_surf, name_rect)

        pygame.display.update()

    return name

def display_scoreboard(scores):
    scoreboard = True
    sorted_scores = sorted(scores.items(), key=lambda x: x[1]['score'], reverse=True)
    small_text = pygame.font.Font("freesansbold.ttf", 20)

    while scoreboard:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        display.fill(gray)

        large_text = pygame.font.Font("freesansbold.ttf", 40)
        title_surf, title_rect = text_object("Bestenliste", large_text)
        title_rect.center = (400, 100)
        display.blit(title_surf, title_rect)

        y_offset = 200
        for name, data in sorted_scores:
            score = data['score']
            level = data['level']
            score_surf, score_rect = text_object(f"{name}: {score}, Level: {level}", small_text)
            score_rect.center = (400, y_offset)
            display.blit(score_surf, score_rect)
            y_offset += 40

        back_surf, back_rect = text_object("Zurück zum Menü", small_text)
        back_rect.center = (400, 500)
        display.blit(back_surf, back_rect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 < mouse[0] < 450 and 480 < mouse[1] < 520 and click[0] == 1:
            return "menu", None

        pygame.display.update()

def policecar(police_startx, police_starty, police):
    """
    Funktion zum Anzeigen der Polizeiautos, die von der Gegenseite kommen.
    """
    if police == 0:
        police_come = pygame.image.load("car2.png")
    elif police == 1:
        police_come = pygame.image.load("car3.png")
    elif police == 2:
        police_come = pygame.image.load("car1.png")
    
    display.blit(police_come, (police_startx, police_starty))

def background():
    """
    Funktion zum Anzeigen des Hintergrunds.
    """
    display.blit(backgroundleft, (0, 0))
    display.blit(backgroundright, (700, 0))

def crash(player_score, player_rank):
    """
    Funktion zum Anzeigen der Game Over-Nachricht.
    """
    message_display("Game Over", player_rank)
    return player_score

def message_display(text, player_rank):
    """
    Funktion zur Anpassung der Game Over-Nachricht.
    """
    restart = False
    while not restart:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse = pygame.mouse.get_pos()
                if 350 < mouse[0] < 450 and 380 < mouse[1] < 420:
                    restart = True

        # Anzeigen der Game Over-Nachricht
        large_text = pygame.font.Font("freesansbold.ttf", 80)
        text_surf, text_rect = text_object(text, large_text)
        text_rect.center = (400, 200)
        display.blit(text_surf, text_rect)

        # Anzeigen des Spieler-Rangs
        rank_text = pygame.font.Font("freesansbold.ttf", 40)
        rank_surf, rank_rect = text_object(f"Dein Rang: {player_rank}", rank_text)
        rank_rect.center = (400, 300)
        display.blit(rank_surf, rank_rect)

        # Zeichnen des Neustart-Buttons
        small_text = pygame.font.Font("freesansbold.ttf", 20)
        restart_surf, restart_rect = text_object("Neustart", small_text)
        restart_rect.center = (400, 400)
        display.blit(restart_surf, restart_rect)

        # Überprüfe Mausklick-Ereignisse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 350 < mouse[0] < 450 and 380 < mouse[1] < 420 and click[0] == 1:
            restart = True

        pygame.display.update()

def text_object(text, font):
    """
    Funktion zum Rendern von Text.
    """
    # Setze die Farbe des Textes
    text_surface = font.render(text, True, black)
    # Gebe die Oberfläche und das Rechteck des Textes zurück
    return text_surface, text_surface.get_rect()

def car(x, y):
    """
    Funktion zum Anzeigen des Autos.
    """
    display.blit(carimg, (x, y))

def score_display(score):
    """
    Funktion zum Anzeigen der Punktzahl.
    """
    font = pygame.font.Font("freesansbold.ttf", 20)
    score_text = font.render(f"Punktzahl: {score}", True, black)
    display.blit(score_text, (700, 10))

def update_scores_and_get_rank(scores, player_name, player_score, difficulty_level):
    """
    Funktion zum Aktualisieren der Bestenliste und zum Ermitteln des Rangs des Spielers.
    Gibt den erreichten Rang des Spielers zurück.
    """
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

def loop(scores, player_name, difficulty_level):
    """
    Die Hauptschleife des Spiels, in der das Spiel ausgeführt wird.
    Gibt die erreichte Punktzahl zurück.
    """
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
        background()
        police_starty -= (policecar_speed / 1.2)
        policecar(police_startx, police_starty, police)
        police_starty += policecar_speed
        car(x, y)

        highest_score_display(scores)

        if x < 130 or x > 700 - car_width:
            player_rank = update_scores_and_get_rank(scores, player_name, score, difficulty_level)
            score = crash(score, player_rank)
            return score

        if police_starty > 600:
            police_starty = 0 - police_height
            police_startx = random.randrange(130, (1000 - 300))
            police = random.randrange(0, 2)
            score += 1

        if y < police_starty + police_height:
            if x > police_startx and x < police_startx + police_width or x + car_width > police_startx and x + car_width < police_startx + police_width:
                player_rank = update_scores_and_get_rank(scores, player_name, score, difficulty_level)
                score = crash(score, player_rank) 
                return score

        score_display(score)
        pygame.display.update()
    return score

def main():
    """
    Die Hauptfunktion des Programms, die das Spiel startet und beendet.
    """
    game()
    pygame.quit()
    quit()

if __name__ == "__main__":
    main()
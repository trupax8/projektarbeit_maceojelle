while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

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
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    if back_rect and back_rect.collidepoint(event.pos):
                        game_state = ("menu", None)
            elif game_state[0] == "exit":
                pygame.quit()
                quit()
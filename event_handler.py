import pygame


class EventHandler:
    def __init__(self, rl_game):
        self.rl_game = rl_game

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.rl_game.is_running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.rl_game.pause = False if self.rl_game.pause else True
                if self.rl_game.pause:
                    self.handle_keydown_pause_events(event)
            if event.type == pygame.MOUSEBUTTONDOWN and self.rl_game.pause:
                self.rl_game.mouse_draw()
            if event.type == pygame.MOUSEMOTION and self.rl_game.pause:
                if pygame.mouse.get_pressed(3)[0]:
                    self.rl_game.mouse_draw()

    def handle_keydown_pause_events(self, event):
        if event.key == pygame.K_n:
            self.rl_game.update_cells()
        if event.key == pygame.K_c:
            for row in self.rl_game.cells:
                for cell in row:
                    cell.kill()
                    self.rl_game.iterate_over_neighbours(cell)
        if event.key == pygame.K_r:
            self.rl_game.generate_cells()

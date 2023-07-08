import pygame

from .state import State
from src.colors import BLACK


class RunState(State):
    def __init__(self, game, approx_fxn_name) -> None:
        self.game = game
        self.timer = 0
        self.approx_fxn = game.assets['approximations'][approx_fxn_name](self.game.assets['cities'])
        self.approximation_complete = False

        # Identify selected button for drawing
        for button in self.game.assets['buttons']:
            if button.is_highlighted():
                self.title_button = button
                break

    def update(self, dt: float, actions: list) -> None:
        self.timer += dt

        # Run approximation
        if not self.approximation_complete:
            score, self.approximation_complete = self.approx_fxn.run()
            print(score)

        # If complete, allow transition back to main menu
        if actions[1][pygame.K_SPACE]:
            self.game.set_state('transition_to_menu')

    def draw(self) -> None:
        self.game.window.fill(BLACK)

        # Selected menu button
        self.title_button.draw()

        # Map
        self.game.assets['map'].draw()

        pygame.display.update()
        
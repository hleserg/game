from __future__ import annotations

import sys

import pygame

from .config import config
from .games.arkanoid import ArkanoidGame
from .games.pacman import PacmanGame
from .games.snake import SnakeGame
from .games.tetris import TetrisGame
from .ui.menu import MainMenu
from .ui.scores import ScoreManager


class GameCollection:
    def __init__(self) -> None:
        pygame.init()

        # Get display configuration
        display_config = config.get_display_config()
        width = display_config.get("width", 1024)
        height = display_config.get("height", 768)
        fullscreen = display_config.get("fullscreen", False)

        # Set up display
        if fullscreen:
            self.screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((width, height))

        pygame.display.set_caption("Game Collection")
        self.clock = pygame.time.Clock()
        self.running = True

        # Инициализация меню и системы рекордов
        self.score_manager = ScoreManager()
        self.menu = MainMenu(self.screen, self.score_manager)

        # Текущее состояние
        self.current_game: SnakeGame | ArkanoidGame | TetrisGame | PacmanGame | None = None
        self.current_state: str = "menu"  # menu, game, scores

    def run(self) -> None:
        display_config = config.get_display_config()
        fps = display_config.get("fps", 60)

        while self.running:
            dt = self.clock.tick(fps) / 1000.0
            events = pygame.event.get()

            # Обработка глобальных событий
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    if self.current_state == "game":
                        self.return_to_menu()
                    elif self.current_state == "scores":
                        self.current_state = "menu"
                    else:
                        self.running = False

            # Обновление и отрисовка
            if self.current_state == "menu":
                self.menu.handle_events(events)
                self.menu.update(dt)
                self.menu.draw()

                # Проверка выбора игры
                selected_game = self.menu.get_selected_game()
                if selected_game:
                    self.start_game(selected_game)

            elif self.current_state == "game" and self.current_game:
                self.current_game.handle_events(events)
                self.current_game.update(dt)
                self.current_game.draw()

                # Проверка окончания игры
                if self.current_game.is_game_over():
                    score = self.current_game.get_score()
                    game_name = self.current_game.get_game_name()
                    self.score_manager.add_score(game_name, score)
                    self.return_to_menu()

            elif self.current_state == "scores":
                self.menu.draw_scores()

            pygame.display.flip()

        pygame.quit()
        sys.exit()

    def start_game(self, game_name: str) -> None:
        """Запуск выбранной игры"""
        if game_name == "snake":
            self.current_game = SnakeGame(self.screen)
        elif game_name == "arkanoid":
            self.current_game = ArkanoidGame(self.screen)
        elif game_name == "tetris":
            self.current_game = TetrisGame(self.screen)
        elif game_name == "pacman":
            self.current_game = PacmanGame(self.screen)

        self.current_state = "game"

    def return_to_menu(self) -> None:
        """Возврат в главное меню"""
        self.current_game = None
        self.current_state = "menu"
        self.menu.reset_selection()


def main() -> None:
    """Main entry point for the game collection."""
    game = GameCollection()
    game.run()


if __name__ == "__main__":
    main()

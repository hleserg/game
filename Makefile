.PHONY: help install format lint typecheck test test-unit test-cov build clean run

help: ## Показать справку
	@echo "Доступные команды:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}'

install: ## Установить зависимости
	pip install -r requirements.txt

format: ## Форматировать код
	python scripts/format.py

lint: ## Проверить код линтером
	python -m ruff check src/

typecheck: ## Проверить типы
	python -m mypy src/ --ignore-missing-imports

quality: ## Полная проверка качества кода
	python scripts/lint.py

test: ## Запустить тесты импорта
	python -c "import pygame; print('Pygame version:', pygame.version.ver)"
	python -c "from game.games.snake import SnakeGame; print('Snake game imported successfully')"
	python -c "from game.games.arkanoid import ArkanoidGame; print('Arkanoid game imported successfully')"
	python -c "from game.games.tetris import TetrisGame; print('Tetris game imported successfully')"
	python -c "from game.games.pacman import PacmanGame; print('Pac-Man game imported successfully')"
	python -c "from game.ui.menu import MainMenu; print('Main menu imported successfully')"
	@echo "✅ All imports successful!"

test-unit: ## Запустить unit-тесты
	python -m pytest tests/ -v --tb=short

test-cov: ## Запустить тесты с покрытием кода
	python -m pytest tests/ -v --cov=src/game/games --cov-report=term-missing --cov-report=html:htmlcov

build: ## Собрать исполняемый файл
	pip install -e .
	pyinstaller --onefile --windowed --name GameCollection --add-data "src/game/config.json;game" src/game/__main__.py

clean: ## Очистить временные файлы
	rm -rf build/
	rm -rf dist/
	rm -rf __pycache__/
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

run: ## Запустить игру
	python -m game

check: format lint typecheck test ## Выполнить все проверки
	@echo "✅ Все проверки пройдены!"

pre-commit-install: ## Установить pre-commit hooks
	pre-commit install

pre-commit-run: ## Запустить pre-commit на всех файлах
	pre-commit run --all-files

pre-commit-update: ## Обновить pre-commit hooks
	pre-commit autoupdate

.PHONY: quality pre-commit-install pre-commit-run pre-commit-update

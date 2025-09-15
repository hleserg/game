"""Конфигурация pytest для тестов игр."""

import sys
from pathlib import Path

import pytest
import pygame
from unittest.mock import Mock

# Add src directory to Python path
src_path = Path(__file__).parent.parent / "src"
if str(src_path) not in sys.path:
    sys.path.insert(0, str(src_path))


@pytest.fixture(scope="session", autouse=True)
def init_pygame():
    """Инициализация pygame для тестов."""
    pygame.init()
    yield
    pygame.quit()


@pytest.fixture
def mock_screen():
    """Мок экрана для тестов."""
    screen = Mock()
    screen.get_size.return_value = (800, 600)
    return screen


@pytest.fixture
def mock_surface():
    """Мок поверхности pygame."""
    surface = Mock()
    surface.get_size.return_value = (800, 600)
    return surface

# 🛠️ Руководство разработчика

Этот документ описывает процесс разработки и поддержания качества кода в коллекции игр.

## 🚀 Быстрый старт

### Установка зависимостей
```bash
make install
# или
pip install -r requirements.txt
```

### Запуск игры
```bash
make run
# или
python main.py
```

## 🔧 Инструменты разработки

### Ruff - Линтер и форматтер
Ruff заменяет flake8, isort, pyupgrade и другие инструменты. Очень быстрый!

```bash
# Форматирование кода
make format
# или
ruff format .

# Проверка кода
make lint
# или
ruff check .
```

### mypy - Проверка типов
Помогает ловить ошибки в логике игр (коллизии, состояния).

```bash
# Проверка типов
make typecheck
# или
mypy .
```

### Makefile команды
```bash
make help          # Показать все команды
make install       # Установить зависимости
make format        # Форматировать код
make lint          # Проверить код линтером
make typecheck     # Проверить типы
make test          # Запустить тесты
make build         # Собрать exe
make clean         # Очистить временные файлы
make run           # Запустить игру
make check         # Выполнить все проверки
```

## 📋 Стандарты кода

### Типизация
- Все функции должны иметь аннотации типов
- Используйте `from __future__ import annotations` для forward references
- Импорты типов: `from typing import Optional, Union, List, Dict`

### Форматирование
- Максимальная длина строки: 100 символов
- Автоматическое форматирование с помощью Ruff
- Сортировка импортов автоматически

### Структура проекта
```
game/
├── main.py              # Главный файл
├── games/               # Игры
│   ├── base.py          # Базовый класс игры
│   ├── snake.py         # Змейка
│   ├── arkanoid.py      # Арканоид
│   ├── tetris.py        # Тетрис
│   └── pacman.py        # Pac-Man
├── ui/                  # Интерфейс
├── scripts/             # Скрипты разработки
├── .github/workflows/   # CI/CD
└── pyproject.toml       # Конфигурация инструментов
```

## 🧪 Тестирование

### Локальное тестирование
```bash
make test
```

### CI/CD тестирование
GitHub Actions автоматически:
- Проверяет форматирование кода
- Запускает линтер
- Проверяет типы
- Тестирует импорты
- Собирает исполняемые файлы

## 🎮 Разработка игр

### Базовый класс игры
Все игры наследуются от `BaseGame`:

```python
from games.base import BaseGame

class MyGame(BaseGame):
    def handle_events(self, events: List[pygame.event.Event]) -> None:
        # Обработка событий
        pass

    def update(self, dt: float) -> None:
        # Обновление логики
        pass

    def draw(self) -> None:
        # Отрисовка
        pass

    def is_game_over(self) -> bool:
        # Проверка окончания
        return False

    def get_score(self) -> int:
        # Возврат счета
        return 0

    def get_game_name(self) -> str:
        # Название игры
        return "My Game"
```

### Типизация игровых объектов
```python
from typing import List, Tuple, Optional

# Позиция
Position = Tuple[int, int]

# Список позиций
SnakeBody = List[Position]

# Опциональный объект
Bomb: Optional[Position] = None
```

## 🚀 Сборка и релизы

### Локальная сборка
```bash
make build
```

### Автоматические релизы
1. Создайте тег: `git tag v1.0.0`
2. Запушьте тег: `git push origin v1.0.0`
3. GitHub Actions автоматически создаст релиз

## 📝 Коммиты

### Формат коммитов
```
тип: краткое описание

Подробное описание изменений

- Список изменений
- Дополнительные детали
```

### Типы коммитов
- `feat`: новая функция
- `fix`: исправление бага
- `docs`: документация
- `style`: форматирование
- `refactor`: рефакторинг
- `test`: тесты
- `ci`: CI/CD

## 🔍 Отладка

### Проверка качества кода
```bash
make check
```

### Отладка типов
```bash
mypy --strict .
```

### Отладка импортов
```bash
python -c "import games.snake; print('OK')"
```

## 📚 Полезные ссылки

- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Type Hints](https://docs.python.org/3/library/typing.html)

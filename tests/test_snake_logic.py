"""Тесты для логики змейки."""

from game.games.logic import (
    check_food_collision,
    generate_food_position,
    move_snake,
)


class TestSnakeMovement:
    """Тесты движения змейки."""

    def test_move_snake_right(self):
        """Тест движения змейки вправо."""
        snake = [(5, 5), (4, 5), (3, 5)]
        direction = (1, 0)  # Вправо

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == [(6, 5), (5, 5), (4, 5)]
        assert collision is False

    def test_move_snake_down(self):
        """Тест движения змейки вниз."""
        snake = [(5, 5), (5, 4), (5, 3)]
        direction = (0, 1)  # Вниз

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == [(5, 6), (5, 5), (5, 4)]
        assert collision is False

    def test_move_snake_left(self):
        """Тест движения змейки влево."""
        snake = [(5, 5), (6, 5), (7, 5)]
        direction = (-1, 0)  # Влево

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == [(4, 5), (5, 5), (6, 5)]
        assert collision is False

    def test_move_snake_up(self):
        """Тест движения змейки вверх."""
        snake = [(5, 5), (5, 6), (5, 7)]
        direction = (0, -1)  # Вверх

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == [(5, 4), (5, 5), (5, 6)]
        assert collision is False

    def test_move_snake_collision_wall_left(self):
        """Тест столкновения змейки с левой стеной."""
        snake = [(0, 5), (1, 5), (2, 5)]
        direction = (-1, 0)  # Влево

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == snake  # Змейка не изменилась
        assert collision is True

    def test_move_snake_collision_wall_right(self):
        """Тест столкновения змейки с правой стеной."""
        snake = [(9, 5), (8, 5), (7, 5)]
        direction = (1, 0)  # Вправо

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == snake
        assert collision is True

    def test_move_snake_collision_wall_top(self):
        """Тест столкновения змейки с верхней стеной."""
        snake = [(5, 0), (5, 1), (5, 2)]
        direction = (0, -1)  # Вверх

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == snake
        assert collision is True

    def test_move_snake_collision_wall_bottom(self):
        """Тест столкновения змейки с нижней стеной."""
        snake = [(5, 9), (5, 8), (5, 7)]
        direction = (0, 1)  # Вниз

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == snake
        assert collision is True

    def test_move_snake_collision_self(self):
        """Тест столкновения змейки с собой."""
        snake = [(5, 5), (4, 5), (3, 5), (3, 4), (3, 3), (4, 3), (5, 3), (5, 4)]
        direction = (0, -1)  # Вверх (голова попадет на позицию тела)

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == snake
        assert collision is True

    def test_move_snake_empty(self):
        """Тест движения пустой змейки."""
        snake = []
        direction = (1, 0)

        new_snake, collision = move_snake(snake, direction, 10, 10)

        assert new_snake == []
        assert collision is True


class TestFoodCollision:
    """Тесты столкновения с едой."""

    def test_food_collision_head_on_food(self):
        """Тест столкновения головы змейки с едой."""
        snake = [(5, 5), (4, 5), (3, 5)]
        food = (5, 5)

        assert check_food_collision(snake, food) is True

    def test_food_collision_head_not_on_food(self):
        """Тест когда голова змейки не на еде."""
        snake = [(5, 5), (4, 5), (3, 5)]
        food = (6, 5)

        assert check_food_collision(snake, food) is False

    def test_food_collision_empty_snake(self):
        """Тест столкновения с едой для пустой змейки."""
        snake = []
        food = (5, 5)

        assert check_food_collision(snake, food) is False

    def test_food_collision_no_food(self):
        """Тест когда еды нет."""
        snake = [(5, 5), (4, 5), (3, 5)]
        food = None

        assert check_food_collision(snake, food) is False


class TestFoodGeneration:
    """Тесты генерации позиции еды."""

    def test_generate_food_empty_grid(self):
        """Тест генерации еды в пустой сетке."""
        snake = [(5, 5), (4, 5), (3, 5)]

        food_pos = generate_food_position(snake, 10, 10)

        assert food_pos is not None
        assert food_pos not in snake
        x, y = food_pos
        assert 0 <= x < 10
        assert 0 <= y < 10

    def test_generate_food_with_existing_items(self):
        """Тест генерации еды с учетом существующих предметов."""
        snake = [(5, 5), (4, 5), (3, 5)]
        existing_items = [(6, 6), (7, 7)]

        food_pos = generate_food_position(snake, 10, 10, existing_items)

        assert food_pos is not None
        assert food_pos not in snake
        assert food_pos not in existing_items
        x, y = food_pos
        assert 0 <= x < 10
        assert 0 <= y < 10

    def test_generate_food_almost_full_grid(self):
        """Тест генерации еды в почти заполненной сетке."""
        # Заполняем почти всю сетку
        snake = [(x, y) for x in range(10) for y in range(10) if (x, y) != (5, 5)]

        food_pos = generate_food_position(snake, 10, 10)

        # Проверяем, что еда размещена в единственном свободном месте
        assert food_pos is not None
        assert food_pos == (5, 5)  # Единственное свободное место

    def test_generate_food_full_grid(self):
        """Тест генерации еды в полностью заполненной сетке."""
        # Заполняем всю сетку
        snake = [(x, y) for x in range(10) for y in range(10)]

        food_pos = generate_food_position(snake, 10, 10)

        assert food_pos is None  # Нет свободных мест

    def test_generate_food_small_grid(self):
        """Тест генерации еды в маленькой сетке."""
        snake = [(0, 0), (1, 0)]

        food_pos = generate_food_position(snake, 2, 2)

        assert food_pos is not None
        assert food_pos not in snake
        # Должна быть одна из двух свободных позиций: (0, 1) или (1, 1)
        assert food_pos in [(0, 1), (1, 1)]

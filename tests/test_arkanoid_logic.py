"""Тесты для логики арканоида."""

import pygame

from game.games.logic import (
    calculate_ball_reflection,
    check_block_collision,
)


class TestBallReflection:
    """Тесты отскока мяча от платформы."""

    def test_ball_reflection_center_paddle(self):
        """Тест отскока мяча от центра платформы."""
        ball_x, ball_y = 100.0, 245.0  # Ближе к платформе
        ball_speed_x, ball_speed_y = 2.0, 5.0
        ball_radius = 8
        paddle_x, paddle_y = 50.0, 250.0
        paddle_width, paddle_height = 100, 15

        new_x, new_y, new_speed_x, new_speed_y = calculate_ball_reflection(
            ball_x,
            ball_y,
            ball_speed_x,
            ball_speed_y,
            ball_radius,
            paddle_x,
            paddle_y,
            paddle_width,
            paddle_height,
        )

        # Мяч должен отскочить вертикально (угол = 0)
        assert abs(new_speed_x) < 0.1  # Почти вертикально
        assert new_speed_y < 0  # Должен двигаться вверх
        assert new_y == paddle_y - ball_radius  # Корректная позиция

    def test_ball_reflection_left_edge_paddle(self):
        """Тест отскока мяча от левого края платформы."""
        ball_x, ball_y = 60.0, 245.0  # Ближе к левому краю и платформе
        ball_speed_x, ball_speed_y = 2.0, 5.0
        ball_radius = 8
        paddle_x, paddle_y = 50.0, 250.0
        paddle_width, paddle_height = 100, 15

        new_x, new_y, new_speed_x, new_speed_y = calculate_ball_reflection(
            ball_x,
            ball_y,
            ball_speed_x,
            ball_speed_y,
            ball_radius,
            paddle_x,
            paddle_y,
            paddle_width,
            paddle_height,
        )

        # Мяч должен отскочить влево
        assert new_speed_x < 0
        assert new_speed_y < 0
        assert new_y == paddle_y - ball_radius

    def test_ball_reflection_right_edge_paddle(self):
        """Тест отскока мяча от правого края платформы."""
        ball_x, ball_y = 140.0, 245.0  # Ближе к правому краю и платформе
        ball_speed_x, ball_speed_y = 2.0, 5.0
        ball_radius = 8
        paddle_x, paddle_y = 50.0, 250.0
        paddle_width, paddle_height = 100, 15

        new_x, new_y, new_speed_x, new_speed_y = calculate_ball_reflection(
            ball_x,
            ball_y,
            ball_speed_x,
            ball_speed_y,
            ball_radius,
            paddle_x,
            paddle_y,
            paddle_width,
            paddle_height,
        )

        # Мяч должен отскочить вправо
        assert new_speed_x > 0
        assert new_speed_y < 0
        assert new_y == paddle_y - ball_radius

    def test_ball_reflection_no_collision(self):
        """Тест когда мяч не сталкивается с платформой."""
        ball_x, ball_y = 200.0, 200.0  # Далеко от платформы
        ball_speed_x, ball_speed_y = 2.0, 5.0
        ball_radius = 8
        paddle_x, paddle_y = 50.0, 250.0
        paddle_width, paddle_height = 100, 15

        new_x, new_y, new_speed_x, new_speed_y = calculate_ball_reflection(
            ball_x,
            ball_y,
            ball_speed_x,
            ball_speed_y,
            ball_radius,
            paddle_x,
            paddle_y,
            paddle_width,
            paddle_height,
        )

        # Параметры не должны измениться
        assert new_x == ball_x
        assert new_y == ball_y
        assert new_speed_x == ball_speed_x
        assert new_speed_y == ball_speed_y

    def test_ball_reflection_upward_motion(self):
        """Тест отскока мяча, движущегося вверх."""
        ball_x, ball_y = 100.0, 200.0
        ball_speed_x, ball_speed_y = 2.0, -5.0  # Движется вверх
        ball_radius = 8
        paddle_x, paddle_y = 50.0, 250.0
        paddle_width, paddle_height = 100, 15

        new_x, new_y, new_speed_x, new_speed_y = calculate_ball_reflection(
            ball_x,
            ball_y,
            ball_speed_x,
            ball_speed_y,
            ball_radius,
            paddle_x,
            paddle_y,
            paddle_width,
            paddle_height,
        )

        # Мяч движется вверх, поэтому отскока не должно быть
        assert new_x == ball_x
        assert new_y == ball_y
        assert new_speed_x == ball_speed_x
        assert new_speed_y == ball_speed_y


class TestBlockCollision:
    """Тесты столкновения мяча с блоками."""

    def test_block_collision_hit_block(self):
        """Тест попадания мяча в блок."""
        ball_x, ball_y = 100.0, 100.0
        ball_speed_x, ball_speed_y = 5.0, 5.0
        ball_radius = 8

        blocks = [
            {"rect": pygame.Rect(90, 90, 20, 20), "destroyed": False, "points": 10},
            {"rect": pygame.Rect(120, 90, 20, 20), "destroyed": False, "points": 10},
        ]

        collision, new_blocks, score = check_block_collision(
            ball_x, ball_y, ball_speed_x, ball_speed_y, ball_radius, blocks
        )

        assert collision is True
        assert new_blocks[0]["destroyed"] is True
        assert new_blocks[1]["destroyed"] is False
        assert score == 10

    def test_block_collision_no_hit(self):
        """Тест когда мяч не попадает в блоки."""
        ball_x, ball_y = 200.0, 200.0  # Далеко от блоков
        ball_speed_x, ball_speed_y = 5.0, 5.0
        ball_radius = 8

        blocks = [{"rect": pygame.Rect(90, 90, 20, 20), "destroyed": False, "points": 10}]

        collision, new_blocks, score = check_block_collision(
            ball_x, ball_y, ball_speed_x, ball_speed_y, ball_radius, blocks
        )

        assert collision is False
        assert new_blocks[0]["destroyed"] is False
        assert score == 0

    def test_block_collision_already_destroyed(self):
        """Тест столкновения с уже уничтоженным блоком."""
        ball_x, ball_y = 100.0, 100.0
        ball_speed_x, ball_speed_y = 5.0, 5.0
        ball_radius = 8

        blocks = [
            {
                "rect": pygame.Rect(90, 90, 20, 20),
                "destroyed": True,  # Уже уничтожен
                "points": 10,
            }
        ]

        collision, new_blocks, score = check_block_collision(
            ball_x, ball_y, ball_speed_x, ball_speed_y, ball_radius, blocks
        )

        assert collision is False
        assert new_blocks[0]["destroyed"] is True
        assert score == 0

    def test_block_collision_multiple_blocks(self):
        """Тест столкновения с несколькими блоками (должен попасть в первый)."""
        ball_x, ball_y = 100.0, 100.0
        ball_speed_x, ball_speed_y = 5.0, 5.0
        ball_radius = 8

        blocks = [
            {"rect": pygame.Rect(90, 90, 20, 20), "destroyed": False, "points": 10},
            {
                "rect": pygame.Rect(95, 95, 20, 20),  # Перекрывается с первым
                "destroyed": False,
                "points": 20,
            },
        ]

        collision, new_blocks, score = check_block_collision(
            ball_x, ball_y, ball_speed_x, ball_speed_y, ball_radius, blocks
        )

        assert collision is True
        assert new_blocks[0]["destroyed"] is True
        assert new_blocks[1]["destroyed"] is False  # Второй блок не затронут
        assert score == 10  # Очки только за первый блок

    def test_block_collision_edge_case(self):
        """Тест граничного случая столкновения."""
        ball_x, ball_y = 110.0, 110.0  # Край блока
        ball_speed_x, ball_speed_y = 5.0, 5.0
        ball_radius = 8

        blocks = [{"rect": pygame.Rect(100, 100, 20, 20), "destroyed": False, "points": 10}]

        collision, new_blocks, score = check_block_collision(
            ball_x, ball_y, ball_speed_x, ball_speed_y, ball_radius, blocks
        )

        assert collision is True
        assert new_blocks[0]["destroyed"] is True
        assert score == 10

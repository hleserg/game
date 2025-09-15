"""Тесты для логики тетриса."""

from game.games.logic import (
    calculate_tetris_score,
    clear_tetris_lines,
    is_valid_tetris_position,
    place_tetris_piece,
    rotate_tetris_piece,
)


class TestTetrisPieceRotation:
    """Тесты поворота фигур тетриса."""

    def test_rotate_i_piece(self):
        """Тест поворота I-фигуры."""
        i_shape = [
            [".....", "..#..", "..#..", "..#..", "..#.."],
            [".....", ".....", "####.", ".....", "....."],
        ]

        # Поворот 0 (исходное положение)
        rotated = rotate_tetris_piece(i_shape, 0)
        assert rotated == [".....", "..#..", "..#..", "..#..", "..#.."]

        # Поворот 1 (горизонтально)
        rotated = rotate_tetris_piece(i_shape, 1)
        assert rotated == [".....", ".....", "####.", ".....", "....."]

        # Поворот 2 (обратно к вертикальному)
        rotated = rotate_tetris_piece(i_shape, 2)
        assert rotated == [".....", "..#..", "..#..", "..#..", "..#.."]

    def test_rotate_o_piece(self):
        """Тест поворота O-фигуры (не должна поворачиваться)."""
        o_shape = [[".....", ".....", ".##..", ".##..", "....."]]

        rotated = rotate_tetris_piece(o_shape, 0)
        assert rotated == [".....", ".....", ".##..", ".##..", "....."]

        rotated = rotate_tetris_piece(o_shape, 1)
        assert rotated == [".....", ".....", ".##..", ".##..", "....."]

    def test_rotate_t_piece(self):
        """Тест поворота T-фигуры."""
        t_shape = [
            [".....", ".....", ".#...", "###..", "....."],
            [".....", ".....", ".#...", ".##..", ".#..."],
            [".....", ".....", ".....", "###..", ".#..."],
            [".....", ".....", ".#...", "##...", ".#..."],
        ]

        # Все 4 поворота
        for i in range(4):
            rotated = rotate_tetris_piece(t_shape, i)
            assert rotated == t_shape[i]


class TestTetrisPositionValidation:
    """Тесты проверки позиций фигур."""

    def test_valid_position_in_empty_grid(self):
        """Тест валидной позиции в пустой сетке."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        shape = [".....", "..#..", "..#..", "..#..", "..#.."]  # I-фигура вертикально

        assert is_valid_tetris_position(shape, 5, 0, 10, 20, grid) is True

    def test_invalid_position_out_of_bounds_left(self):
        """Тест невалидной позиции за левой границей."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        shape = [".....", "..#..", "..#..", "..#..", "..#.."]

        assert is_valid_tetris_position(shape, -3, 0, 10, 20, grid) is False

    def test_invalid_position_out_of_bounds_right(self):
        """Тест невалидной позиции за правой границей."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        shape = [".....", ".....", "####.", ".....", "....."]  # I-фигура горизонтально

        assert is_valid_tetris_position(shape, 7, 0, 10, 20, grid) is False

    def test_invalid_position_out_of_bounds_bottom(self):
        """Тест невалидной позиции за нижней границей."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        shape = [".....", "..#..", "..#..", "..#..", "..#.."]

        assert is_valid_tetris_position(shape, 5, 17, 10, 20, grid) is False

    def test_invalid_position_collision_with_blocks(self):
        """Тест невалидной позиции при столкновении с блоками."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        grid[5][5] = 1  # Блок на позиции (5, 5)
        shape = [".....", "..#..", "..#..", "..#..", "..#.."]

        assert is_valid_tetris_position(shape, 3, 3, 10, 20, grid) is False

    def test_valid_position_above_blocks(self):
        """Тест валидной позиции над блоками."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        grid[5][5] = 1  # Блок на позиции (5, 5)
        shape = [".....", "..#..", "..#..", "..#..", "..#.."]

        assert is_valid_tetris_position(shape, 4, 1, 10, 20, grid) is True


class TestTetrisPiecePlacement:
    """Тесты размещения фигур."""

    def test_place_piece_in_empty_grid(self):
        """Тест размещения фигуры в пустой сетке."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        shape = [".....", "..#..", "..#..", "..#..", "..#.."]

        new_grid = place_tetris_piece(shape, 5, 0, 1, grid)

        # Проверяем, что фигура размещена правильно
        assert new_grid[1][7] == 1  # Первый блок
        assert new_grid[2][7] == 1  # Второй блок
        assert new_grid[3][7] == 1  # Третий блок
        assert new_grid[4][7] == 1  # Четвертый блок

        # Проверяем, что остальные клетки не изменились
        assert new_grid[0][7] == 0  # Пустая клетка выше
        assert new_grid[5][7] == 0  # Пустая клетка ниже

        # Проверяем, что оригинальная сетка не изменилась
        assert grid[1][5] == 0

    def test_place_piece_partially_above_grid(self):
        """Тест размещения фигуры частично выше сетки."""
        grid = [[0 for _ in range(10)] for _ in range(20)]
        shape = [".....", "..#..", "..#..", "..#..", "..#.."]

        new_grid = place_tetris_piece(shape, 5, -1, 1, grid)

        # Проверяем, что только видимые части размещены
        assert new_grid[0][7] == 1  # Первый видимый блок
        assert new_grid[1][7] == 1  # Второй блок
        assert new_grid[2][7] == 1  # Третий блок
        assert new_grid[3][7] == 1  # Четвертый блок


class TestTetrisLineClearing:
    """Тесты очистки линий."""

    def test_clear_single_line(self):
        """Тест очистки одной линии."""
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Пустая линия
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Полная линия
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # Частично заполненная
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Пустая линия
        ]

        new_grid, lines_cleared = clear_tetris_lines(grid)

        assert lines_cleared == 1
        assert len(new_grid) == 4  # Количество линий не изменилось
        assert new_grid[0] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Новая пустая линия сверху
        assert new_grid[1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Бывшая пустая линия
        assert new_grid[2] == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # Частично заполненная сдвинулась вниз

    def test_clear_multiple_lines(self):
        """Тест очистки нескольких линий."""
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # Пустая линия
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Полная линия 1
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],  # Полная линия 2
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],  # Частично заполненная
        ]

        new_grid, lines_cleared = clear_tetris_lines(grid)

        assert lines_cleared == 2
        assert len(new_grid) == 4
        # Две новые пустые линии сверху
        assert new_grid[0] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert new_grid[1] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        assert new_grid[2] == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]  # Бывшая пустая линия
        assert new_grid[3] == [0, 1, 0, 1, 0, 1, 0, 1, 0, 1]  # Частично заполненная сдвинулась вниз

    def test_clear_no_lines(self):
        """Тест когда нет линий для очистки."""
        grid = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]

        new_grid, lines_cleared = clear_tetris_lines(grid)

        assert lines_cleared == 0
        assert new_grid == grid  # Сетка не изменилась


class TestTetrisScoreCalculation:
    """Тесты расчета очков."""

    def test_score_no_lines(self):
        """Тест очков за 0 линий."""
        assert calculate_tetris_score(0, 1) == 0
        assert calculate_tetris_score(0, 5) == 0

    def test_score_single_line(self):
        """Тест очков за 1 линию."""
        assert calculate_tetris_score(1, 1) == 100
        assert calculate_tetris_score(1, 2) == 200
        assert calculate_tetris_score(1, 5) == 500

    def test_score_multiple_lines(self):
        """Тест очков за несколько линий."""
        assert calculate_tetris_score(2, 1) == 200
        assert calculate_tetris_score(3, 2) == 600
        assert calculate_tetris_score(4, 3) == 1200

    def test_score_tetris(self):
        """Тест очков за тетрис (4 линии)."""
        assert calculate_tetris_score(4, 1) == 400
        assert calculate_tetris_score(4, 5) == 2000

"""Тесты для логики пакмана."""

from game.games.logic import (
    check_dot_collision,
    check_ghost_collision,
    get_next_maze_position,
    is_valid_maze_position,
    remove_dot_from_maze,
)


class TestMazePositionValidation:
    """Тесты проверки валидности позиций в лабиринте."""

    def test_valid_position_empty_space(self):
        """Тест валидной позиции в пустом пространстве."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert is_valid_maze_position(1, 1, maze, 5, 5) is True
        assert is_valid_maze_position(2, 2, maze, 5, 5) is True
        assert is_valid_maze_position(3, 3, maze, 5, 5) is True

    def test_invalid_position_wall(self):
        """Тест невалидной позиции в стене."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert is_valid_maze_position(0, 0, maze, 5, 5) is False
        assert is_valid_maze_position(4, 4, maze, 5, 5) is False
        assert is_valid_maze_position(0, 2, maze, 5, 5) is False

    def test_invalid_position_out_of_bounds(self):
        """Тест невалидной позиции за границами лабиринта."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert is_valid_maze_position(-1, 2, maze, 5, 5) is False
        assert is_valid_maze_position(5, 2, maze, 5, 5) is False
        assert is_valid_maze_position(2, -1, maze, 5, 5) is False
        assert is_valid_maze_position(2, 5, maze, 5, 5) is False

    def test_valid_position_on_dot(self):
        """Тест валидной позиции на точке."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert is_valid_maze_position(2, 2, maze, 5, 5) is True


class TestMazePositionMovement:
    """Тесты движения по лабиринту."""

    def test_move_right(self):
        """Тест движения вправо."""
        x, y = get_next_maze_position(2, 2, 0)  # direction 0 = right
        assert x == 3
        assert y == 2

    def test_move_down(self):
        """Тест движения вниз."""
        x, y = get_next_maze_position(2, 2, 1)  # direction 1 = down
        assert x == 2
        assert y == 3

    def test_move_left(self):
        """Тест движения влево."""
        x, y = get_next_maze_position(2, 2, 2)  # direction 2 = left
        assert x == 1
        assert y == 2

    def test_move_up(self):
        """Тест движения вверх."""
        x, y = get_next_maze_position(2, 2, 3)  # direction 3 = up
        assert x == 2
        assert y == 1

    def test_move_all_directions(self):
        """Тест движения во всех направлениях."""
        start_x, start_y = 5, 5

        # right
        x, y = get_next_maze_position(start_x, start_y, 0)
        assert x == start_x + 1 and y == start_y

        # down
        x, y = get_next_maze_position(start_x, start_y, 1)
        assert x == start_x and y == start_y + 1

        # left
        x, y = get_next_maze_position(start_x, start_y, 2)
        assert x == start_x - 1 and y == start_y

        # up
        x, y = get_next_maze_position(start_x, start_y, 3)
        assert x == start_x and y == start_y - 1


class TestDotCollision:
    """Тесты столкновения с точками."""

    def test_dot_collision_on_dot(self):
        """Тест столкновения с точкой."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert check_dot_collision(2, 2, maze) is True

    def test_dot_collision_empty_space(self):
        """Тест отсутствия столкновения в пустом пространстве."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert check_dot_collision(1, 1, maze) is False
        assert check_dot_collision(3, 3, maze) is False

    def test_dot_collision_wall(self):
        """Тест отсутствия столкновения в стене."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert check_dot_collision(0, 0, maze) is False
        assert check_dot_collision(4, 4, maze) is False

    def test_dot_collision_out_of_bounds(self):
        """Тест столкновения за границами лабиринта."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        assert check_dot_collision(-1, 2, maze) is False
        assert check_dot_collision(5, 2, maze) is False


class TestDotRemoval:
    """Тесты удаления точек из лабиринта."""

    def test_remove_dot_success(self):
        """Тест успешного удаления точки."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        new_maze = remove_dot_from_maze(2, 2, maze)

        assert new_maze[2][2] == 0  # Точка удалена
        assert new_maze[1][1] == 0  # Остальные клетки не изменились
        assert maze[2][2] == 2  # Оригинальный лабиринт не изменился

    def test_remove_dot_empty_space(self):
        """Тест удаления точки из пустого пространства."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        new_maze = remove_dot_from_maze(1, 1, maze)

        assert new_maze[1][1] == 0  # Пустое пространство остается пустым
        assert new_maze[2][2] == 2  # Точка не затронута

    def test_remove_dot_out_of_bounds(self):
        """Тест удаления точки за границами лабиринта."""
        maze = [
            [1, 1, 1, 1, 1],
            [1, 0, 0, 0, 1],
            [1, 0, 2, 0, 1],
            [1, 0, 0, 0, 1],
            [1, 1, 1, 1, 1],
        ]

        new_maze = remove_dot_from_maze(-1, 2, maze)

        # Лабиринт не должен измениться
        assert new_maze == maze


class TestGhostCollision:
    """Тесты столкновения с призраками."""

    def test_ghost_collision_chase_mode(self):
        """Тест столкновения с призраком в режиме преследования."""
        ghosts = [
            {"x": 5, "y": 5, "mode": "chase"},
            {"x": 3, "y": 3, "mode": "scatter"},
        ]

        collision, mode = check_ghost_collision(5, 5, ghosts)

        assert collision is True
        assert mode == "chase"

    def test_ghost_collision_frightened_mode(self):
        """Тест столкновения с призраком в испуганном режиме."""
        ghosts = [
            {"x": 5, "y": 5, "mode": "frightened"},
            {"x": 3, "y": 3, "mode": "chase"},
        ]

        collision, mode = check_ghost_collision(5, 5, ghosts)

        assert collision is True
        assert mode == "frightened"

    def test_ghost_collision_scatter_mode(self):
        """Тест столкновения с призраком в режиме разброса."""
        ghosts = [
            {"x": 5, "y": 5, "mode": "scatter"},
        ]

        collision, mode = check_ghost_collision(5, 5, ghosts)

        assert collision is True
        assert mode == "scatter"

    def test_no_ghost_collision(self):
        """Тест отсутствия столкновения с призраками."""
        ghosts = [
            {"x": 3, "y": 3, "mode": "chase"},
            {"x": 7, "y": 7, "mode": "scatter"},
        ]

        collision, mode = check_ghost_collision(5, 5, ghosts)

        assert collision is False
        assert mode == ""

    def test_ghost_collision_empty_list(self):
        """Тест столкновения с пустым списком призраков."""
        ghosts = []

        collision, mode = check_ghost_collision(5, 5, ghosts)

        assert collision is False
        assert mode == ""

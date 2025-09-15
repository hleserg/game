"""Тесты для общих утилит."""

import math

from game.games.logic import (
    calculate_distance,
    clamp,
    normalize_vector,
)


class TestDistanceCalculation:
    """Тесты расчета расстояния."""

    def test_distance_same_point(self):
        """Тест расстояния до той же точки."""
        distance = calculate_distance(5.0, 5.0, 5.0, 5.0)
        assert distance == 0.0

    def test_distance_horizontal(self):
        """Тест горизонтального расстояния."""
        distance = calculate_distance(0.0, 0.0, 3.0, 0.0)
        assert distance == 3.0

    def test_distance_vertical(self):
        """Тест вертикального расстояния."""
        distance = calculate_distance(0.0, 0.0, 0.0, 4.0)
        assert distance == 4.0

    def test_distance_diagonal(self):
        """Тест диагонального расстояния."""
        distance = calculate_distance(0.0, 0.0, 3.0, 4.0)
        assert distance == 5.0  # 3-4-5 треугольник

    def test_distance_negative_coordinates(self):
        """Тест расстояния с отрицательными координатами."""
        distance = calculate_distance(-1.0, -1.0, 2.0, 3.0)
        expected = math.sqrt((2 - (-1)) ** 2 + (3 - (-1)) ** 2)
        assert distance == expected

    def test_distance_floating_point(self):
        """Тест расстояния с плавающей точкой."""
        distance = calculate_distance(1.5, 2.5, 4.5, 6.5)
        expected = math.sqrt((4.5 - 1.5) ** 2 + (6.5 - 2.5) ** 2)
        assert abs(distance - expected) < 1e-10


class TestClamp:
    """Тесты ограничения значений."""

    def test_clamp_within_range(self):
        """Тест ограничения значения в пределах диапазона."""
        assert clamp(5.0, 0.0, 10.0) == 5.0
        assert clamp(0.0, 0.0, 10.0) == 0.0
        assert clamp(10.0, 0.0, 10.0) == 10.0

    def test_clamp_below_minimum(self):
        """Тест ограничения значения ниже минимума."""
        assert clamp(-5.0, 0.0, 10.0) == 0.0
        assert clamp(-10.0, -5.0, 5.0) == -5.0

    def test_clamp_above_maximum(self):
        """Тест ограничения значения выше максимума."""
        assert clamp(15.0, 0.0, 10.0) == 10.0
        assert clamp(20.0, -5.0, 5.0) == 5.0

    def test_clamp_negative_range(self):
        """Тест ограничения в отрицательном диапазоне."""
        assert clamp(-3.0, -10.0, -1.0) == -3.0
        assert clamp(-15.0, -10.0, -1.0) == -10.0
        assert clamp(5.0, -10.0, -1.0) == -1.0

    def test_clamp_zero_range(self):
        """Тест ограничения в нулевом диапазоне."""
        assert clamp(0.0, 0.0, 0.0) == 0.0
        assert clamp(5.0, 0.0, 0.0) == 0.0
        assert clamp(-5.0, 0.0, 0.0) == 0.0


class TestVectorNormalization:
    """Тесты нормализации векторов."""

    def test_normalize_unit_vector(self):
        """Тест нормализации единичного вектора."""
        x, y = normalize_vector(1.0, 0.0)
        assert abs(x - 1.0) < 1e-10
        assert abs(y - 0.0) < 1e-10

    def test_normalize_zero_vector(self):
        """Тест нормализации нулевого вектора."""
        x, y = normalize_vector(0.0, 0.0)
        assert x == 0.0
        assert y == 0.0

    def test_normalize_arbitrary_vector(self):
        """Тест нормализации произвольного вектора."""
        x, y = normalize_vector(3.0, 4.0)
        expected_length = math.sqrt(3.0**2 + 4.0**2)
        assert abs(x - 3.0 / expected_length) < 1e-10
        assert abs(y - 4.0 / expected_length) < 1e-10

    def test_normalize_negative_vector(self):
        """Тест нормализации отрицательного вектора."""
        x, y = normalize_vector(-3.0, -4.0)
        expected_length = math.sqrt(3.0**2 + 4.0**2)
        assert abs(x - (-3.0 / expected_length)) < 1e-10
        assert abs(y - (-4.0 / expected_length)) < 1e-10

    def test_normalize_floating_point_vector(self):
        """Тест нормализации вектора с плавающей точкой."""
        x, y = normalize_vector(1.5, 2.5)
        expected_length = math.sqrt(1.5**2 + 2.5**2)
        assert abs(x - 1.5 / expected_length) < 1e-10
        assert abs(y - 2.5 / expected_length) < 1e-10

    def test_normalized_vector_length(self):
        """Тест что нормализованный вектор имеет длину 1."""
        test_vectors = [
            (3.0, 4.0),
            (-5.0, 12.0),
            (1.0, 1.0),
            (0.1, 0.1),
            (100.0, 200.0),
        ]

        for vx, vy in test_vectors:
            nx, ny = normalize_vector(vx, vy)
            length = math.sqrt(nx**2 + ny**2)
            assert abs(length - 1.0) < 1e-10

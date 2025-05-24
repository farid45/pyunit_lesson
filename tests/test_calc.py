"""Тесты для калькулятора (Calculator)."""

import math
import unittest
from parameterized import parameterized
from app.main import Calculator
from math import inf


class TestCalculator(unittest.TestCase):
    """Группа тестов для проверки калькулятора."""

    def setUp(self):
        """Подготовка к тестам - создаем калькулятор."""
        self.calc = Calculator()  # Этот объект будет доступен во всех тестах

    # Тестируем обычное сложение
    @parameterized.expand([
        ("целые числа", 2, 3, 5),
        ("дробные числа", 2.5, 3.1, 5.6),
        ("отрицательные числа", -2.5, 3.0, 0.5)
    ])
    def test_sum(self, name, a, b, expected):
        """Проверяем, что сложение работает правильно.
        
        Аргументы:
            name: название теста (чтобы понять, какой провалился)
            a: первое число для сложения
            b: второе число для сложения
            expected: какой результат ожидаем
        """
        result = self.calc.sum(a, b)
        self.assertEqual(result, expected)

    # Тестируем сложение с неправильными данными
    @parameterized.expand([
        ("текст вместо чисел", 'a', 'b', TypeError),
        ("None вместо числа", None, 1, TypeError),
    ])
    def test_sum_invalid(self, name, a, b, expected_error):
        """Проверяем, что калькулятор ругается на неправильные данные.
        
        Аргументы:
            name: название теста
            a: неправильный первый аргумент
            b: неправильный второй аргумент
            expected_error: какая ошибка должна появиться
        """
        with self.assertRaises(expected_error):
            self.calc.sum(a, b)

    def test_divide_by_zero(self):
        """Проверяем, что нельзя делить на ноль."""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(1, 0)  # 1 / 0 должно вызвать ошибку


if __name__ == "__main__":
    unittest.main()  # Запускаем тесты при запуске файла
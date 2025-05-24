"""Тесты для функции log() калькулятора."""

import unittest
from parameterized import parameterized  # Для удобного тестирования разных случаев
import math  # Для использования математических констант
from app.main import Calculator  # Наш тестируемый калькулятор
from app.error import InvalidInputException  # Ошибка для недопустимых значений


class TestCalculatorLog(unittest.TestCase):
    """Тестируем функцию вычисления логарифма в калькуляторе."""
    
    def setUp(self):
        """Подготовка перед каждым тестом - создаем калькулятор."""
        self.calc = Calculator()  # Создаем новый калькулятор для каждого теста

    # Тестируем корректные входные данные
    @parameterized.expand([
        ("положительные целые числа", 8, 2, 3.0),  # log₂8 = 3
        ("дробное основание", 4, 0.5, -2.0),  # log₀.₅4 = -2
        ("одинаковые значения", math.e, math.e, 1.0),  # logₑe = 1
    ])
    def test_log_valid_input(self, name, a, base, expected):
        """Проверяем правильные расчеты логарифма.
        
        Аргументы:
            name: название теста (для понятных сообщений об ошибках)
            a: число для логарифма
            base: основание логарифма
            expected: ожидаемый результат
        """
        result = self.calc.log(a, base)
        self.assertAlmostEqual(result, expected)  # Почти равно для дробных чисел

    # Тестируем неправильные типы данных
    @parameterized.expand([
        ("строка вместо числа", "a", 1, TypeError),  # 'a' - не число
        ("None вместо числа", None, 1, TypeError),  # None недопустим
        ("список вместо числа", [2], 2, TypeError),  # Список не число
    ])
    def test_log_invalid_types(self, name, a, base, expected_error):
        """Проверяем обработку нечисловых аргументов.
        
        Аргументы:
            name: название теста
            a: некорректный аргумент
            base: основание логарифма
            expected_error: ожидаемая ошибка
        """
        with self.assertRaises(expected_error):
            self.calc.log(a, base)

    # Тестируем недопустимые значения
    @parameterized.expand([
        ("отрицательное число", -1, 2, InvalidInputException),  # log₂(-1) - ошибка
        ("основание 0", 10, 0, InvalidInputException),  # log₀10 - ошибка
        ("основание 1", 10, 1, InvalidInputException),  # log₁10 - ошибка
    ])
    def test_log_invalid_domain(self, name, a, base, expected_error):
        """Проверяем обработку значений вне области определения.
        
        Аргументы:
            name: название теста
            a: число для логарифма
            base: недопустимое основание
            expected_error: ожидаемая ошибка
        """
        with self.assertRaises(expected_error):
            self.calc.log(a, base)


if __name__ == "__main__":
    unittest.main()  # Запускаем тесты при выполнении файла
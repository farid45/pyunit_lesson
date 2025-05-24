"""
Модуль калькулятора с базовыми арифметическими операциями и логарифмом.

Калькулятор поддерживает:
- сложение чисел
- вычитание
- умножение
- деление
- вычисление логарифма
"""

from typing import Union, TypeVar  # Для аннотации типов
import math  # Для математических операций
from app.error import InvalidInputException  # Кастомное исключение

# Определяем тип для числовых значений (int или float)
Numeric = TypeVar('Numeric', int, float)

class Calculator:
    """Класс калькулятора с основными математическими операциями."""
    
    @staticmethod
    def sum(*args: Numeric) -> Numeric:
        """Складывает произвольное количество чисел.
        
        Аргументы:
            *args: числа для сложения (минимум два)
            
        Возвращает:
            Сумму всех чисел
            
        Выбрасывает:
            TypeError: если хотя бы один аргумент не число
        """
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise TypeError("Все аргументы должны быть числами")
        return sum(args)

    @staticmethod
    def subtract(a: Numeric, b: Numeric) -> Numeric:
        """Вычитает одно число из другого.
        
        Аргументы:
            a: уменьшаемое
            b: вычитаемое
            
        Возвращает:
            Разность a - b
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Аргументы должны быть числами")
        return a - b

    @staticmethod
    def multiply(a: Numeric, b: Numeric) -> Numeric:
        """Умножает два числа.
        
        Аргументы:
            a: первый множитель
            b: второй множитель
            
        Возвращает:
            Произведение a * b
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Аргументы должны быть числами")
        return a * b

    @staticmethod
    def divide(a: Numeric, b: Numeric) -> float:
        """Делит одно число на другое.
        
        Аргументы:
            a: делимое
            b: делитель
            
        Возвращает:
            Частное a / b
            
        Выбрасывает:
            ZeroDivisionError: при делении на ноль
        """
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Аргументы должны быть числами")
        if b == 0:
            raise ZeroDivisionError("Деление на ноль невозможно")
        return a / b

    def log(self, a: Numeric, base: Numeric) -> float:
        """Вычисляет логарифм числа по заданному основанию.
        
        Аргументы:
            a: число для логарифмирования (должно быть > 0)
            base: основание логарифма (должно быть > 0 и ≠ 1)
            
        Возвращает:
            Значение логарифма
            
        Выбрасывает:
            InvalidInputException: при недопустимых значениях a или base
            TypeError: если аргументы не числа
        """
        if not (isinstance(a, (int, float)) and isinstance(base, (int, float))):
            raise TypeError("Аргументы должны быть числами")
        
        if a <= 0 or base <= 0 or base == 1:
            raise InvalidInputException(self.log, a, base)
        return math.log(a, base)

# Пример использования калькулятора
if __name__ == "__main__":
    calc = Calculator()  # Создаем экземпляр калькулятора
    
    try:
        # Вычисляем логарифм 100 по основанию 10 (должно быть 2.0)
        print(calc.log(100, 10))
        
    except (TypeError, InvalidInputException) as e:
        # Обрабатываем возможные ошибки
        print(f"Ошибка: {e}")
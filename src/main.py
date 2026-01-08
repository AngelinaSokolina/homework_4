def add_numbers(a: int | float, b: int | float) -> float:
    """Сложение чисел"""
    return a + b


def is_even(a: int | float) -> bool:
    """Четное ли число?"""
    return a % 2 == 0


def find_max(my_list):
    """Найти максимальное значение"""
    if len(my_list) > 0:
        return max(my_list)
    return 0


def divide(a: int | float, b: int | float) -> float:
    """Деление чисел"""
    if b > 0:
        return a / b
    return 0

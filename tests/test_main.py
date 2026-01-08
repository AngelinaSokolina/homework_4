from src.main import divide
from src.main import add_numbers
from src.main import is_even
from src.main import find_max


def test_divide() -> None:
    """Тестирование функции divide"""
    assert divide(2, 1) == 2
    assert divide(2, 0) == 0


def test_add_numbers() -> None:
    """Тестирование функции add_numbers"""
    assert add_numbers(2, 2) == 4


def test_is_even() -> None:
    """Тестирование функции is_even"""
    assert is_even(2) == True
    assert is_even(3) == False, 'Это число нечетное'


def test_find_max() -> None:
    """Тестирование функции find_max"""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([]) == 0

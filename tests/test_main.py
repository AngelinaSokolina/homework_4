from src.main import divide, add_numbers, is_even, find_max, calculate_logarithm, check_age, reverse_string
import pytest


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


def test_calc_log():
    assert calculate_logarithm(8, 2) == 3.0
    assert calculate_logarithm(8, 4) == 1.5

    with pytest.raises(ValueError):
        calculate_logarithm(0, 2)

    with pytest.raises(ValueError):
        calculate_logarithm(4, 0)

# Если нужно проверить текст сообщения внутри ошибки — as exc_info обязателен.
def test_check_age() -> None:
    # Ловим ошибку в "контейнер" exc_info
    with pytest.raises(ValueError) as exc_info:
        check_age(-5)

    # Залезаем внутрь этого контейнера
    # Свойство .value — это и есть сам объект ошибки ValueError
    assert str(exc_info.value) == "Возраст не может быть отрицательным!"


@pytest.mark.parametrize('value, expected', [
    ('123', '321'),
    ('hello', 'olleh'),
    ('world', 'dlrow'),
])
def test_reverse_string(value, expected):
    assert reverse_string(value) == expected

# def test_reverse_string_numbers(numbers) -> None:
#     assert reverse_string('123') == numbers
#
#
# def test_reverse_string_letters(letters) -> None:
#     assert reverse_string('hello') == letters


# Сложение чисел
def add_numbers(a, b):
    return a + b


# Четное ли число?
def is_even(a):
    return a % 2 == 0

# Найти максимальное значение
def find_max(my_list):
    if len(my_list) > 0:
        return max(my_list)
    return 0


def divide(a, b):
    if b > 0:
        return a / b
    return 0

if __name__ == '__main__':
    assert add_numbers(2, 2) == 4

    assert is_even(2) == True
    assert is_even(3) == False, 'Это число нечетное'

    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([]) == 0

def linear_search(lst, target):
    """
    Линейный поиск элемента в списке.

    Args:
        lst: список для поиска
        target: элемент, который нужно найти

    Returns:
        индекс элемента, если найден, иначе -1
    """
    for index, value in enumerate(lst):
        if value == target:
            return index
    return -1
import random

# Создаём список из 100 случайных чисел от 1 до 1000
random_list = [random.randint(1, 1000) for _ in range(100)]
print("Список из 100 случайных чисел:")
print(random_list)

# Элементы для поиска: несколько есть в списке, несколько — нет
search_elements = [random_list[0], random_list[50], 9999, 8888]

print("\nРезультаты поиска:")
for element in search_elements:
    result = linear_search(random_list, element)
    if result != -1:
        print(f"Элемент {element} найден на позиции {result}")
    else:
        print(f"Элемент {element} не найден (возвращено {result})")

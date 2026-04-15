import random
import timeit
import matplotlib.pyplot as plt


def linear_search(arr, target):
    """
    Выполняет линейный поиск элемента target в списке arr.
    Возвращает индекс первого вхождения или -1, если элемент не найден.

    :param arr: Список, в котором выполняется поиск.
    :param target: Искомый элемент.
    :return: Индекс элемента или -1.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


# 01. Демонстрация работы функции на небольшом примере
demo_list = [10, 25, 30, 45, 50]
print("Демонстрация линейного поиска:")
print(f"Индекс числа 30: {linear_search(demo_list, 30)}")
print(f"Индекс числа 99: {linear_search(demo_list, 99)}\n")

# 02. Анализ временной и пространственной сложности (выводы в коде)
print("Анализ сложности:")
print("- Временная сложность: O(n) в худшем и среднем случае, O(1) в лучшем.")
print("- Пространственная сложность: O(1), так как используется константная дополнительная память.\n")

# 03. Поиск в списке из 100 случайных чисел
random.seed(42)  # Для воспроизводимости результатов
random_list = [random.randint(1, 100) for _ in range(100)]

# Выбираем значения для поиска: существующее в начале, в середине и отсутствующее
targets = [random_list[0], random_list[50], 200]
results = {t: linear_search(random_list, t) for t in targets}
print("Результаты поиска в списке из 100 случайных чисел:")
for t, idx in results.items():
    print(f"  Элемент {t}: индекс {idx}")
print()

# 04. Сравнение времени выполнения для разных размеров списков
sizes = [10, 100, 1000, 5000]
times = []

for size in sizes:
    # Генерируем новый список для каждого размера
    arr = [random.randint(1, 100) for _ in range(size)]

    # Измеряем время поиска отсутствующего элемента (худший случай)
    # number=10 — среднее по 10 запускам для большей точности
    elapsed = timeit.timeit(lambda: linear_search(arr, -1), number=10)

    # Сохраняем среднее время одного поиска
    times.append(elapsed / 10)

# Выводим результаты измерений
print("Время выполнения линейного поиска (в секундах):")
for size, t in zip(sizes, times):
    print(f"  Размер списка: {size:>5} — Среднее время: {t:.6f} сек")

# Строим график зависимости времени от размера списка
plt.figure(figsize=(8, 5))
plt.plot(sizes, times, marker='o', linestyle='-', color='b')
plt.title('Зависимость времени выполнения линейного поиска от размера списка')
plt.xlabel('Размер списка (n)')
plt.ylabel('Среднее время выполнения (сек)')
plt.grid(True)
plt.tight_layout()
plt.show()
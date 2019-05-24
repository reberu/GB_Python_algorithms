# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random


def bubble_sort(arr):
    last_elem = len(arr) - 1
    for x in range(0, last_elem):
        for i in range(0, last_elem):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


array = [random.randint(-100, 99) for i in range(10)]
print(f'Исходный массив:        {array}')
print(f'Отсортированный массив: {bubble_sort(array)}')

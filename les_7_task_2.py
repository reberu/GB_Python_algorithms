# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):
    middle = len(arr) // 2
    if len(arr) < 2:
        return arr
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)


def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result


array = [round(random.uniform(0, 49), 2) for i in range(10)]
print(f'Исходный массив:        {array}')
sorted_array = merge_sort(array)
print(f'Отсортированный массив: {sorted_array}')

# Задание №3
# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

array = [random.randint(0, 100) for _ in range(10)]
mn = mx = 0
for i in range(0, len(array)):
    if array[mx] < array[i]:
        mx = i
    if array[mn] > array[i]:
        mn = i
array[mn], array[mx] = array[mx], array[mn]

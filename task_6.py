# Задание №6
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [random.randint(0, 100) for _ in range(10)]
print(array)
mn = mx = total = 0
for i in range(0, len(array)):
    if array[mx] < array[i]:
        mx = i
    if array[mn] > array[i]:
        mn = i
if mn < mx:
    for i in range(mn + 1, mx):
        total += array[i]
else:
    for i in range(mx + 1, mn):
        total += array[i]
print(total)

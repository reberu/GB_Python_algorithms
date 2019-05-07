# Задание №5
# В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

import random

array = [random.randint(0, 10) - random.randint(0, 10) for _ in range(10)]
print(array)

mx = index = 0
for i in range(0, len(array)):
    if array[i] < 0 and (mx == 0 or array[i] > mx):
        mx = array[i]
        index = i
print(f'Максимальный отрицательный элемент массива: {mx}\nПозиция в массиве: {index + 1}')

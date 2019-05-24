# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.

import random

m = int(input('Задайте число m: '))
size = 2 * m + 1
array = [random.randint(0, 10) for i in range(size)]
print(array)
for i in range(len(array)):
    n = m = 0
    for j in range(0, len(array)):
        if array[j] != array[i]:
            if array[j] >= array[i]:
                n += 1
            else:
                m += 1
    if n == m:
        print(f'Медиана массива: {array[i]}')
        break

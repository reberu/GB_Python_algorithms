# Задание №4
# Определить, какое число в массиве встречается чаще всего.

import random

import random

array = [random.randint(0, 10) for _ in range(10)]
print(array)
count_max = 0
num = array[0]
for i in range(0, len(array)):
    count_min = 0
    for j in range(0, len(array)):
        if array[i] == array[j]:
            count_min += 1
    if count_max < count_min:
        count_max = count_min
        num = array[i]

if count_max > 1:
    print(f'{count_max} раз(а) встречается число {num}')
else:
    print('Все элементы уникальны')

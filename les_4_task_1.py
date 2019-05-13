# Практическое задание №6 урока №3
# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

# Из трех представленных вариантов решения задания, наиболее оптимальным является функция f_func,
# ввиду небольшого преимущества в скорости.
# Наименее оптимальным является функция f_sum, поскольку время на выполнение кода увеличивается существенно, 
# по сравнению с другими функциями. Особенно это проявляется при использовании массива с 1000 элементами и более.


def f_array(array):
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

# "les_4_task_1.f_array([random.randint(0, 100) for _ in range(10)])"
# 100 loops, best of 5: 121 usec per loop

# "les_4_task_1.f_array([random.randint(0, 100) for _ in range(20)])"
# 100 loops, best of 5: 141 usec per loop

# "les_4_task_1.f_array([random.randint(0, 100) for _ in range(40)])"
# 100 loops, best of 5: 436 usec per loop

# "les_4_task_1.f_array([random.randint(0, 100) for _ in range(80)])"
# 100 loops, best of 5: 534 usec per loop

# "les_4_task_1.f_array([random.randint(0, 100) for _ in range(160)])"
# 100 loops, best of 5: 752 usec per loop

# "les_4_task_1.f_array([random.randint(0, 100) for _ in range(500)])"
# 100 loops, best of 5: 2.25 msec per loop


def f_func(array):
    print(array)
    total = 0
    max_index = array.index(max(array))
    min_index = array.index(min(array))
    if max_index > min_index:
        for i in range(min_index + 1, max_index):
            total += array[i]
    elif max_index < min_index:
        for i in range(max_index + 1, min_index):
            total += array[i]
    print(total, ' ', max_index, ' ', min_index)


# "les_4_task_1.f_func([random.randint(0, 100) for _ in range(10)])"
# 100 loops, best of 5: 117 usec per loop

# "les_4_task_1.f_func([random.randint(0, 100) for _ in range(20)])"
# 100 loops, best of 5: 137 usec per loop

# "les_4_task_1.f_func([random.randint(0, 100) for _ in range(40)])"
# 100 loops, best of 5: 179 usec per loop

# "les_4_task_1.f_func([random.randint(0, 100) for _ in range(80)])"
# 100 loops, best of 5: 276 usec per loop

# "les_4_task_1.f_func([random.randint(0, 100) for _ in range(160)])"
# 100 loops, best of 5: 740 usec per loop

# "les_4_task_1.f_func([random.randint(0, 100) for _ in range(500)])"
# 100 loops, best of 5: 2.01 msec per loop


def f_sum(array):
    print(array)
    mn, mx = 0, 0
    for i in range(1, len(array)):
        if array[i] > array[mx]: mx = i
        if array[i] < array[mn]: mn = i
    print(mn, ' ', mx)
    if mn < mx:
        print(sum(array[mn + 1: mx]))
    else:
        print(sum(array[mx + 1: mn]))


# "les_4_task_1.f_sum([random.randint(0, 100) for _ in range(10)])"
# 100 loops, best of 5: 163 usec per loop

# "les_4_task_1.f_sum([random.randint(0, 100) for _ in range(20)])"
# 100 loops, best of 5: 184 usec per loop

# "les_4_task_1.f_sum([random.randint(0, 100) for _ in range(40)])"
# 100 loops, best of 5: 467 usec per loop

# "les_4_task_1.f_sum([random.randint(0, 100) for _ in range(80)])"
# 100 loops, best of 5: 637 usec per loop

# "les_4_task_1.f_sum([random.randint(0, 100) for _ in range(160)])"
# 100 loops, best of 5: 749 usec per loop

# "les_4_task_1.f_sum([random.randint(0, 100) for _ in range(500)])"
# 100 loops, best of 5: 2.35 msec per loop

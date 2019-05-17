count = int(input('Введите количество предприятий: '))
data = {}
for this in range(count):
    incomes = []
    name = input("Введите название предприятия: ")
    for i in range(4):
        incomes.append(int(input(f'Введите прибыль за {i + 1} квартал: ')))
    data[name] = incomes
org_total = {}
median = 0
for key in data:
    name = key
    year_gain = 0
    for this in data[key]:
        year_gain += this
    org_total[name] = year_gain
    median += year_gain
print(f'Средняя прибыль всех предприятий: {median / count}')
bankrupt = []
profit = []
for key in org_total:
    if org_total[key] > (median / count):
        profit.append(key)
    elif org_total[key] < (median / count):
        bankrupt.append(key)
print(f'Прибыль предприятий выше среднего:', end=' ')
for this in profit:
    print(this, end=' ')
print()
print(f'Прибыль предприятий ниже среднего:', end=' ')
for this in bankrupt:
    print(this, end=' ')

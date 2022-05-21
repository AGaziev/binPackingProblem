import math


def inNsystem(a, n):  # перевод в N-мерную систему счисления c дополнением до количества предметов
    global itemCount
    res = []
    while a > 0:
        res.append(a % n)
        a = a // n
    res.reverse()
    for i in range(itemCount - len(res)):
        res.insert(0, 0)  # дополняем массив нулями до количества предметов
    return res


itemCount = 6
items = [3, 3, 3, 3, 3, 3]
binSize = 4
sum = 0
for w in items:
    sum += w
print(sum)
maxBins = math.ceil(sum / binSize)  # оценка количества ящиков сверху
bestChoice = None
while bestChoice is None: # пока не найден лучший набор
    for i in range(maxBins ** itemCount):
        badSet = False  # проверка на валидность набора
        binStored = [0] * maxBins  # вес который хранит каждый ящик
        setOfPlaces = inNsystem(i, maxBins)  # набор
        for item, place in enumerate(setOfPlaces):
            binStored[place] += items[item]  # загружаем в ящик
            if binStored[place] > binSize:  # если перебор
                badSet = True
                break
        print(setOfPlaces, badSet)
        if not badSet:
            bestChoice = setOfPlaces
            break
    maxBins += 1 # если не найден набор для такого количества ящиков увеличиваем на единицу
print(bestChoice)

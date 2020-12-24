"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №64
Суммировать вводимые числа, среди которых нет нулевых. При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.
#версия Python: 3.6
"""
import re

list_numbers = []

sum = 0


while True:
    print("Введите число:", end=' ')
    string = re.sub(r'[^0-9\-]+', '', input())
    if len(string) == 0:
        print("В строке не обнаружено числа")
        continue

    number = int(string)
    list_numbers.append(number)

    if number == 99999:
        break
    elif number == 0:
        print("Сумма:", sum)
    else:
        sum += number

print("Сумма:", sum)

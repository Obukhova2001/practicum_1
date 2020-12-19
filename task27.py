"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №27
import math
Дано вещественное число A. Вычислить f(A), если f(x) = 0 при x ≤ 0; f(x) = x2 − x при 0 < x < 1, в противном случае f(x) = x2 − sin(πx2).
#версия Python: 3.8.5
"""
import math
A = float(input("Введите число А:"))
x = A
if x <= 0:
    fx = 0
    print("x <= 0; f(a) =:", fx)
elif 0 < x < 1:
    fx = math.pow(x, 2) - x
    print("0 < x < 1; f(a) =:", fx)
else:
    fx = math.pow(x, 2) - math.sin((math.pi * math.pow(x, 2)))
    print("x >= 1; f(a) =:", fx)

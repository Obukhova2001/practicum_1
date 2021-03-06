"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №25
Дано вещественное число A. Вычислить f(A), если f(x) = x2 + 4x + 5, при x ≤ 2; в противном случае f(x) = 1/(x2 + 4x + 5).
#версия Python: 3.8.5
"""
a = float(input("Введите число А:"))
x = a
if x <= 2:
    fx = x**2 + 4*x + 5
    print("x <= 2; f(a) =:", fx)
else:
    fx = 1 / (x**2 + 4*x + 5)
    print("x > 2; f(a) =:", fx)

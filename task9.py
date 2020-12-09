"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 9
Дано натуральное число. Определить, будет ли это число: нечётным, кратным 7.
#версия Python: 3.8.5
"""
a = int(input("Введите число для проверки:"))
if a % 2 == 1 and a % 7 == 0:
    print("Число", a, "нечетно и кратно 7")
else:
    print("Число не соответствует условиям")

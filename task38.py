"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №38
Дан одномерный массив числовых значений, насчитывающий N элементов.Исключить из него M элементов, начиная с позиции K.
#версия Python: 3.8.5
"""
import numpy as np
import array
import random

N = int(input("Введите количество элементов массива "))
K = int(input("Позиция K "))
M = int(input("количество элементов для вычитания "))
A = [random.randint(0, 100) for i in range(0, N)]
print(A)

A.insert(K,M)
print(A)

A.delete(K,M)

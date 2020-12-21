"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №36
Дан одномерный массив числовых значений, насчитывающий N элементов. Вставить группу из M новых элементов, начиная с позиции K.
#версия Python: 3.8.5
"""
import array
import random

N = int(input("Введите количество элементов массива "))
M = int(input("Количесвто элементов в группе"))
K = int(input("Позиция K"))
A = [random.randint(0, 100) for i in range(0, N)]
B = [random.randint(0, 100) for b in range(0, M)]

print(A)
print(B)

A.insert(K, B)
print(A)

"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума № 78
Создать прямоугольную матрицу A, имеющую N строк и M столбцов со случайными элементами. Разделить элементы каждой строки на элемент этой строки с наибольшим значением.
#версия Python: 3.8.5
"""
import random

N = 4
M = 5

L = 2


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(0, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

i = 0
while i < len(A):
    j = 0
    max_element = max(A[i])
    while j < len(A[i]):
        A[i][j] /= max_element
        A[i][j] = round(A[i][j], 1)
        j += 1

    i += 1

print("Модифицированная матрица:")
print_matrix(A)

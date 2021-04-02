"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №52
Заданы M строк символов, которые вводятся с клавиатуры. Из заданных строк, каждая из которых представляет одно слово, составить одну длинную строку, разделяя слова пробелами.
#версия Python: 3.6
"""
import random
M = random.randint(1,10)
arr = [random.randint(1,10) for i in range(M)]

for i in range(M):
    arr[i] = input()
print(arr)
b = arr[0]

for i in range(1 , M):
    b = str(b) + " " + arr[i]
print(b)

"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №59
Заданы M строк, которые вводятся с клавиатуры. Подсчитать количество пробелов в каждой из строк.
#версия Python: 3.6
"""
import re
M = 3

list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for string in list_strings:
    count_spaces = len(re.findall(r'\s', string))
    print("В строке \"%s\" %s пробелов" % (string, count_spaces))

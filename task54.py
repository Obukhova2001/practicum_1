"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №54
Заданы M строк слов, которые вводятся с клавиатуры (в каждой строке – одно слово). Вводится слог (последовательность букв). Подсчитать количество таких слогов в каждой строке.
#версия Python: 3.6
"""
import re
M = 2
list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

print("Введите слог:", end=' ')
syllable = input()

for string in list_strings:
    count = len(re.findall(syllable, string))
    print("В строке \"%s\" слог \"%s\" встречается %s раз"
          % (string, syllable, count))

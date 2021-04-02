"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №53
Заданы M строк слов, которые вводятся с клавиатуры. Подсчитать количество гласных букв в каждой из заданных строк.
#версия Python: 3.6
"""
import re
M = 4
def get_count(str):
    vowel = 0
    consonant = 0
    str = re.sub(r'\d', '', str)
    str = re.sub(r'\W', '', str)
    i = 0
    while i < len(str):
        char = str[i]
        if char.lower() in ['a', 'e', 'i', 'o', 'u', 'y',
                            'а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']:
            vowel += 1
        else:
            consonant += 1

        i += 1
    return vowel, consonant
list_strings = []
for i in range(0, M):
    print("Введите строку:", end=' ')
    list_strings.append(input())

for str in list_strings:
    vowel, consonant = get_count(str)
    print("В строке %s %s гласных и %s согласных" % (str, vowel, consonant))

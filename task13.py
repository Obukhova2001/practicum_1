"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №13
Можно ли из бревна, имеющего диаметр поперечного сечения D, выпилить квадратный брус шириной А?
#версия Python: 3.8.5
"""
import math
D = int(input("Введите диаметр поперечного сечения:"))
A = int(input("Введите ширину квадратного бруса:"))
A = math.sqrt(2) * A
print("Диагональ бруса равна",A)
if (A <=D):
    print("Выпилить квадратный брус шириной ",A,"возможно")
else:
    print("Выпилить квадратный брус шириной ", A, "невозможно")

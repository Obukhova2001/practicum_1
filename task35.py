"""
Имя проекта: Boring-numpy
Номер версии: 1.0
Имя файла: practicum-1(1-101).py
Автор: 2019 © Д.А.Обухова, Челябинск
Лицензия использования:  CC BY-NC 4.0 (https://creativecommons.org/licenses/by-nc/4.0/deed.ru)
Дата создания: 11/11/2020
Дата последней модификации: 11/11/2020
Связанные файлы/пакеты: numpy, random
Описание: Решение задач № 1-101 практикума №35
Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами группу из M элементов, начинающихся с позиции K с группой из M элементов, начинающихся с позиции P.
#версия Python: 3.8.5
"""
N = int(input("Введите количество элементов массива "))
A = int(input("Количесвто элементов в группе"))
C = int(input("Позиция C"))
B = int(input("Позиция B"))
a = [random.randint(0, 100) for i in range(0, N)]

print(a)
for i in range(N):
    a[C: C + A], a[B: B + A] = a[C: C + A], a[B: B + A]
    
print(a)

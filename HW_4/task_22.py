# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. 
# n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов в 1 списке: '))
m = int(input('Введите количество элементов во 2 списке: '))
A = list()
B = list()
for i in range(n):
    A.append(int(input('Введите элемент 1-го списка №' + str(i + 1) + ': ')))
print('---------')
for i in range(m):
    B.append(int(input('Введите элемент 2-го списка №' + str(i + 1) + ': ')))
print('Список 1:', *A)
print('Список 2:', *B)
res = []
for i in A:
    for j in B:
        if i == j and i not in res:
            res.append(i)
print('Результат:', *sorted(res))

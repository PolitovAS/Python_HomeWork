# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# lst = list(map(int, input('Введите список из чисел: ').split()))
lst = list(int(x) for x in input('Введите список из чисел: ').split()) # Эквивалент предыдущей строке

min_val = int(input('Введите минимальное значение: '))
max_val = int(input('Введите максимальное значение: '))
res = list()

for i, el in enumerate(lst):
    if min_val <= el <= max_val:
        res.append(i)
print(*lst)
print(*res)


   
# list_1 = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# min_number = int(input())
# max_number = int(input())
# for i in range(len(list_1)):
#     if min_number <= list_1[i] <= max_number:
#         print(i)
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Сумма чисел: '))
p = int(input('Произведение чисел: '))

# Первый вариант
for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'x = {x}, y = {y}')
            

# Второй вариант
# from math import sqrt

# D = s * s - 4 * p

# if D < 0:
#     print('Решений нет')
    
# x = int((s + sqrt(D)) / 2)
# y = int((s - sqrt(D)) / 2)

# print(f'x = {x}, y = {y}')
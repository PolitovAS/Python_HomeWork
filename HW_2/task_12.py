# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000),
# а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

s = int(input('Сумма чисел: '))
p = int(input('Произведение чисел: '))


for x in range(s):
    for y in range(p):
        if s == x + y and p == x * y:
            print(f'x = {x}, y = {y}')
            break
    else:
        continue
    break 
else:
    print('Подсказки не правильные! или Числа не натуральные!')   

# второй вариант
# s = int(input('введите сумму двух чисел: '))
# p = int(input('введите произведение двух чисел: '))

# for x in range(1, 1000):
#     if s - x == p // x and p % x == 0:
#         print(x, p // x)
#         break
# else:
#     print('решения нет')
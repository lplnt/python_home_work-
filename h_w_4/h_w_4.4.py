# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k(до 6 степени).*
# *Пример:* - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите натуральную степень: '))
coef = []
result = ''
for i in range(k + 1):
    coef.append('{:+}'.format(random.randint(-100, +100)))
x, y, z = 1, 1, 0
while k != -1:
    if k <= 1:
        x = 0
    if k == 0:
        y = 0
    result += coef[z] + y * ('x' + x * ('^' + str(k)) + ' ')
    k -= 1
    z += 1
result += '  = 0'

with open('Python/Python home work/h_w_4/h_w_4.4.txt', 'a') as f:
    if result[0] == '+':
        f.write(result[1:])
        f.write('\n')
    # if coef == 0:
        # тут что-то еще надо добавить
    else:
        f.write(result)
        f.write('\n')
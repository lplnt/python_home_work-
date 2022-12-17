# Вычислить число ПИ c заданной точностью d
# *Пример:* - при d = 0.0001, π = 3.1415.    10^-1 ≤ d ≤ 10^-10

import math

pi = math.pi
num = int(input("Введите сколько знаков нужно вывести после запятой: "))
result = round(pi, num)
print(result)
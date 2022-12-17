# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N. 

num = int(input("Введите натуральное число: "))
fact = []
d = 2
memb = num
while d ^ 2 <= num:
    if num % d == 0:
        fact.append(d)
        num //= d
    else:
        d += 1
fact.append(num)
print('{} = {}' .format(memb, fact))

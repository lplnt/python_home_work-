# MAP
# Программа создает список и возводит все его значения в квадрат

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(0, 10))
print(f'Cлучайный список: {numbers}')

squared = map(lambda num: num ** 2, numbers)
print(list(squared))
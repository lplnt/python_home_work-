# ENUMERATE
# Программа выводит элемент списка и его индекс

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(0, 10))
print(f'Cлучайный список: {numbers}')

for i in enumerate(numbers):
    print(i)
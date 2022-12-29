# FILTER
# Программа создает случайный список и выводит нечетные числа из списка

from random import randint
numbers = []
for i in range(10):
    numbers.append(randint(-10, 10))
print(f'Cлучайный список: {numbers}')

new_list = list(filter(lambda x: (x%2 != 0) , numbers))
print(f'Нечетные числа в списке: {new_list}')
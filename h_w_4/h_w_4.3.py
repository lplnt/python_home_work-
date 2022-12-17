# Задайте последовательность чисел. Напишите программу, которая 
# выведет список неповторяющихся элементов исходной последовательности.

from random import randint

numbers = []
for i in range(10):
    numbers.append(randint(-10, 10))
print(f'Cлучайный список: {numbers}')

new_numbers = []
for i in range(len(numbers)):
    if numbers.count(numbers[i]) == 1:
        new_numbers.append(numbers[i])
print(f'Cписок без повторений: {new_numbers}')
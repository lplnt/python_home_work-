# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: - [2, 3, 4, 5, 6] => [12, 15, 16];
#         - [2, 3, 5, 6] => [12, 15]

lst = list(map(int, input("Введите числа через пробел: ").split()))
new_lst = []

for i in range(len(lst)//2):
    new_lst.append(lst[i] * lst[-i-1])
if len(lst) % 2 != 0:
    mid = len(lst) // 2
    new_lst.append(lst[mid] ** 2)

print(new_lst)
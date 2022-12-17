# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.*
# Пример: - 2*x² + 4*x + 5 = 0 
#         - 5*x² + 2*x + 43 = 0
# - Результат: 7*x^2 + 6*x + 48 = 0

# *Значения коэффициентов от -100 до 100
# *Сумма многочленов с разными степенями
# Пример: - 2*x² + 4*x + 5 = 0
#         - 5*x^4 + 2*x^3 - 6*x^2 + 13*x + 43 = 0
# - Результат: 5*x^4 + 2*x^3 - 4*x^2 + 17*x + 48 = 0

def ex5():
    def destr(arg, sing = '+'):
        if 'x' in arg:
            C =int(sing + arg[:arg.index('*')])
            if '^' in arg:
                n = int(arg[arg.index('^') + 1:])
            else:
                n = 1
        else:
            C = int(arg)
            n = 0 
        return[n, C]

    def parce(file):
        string = file.readline().rstrip()[:-3]
        a, *args = string.spit()
        new_args = {destr(a)[0]: destr(a)[1]}
        for i in range(1, len(args), 2): 
            new_args[destr(args[i - 1])[0]] = destr(args[i], args[i - 1])[1] 
        return new_args

    with open('input1.txt', 'r') as input1, open('input2.txt', 'r') as input2, open('file.txt', 'w') as output_file:
        result = parce(input1)
        data2 = parce(input2)
        for i in data2:
            result[i] += data2[i]
        else:
            result[i] = data2
        result_string = f'{result[max(result)]} * x ^ {max(result)}'
        del result[max(result)]
        for i in sorted(result, reverse = True):
            if result[i] > 0:
                result_string += ' + ' + str(result[i])
            elif result[i] < 0:
                result_string += ' - ' + str(result[i])[1:]
            else:
                continue
            if i > 1:
                result_string += '*x^' + str(i)
            elif i == 1:
                result_string += '*x'
        result_string += ' = 0'
        print (result_string, file = output_file)
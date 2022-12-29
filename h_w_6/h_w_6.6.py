# Напишите программу вычисления арифметического выражения заданного строкой. 
# Используйте операции +,-,/,*. приоритет операций стандартный.
# *Пример:*
# 2+2 => 4;
# 1+2*3 => 7;
# 1-2*3 => -5;

ln_in = input('Введите выражение: ').split()

print(ln_in)

def aka_eval(args):
    
    while len(args) != 1:
        while '*' in args or '/' in args:
            try:
                prod_index = args.index('*')
            except:
                prod_index = 100

            try:
                div_index = args.index('/')
            except:
                div_index = 100

            if prod_index < div_index:
                args[prod_index - 1] = int(args[prod_index - 1]) * int(args[prod_index + 1])
                args.pop(prod_index +1)
                args.pop(prod_index)
            else:
                args[prod_index - 1] = int(args[prod_index - 1]) / int(args[prod_index + 1])
                args.pop(prod_index +1)
                args.pop(prod_index)


        while '+' in args or '-' in args:
            try:
                sum_index = args.index('+')
            except:
                sum_index = 100

            try:
                deg_index = args.index('-')
            except:
                deg_index = 100

            if sum_index < deg_index:
                args[sum_index - 1] = int(args[sum_index - 1]) + int(args[sum_index + 1])
                args.pop(sum_index + 1)
                args.pop(sum_index)
            else:
                args[deg_index - 1] = int(args[deg_index - 1]) - int(args[deg_index + 1])
                args.pop(deg_index + 1)
                args.pop(deg_index)

    print(args[0])

aka_eval(ln_in)
# def view_data(data, title):
#     print(f'{title} = {data}')

# def get_value():
#     return int(input('value = '))

def get_value():
    print("Добро пожаловать в калькулятор.")
    kind_operation = input("Для работы с комплексными числами введите 1, для работы с работы с обычными числами введите 2: ")
    
    while True:
        inp = input("Введите числа и знак операции через пробелы: ")
        try_act = inp
        data = try_act.split()

        if len(data) == 3:
            if data[1] == "+" or data[1] == "-" or data[1] == "*" or data[1] == "/":
                print("Спасибо!")
                break

        print("Неверно, введите еще раз!")

    return inp, kind_operation


def output(result):
    try:
        if result.is_integer():
            print(f"Результат: ", int(result))
        elif isinstance(result, float):
            print(f"Результат: ", result)
        else: print(result)
    except:
        print(result)
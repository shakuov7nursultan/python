def is_digit(string):
     if string.isdigit():
        return True
     else:
         try:
             float(string)
             return True
         except ValueError:
             return False

def ask_calc_type(message):
     print(message)
     value = input()
     while not (value == '1' or value == '2'):
         print('Неправильный ввод \n' + message)
         value = input()
     return value

calc_type = ask_calc_type("Выберите тип вычисления: если рациональные введите 1, если комплексные введите 2")

def ask_number(message):
     print(message)
     value = ''
     while not (is_digit(value)):
         value = input()
     return float(value)


left_value = ask_number('Введите первое число (для комплексного чисила используйте формат: "5 + 3j"):')
right_value = ask_number('Введите второе число (для комплексного чисила используйте формат: "5 + 3j"):')
op = ask_opertaion('Выберите операцию:')


# 1) Введите число 1
# 2) Введите число 2
# 3) Какую операцию производим


def view_data(data, title):
    print(f'{title} = {data}')


def get_value():
    return input()


def input_data():
    print('С какими числами будем работать? Введите 1 для работы с комплексными числами, 2 - для работы с рациональными числами')
    data_type = get_value()
    if data_type == '1':
        print('Введите первое число (используйте формат: "5 + 3j"):')
        left_value = get_value()
        print('Введите второе число (используйте формат: "5 + 3j"):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
    elif data_type == '2':
        print('Введите первое число (используйте формат: "5/11"):')
        left_value = get_value()
        print('Введите второе число (используйте формат: "5/11"):')
        right_value = get_value()
        print('Выберите операцию:')
        oper = get_value()
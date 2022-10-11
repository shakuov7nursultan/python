import Func_list_generation as lg
numbers_list = lg.list_generation()
sum_odd = sum(numbers_list[item] for item in range(1, len(numbers_list), 2))
odd_el = str([numbers_list[item] for item in range(1, len(numbers_list), 2)]).strip('[]')
print(f'Для списка {numbers_list} сумма чисел, стоящих на нечётных позициях: \n{odd_el} равна {sum_odd}.')
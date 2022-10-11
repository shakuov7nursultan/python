def reduction_correct_form_expression(func: str) -> str:
    expression = func.replace('^', '**')
    expression = expression.replace(' ', '')
    expression = expression.replace('+-', '-')
    expression = expression.replace('-+', '-')
    expression = expression.replace(',', '.')

    return expression

def identification_numbers_right(simbol: str, expression: str):
    index = expression.find(simbol)
    right_num = ''
    t = 0
    if simbol == '**':
        a = index + 2
    else:
        a = index +1 
    sing = (expression[a])
    if sing == '-':
        right_num = right_num + (expression[i])
        a += 1
    elif sing == '+':
        a += 1
    for i in range(a, len(expression)):
        bb = (expression[i])
        if bb.isdigit() or bb == '.':
            right_num = right_num + bb
            if bb == '.':
                t += 1 
        else:
            break
    if t > 0:
        right_num = float(right_num)
    else:
        right_num = int(right_num)
    return right_num

def identification_numbers_left(simbol: str, expression: str):
    index = expression.find(simbol)
    left_num = ''
    t = 0
    for i in range(index-1, -1, -1):
        bb = (expression[i])
        if bb.isdigit() or bb == '.':
            left_num = bb + left_num
            if bb == '.':
                t += 1 
        else:
            break
    if t > 0:
        left_num = float(left_num)
    else:
        left_num = int(left_num)
    return left_num

def arithmetic_action(simbol: str, left_num, right_num):
    if simbol == '**':
        return left_num**right_num
    elif simbol == '*':
        return left_num*right_num
    elif simbol == '/':
        return left_num/right_num
    elif simbol == '+': 
        return left_num+right_num
    elif simbol == '-':
        return left_num-right_num

def expression_abbreviation(simbol: str, expression: str):
    index = expression.find(simbol)
    left_num = identification_numbers_left(simbol, expression)
    right_num = identification_numbers_right(simbol, expression)
    res = arithmetic_action(simbol, left_num, right_num)
    li = index - len(str(left_num))
    ri = li + len(str(left_num)+simbol+str(right_num))
    return expression[:li] + str(res) + expression[ri:]

def priority_of_operations(simbol_1: str, simbol_2: str, expression: str) -> str:
    if simbol_1 in expression and simbol_2 in expression:
        if expression.find(simbol_1) > expression.find(simbol_2):
            return simbol_2
        elif expression.find(simbol_1) < expression.find(simbol_2):
            return simbol_1
    elif simbol_1 in expression:
        return simbol_1
    elif simbol_2 in expression:
        return simbol_2

def performing_operations(expression: str):
    while '**' in expression:
        simbol = '**'
        expression = expression_abbreviation(simbol, expression)
    while '*' in expression or '/' in expression:
        simbol = priority_of_operations('*', '/', expression)
        expression = expression_abbreviation(simbol, expression)
    while '+' in expression or '-' in expression:
        if expression.find('-') == 0:
            break
        else:
            simbol = priority_of_operations('+', '-', expression)
            expression = expression_abbreviation(simbol, expression)
    result = float(expression)
    if result % 1 == 0:
        result = int(result)
    return result

func = '(12/3+(2+3)**3-7)*2-16 / (4 +4)+(11-7*(8-(8/4)**2 +6)/5)'
print(f'{eval(func) = }')
expression = reduction_correct_form_expression(func)
if expression.count('(') != expression.count(')'):
    print(f'Заданное выражение {func} некорректно! Оно содержит непарные скобки!!!')
else:
    while expression.count('(') != 0 or expression.count(')') !=0:
        right_index = expression.find(')')
        item = expression.find('(')
        while expression.find('(', item) != -1:
            if expression.find('(', item+1) > right_index or expression.find('(', item+1) == -1:
                left_index = expression.find('(', item)
                break
            else:
                item = expression.find('(', item+1)
        expr = expression[left_index+1 : right_index]
        res = performing_operations(expr)
        expression = expression[:left_index] + str(res) + expression[right_index+1:]
        expression = expression.replace('+-', '-')
result = performing_operations(expression)
print(f'{result = }')
f = '3*x+1'
n = int(input('Количество элементов словаря: '))
d = {x: eval(f) for x in range(1, n+1)}
print(f'для {n = }: {d}')
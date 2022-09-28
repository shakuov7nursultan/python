n = int(input('input N: '))
factorial = 1
for i in range(1, n+1):
    factorial *= i
print(factorial, end=' ')
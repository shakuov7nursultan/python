n = int(input('input quarter number: '))
if n < 1 or n > 4:
     print('Please, repeat the input')
elif n == 1:
     print('x > 0 and y > 0')
elif n == 2:
     print('x < 0 and y > 0')
elif n == 3:
     print('x < 0 and y < 0')
elif n == 4:
     print('x > 0 and y < 0')
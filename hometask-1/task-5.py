print('Enter coordinates point А:')
x_A = float(input('X: '))
y_A = float(input('Y: '))
print("Enter coordinates point B:")
x_B = float(input('X: '))
y_B = float(input('Y: '))

from math import sqrt
print('Distance between A and B: ',round(sqrt((x_A - x_B)**2 + (y_A - y_B)**2), 2)) # Теорема Пифагора 
day = int(input('Enter day number: '))
if day > 7 or day < 1:
    print('Please, repeat the input')
elif day == 6 or day == 7:
    print("Yes, it's weekend!") 
else:
    print("No, it's not weekend!")
number_1 = int(input('Enter your first number: '))
number_2 = int(input('Enter your second number: '))

operation = input(''' 
Please enter one of the following options: 
+ for Addition, 
- for Subtraction,
* for Multiplication,
/ for division ''')

if operation == '+':

    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Please restart and enter symbol from the list.')


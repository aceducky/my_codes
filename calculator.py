import sys
import os
import time


def calculator():
    try:
        os.system('cmd /c "color a" ')
        print('''
                            /---+++***Calculator***+++---/


             .----------------.   .----------------.   .----------------.   .----------------.   .----------------. 
            | .--------------. | | .--------------. | | .--------------. | | .--------------. | | .--------------. |
            | |      _       | | | |              | | | |      _       | | | |        __    | | | |     ___      | |
            | |     | |      | | | |              | | | |   /\| |/\    | | | |       / /    | | | |    / _ \     | |
            | |  ___| |___   | | | |    ______    | | | |   \     /    | | | |      / /     | | | |   |_/ \_|    | |
            | | |___   ___|  | | | |   |______|   | | | |  |_     _|   | | | |     / /      | | | |              | |
            | |     | |      | | | |              | | | |   /     \    | | | |    / /       | | | |              | |
            | |     |_|      | | | |              | | | |   \/|_|\/    | | | |   /_/        | | | |              | |
            | |              | | | |              | | | |              | | | |              | | | |              | |
            | '--------------' | | '--------------' | | '--------------' | | '--------------' | | '--------------' |
             '----------------'   '----------------'   '----------------'   '----------------'   '----------------' 

                    ''')
        while True:
            a = input("Enter first number: ")
            try:
                a = float(a)
            except:
                print('Quitting....',)
                time.sleep(0.5)
                print('....')
                time.sleep(0.5)
                print('Complete')
                quit()
            b = float(input('Enter second number: '))
            choice = int(input('''Enter a choice:
                        1. add
                        2. subtract
                        3. multiply
                        4. divide
                        5. power\n '''))
            operators = {1: 'add', 2: 'subtract',
                         3: 'multiply', 4: 'divide', 5: 'power'}
            if choice not in operators.keys():
                print("Error")
                sys.exit(1)
            print('\n')
            if choice == 1:
                print(f'Result: {a} + {b} = {a + b} \n')
            if choice == 2:
                print(f'Result: {a} - {b} = {a - b} \n')

            if choice == 3:
                print(f'Result: {a} * {b} = {a * b} \n')
            if choice == 4:
                try:
                    print(f'Result: {a} / {b} = {a / b} \n')
                except ZeroDivisionError:
                    print("Infinity ")
            if choice == 5:
                print(f'Result: {a} ^ {b} = {pow(a, b)}')
            print('Enter any alphabet to exit \n')
    except Exception as e:
        print(f'Error Occured: {e}')


calculator()

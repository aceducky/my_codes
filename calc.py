import sys
import os
import time

class Calculator:
    try:
        def __init__(self, a, b):
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
            os.system('cmd /c "color a" ')
            while True:
                a = input("Enter first number: ")
                try:
                    a = float(a)
                except:
                    print('Quitting',end= ' ')
                    time.sleep(0.5)
                    print('....')
                    time.sleep(0.5)
                    print('....')
                    time.sleep(0.5)
                    print('Complete')
                    quit()
                b = float(input('Enter second number: '))
                self.a = a
                self.b = b
                choice = int(input('''Enter a choice:
                    1. add
                    2. subtract
                    3. multiply
                    4. divide
                    5. power\n '''))
                operators = {1: 'add', 2: 'subtract', 3: 'multiply', 4: 'divide', 5: 'power'}
                if choice not in operators.keys():
                    print("Error")
                    sys.exit(1)
                print(operators.get(choice))
                if choice == 1:
                    print(f'{self.a} + {self.b} = {self.a + self.b}')
                if choice == 2:
                    print(f'{self.a} - {self.b} = {self.a - self.b}')

                if choice == 3:
                    print(f'{self.a} * {self.b} = {self.a * self.b}')
                if choice == 4:
                    try:
                        print(f'{self.a} / {self.b} = {self.a / self.b}')
                    except ZeroDivisionError:
                        print("Can\'t divide by zero")
                if choice == 5:
                    print(f'{self.a} ^ {self.b} = {pow(self.a, self.b)}')
                print('Press any alphabet to exit')
    except Exception as e:
        print(f'Error Occured: {e}')
        
calci = Calculator(1,2)

import sys
import os
import time
import platform



def calculator():
    try:
        if sys.platform == "win32" or platform.system() == "Windows": os.system('cmd /c "color a" ')
        print(r'''
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
            if a.strip() == '':
                print('Quitting....',)
                time.sleep(0.5)
                print('....')
                time.sleep(0.5)
                print('Complete')
                sys.exit(0)
            a = float(a)
            choice = input(
                'Choose one:\n (a) +  (b) -  (c) *  (d) /  (e) ^ : ').lower()
            if choice == 'a':
                print('\033[1A' + '+' + '\033[K')
            elif choice == 'b':
                print('\033[1A' + '-' + '\033[K')
            elif choice == 'c':
                print('\033[1A' + '*' + '\033[K')
            elif choice == 'd':
                print('\033[1A' + '/' + '\033[K')
            elif choice == 'e':
                print('\033[1A' + '^' + '\033[K')
            else:
                pass
            operators = ['a', 'b', 'c', 'd', 'e']
            if choice not in operators:
                print("Error")
                sys.exit(1)
            b = float(input('Enter second number: '))
            print('\n')
            if choice == 'a':
                print(f'Result: {a} + {b} = {a + b} \n')
            if choice == 'b':
                print(f'Result: {a} - {b} = {a - b} \n')
            if choice == 'c':
                print(f'Result: {a} * {b} = {a * b} \n')
            if choice == 'd':
                try:
                    print(f'Result: {a} / {b} = {a / b} \n')
                except ZeroDivisionError:
                    print("Infinity ")
            if choice == 'e':
                print(f'Result: {a} ^ {b} = {pow(a, b)}')
            print("\n(Press Enter to exit)\n")
        
    except Exception as e:
        print(f'Error Occured: {e}')

calculator()

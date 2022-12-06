from colorama import Fore, init
init()

def calc():
    print(Fore.GREEN + '********************************************')
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    action = str(input('Choose an action: '))
    if action != '/' and action != '*' and action != '+' and action != '-':
        while action != '/' and action != '*' and action != '+' and action != '-':
            action = str(input('Choose an action: '))

    print(Fore.GREEN + '********************************************')
    if action == '/':
        print(f'Result: {num1 / num2}')
        print(Fore.GREEN + '********************************************')
    elif action == '*':
        print(f'Result: {num1 * num2}')
        print(Fore.GREEN + '********************************************')
    elif action == '+':
        print(f'Result: {num1 + num2}')
        print(Fore.GREEN + '********************************************')
    elif action == '-':
        print(f'Result: {num1 - num2}')
        print(Fore.GREEN + '********************************************')
    elif action == 'sqr':
        print(f'Result: {num1 ** num2}')
        print(Fore.GREEN + '********************************************')
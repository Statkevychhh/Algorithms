from sympy.logic import SOPform, POSform
from sympy import symbols



def insertion():
    func = []

    numbers = input(f'Введіть власну функцію (наприклад: 1 2 3 4 5 6 7 8): ')
    func = [int(num) for num in  numbers.split(' ')]
    print(f'V = {*func,}')
    return func


def minimize(func):
    x1, x2, x3, x4 = symbols('x1 x2 x3 x4')
    CDNF = SOPform([x1, x2, x3, x4], func)
    print('СДНФ: F =', CDNF)
    # CKNF = POSform([x1, x2, x3, x4], minterms)
    # print('СКНФ: F =', CKNF)



if __name__ == '__main__':
    func = [1, 2, 3, 5, 10, 14, 15]
    
    while True:
        n = input('''Мінімізувати логічну функцію, задану в умові завдання - введіть 1,\nВвести логічну функцію власноруч - введіть - 2\n''')
        if not n in ['1','2']:
            print('Ви ввели не валідні дані, введіть ще раз!')
            continue;
        break;
    
    if int(n) == 2:
        func = insertion()    
    print(f'V = {*func,}')
    
    minimize(func)

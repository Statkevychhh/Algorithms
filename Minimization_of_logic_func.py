def insertion():
    func = []
    count = int(input('Введіть кілікість чисел для логічної функції: '))
    for x in range(0, int(count)):
        num = int(input(f'Введіть число {x+1}: '))
        func.append(num)
    print(f'V = {*func,}')
    return func


def minimize(logic_func):
    ...



if __name__ == '__main__':
    func = [1, 2, 3, 5, 10, 14, 15]
    
    while True:
        n = input('''Мінімізувати логічну функцію, задану в умові завдання - введіть 1,
Ввести логічну функцію власноруч - введіть - 2\n''')
        if (not n.isnumeric()) or (not n in ['1','2']):
            print('Ви ввели не валідні дані, введіть ще раз!')
            continue;
        elif int(n) == 1:
            print(f'V = {*func,}')
            minimize(func)
            break;
        elif int(n) == 2:
            func = insertion()
            minimize(func)
            break;

def insertion():
    matrix = []
    rows = input('Введіть кількість масивів: ')
    columns = input('Введіть кількість елементів в кожному масиві: ')
    
    for x in range(0, int(rows)):
        mas = []
        for y in range(0, int(columns)):
            num = input(f'Введіть {y+1}-й елемент {x+1}-ї матриці: ')
            mas.append(int(num))
        cost = input(f'Введіть вартість {x+1}-ої матриці: ')
        mas.append(int(cost))
        matrix.append(mas)
    print(matrix)
    return matrix

def deleting_of_column(matrix, column):
    return [[row[i] for i in range(len(row)) if i != column] for row in matrix]


def min_max_coverage(matrix, letters='АБВГДЕЖЗІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'):
    min_subset = []
    cost = 0
    num_rows = len(matrix)
    num_cols = len(matrix[0]) - 1

   
    sum_of_values = [0] * num_cols
    for col in range(num_cols):
        for row in range(num_rows):
            sum_of_values[col] += matrix[row][col]
    min_column = sum_of_values.index(min(sum_of_values))
    
    max_row = -1
    cost_of_max_row = -1
    for row in range(num_rows):
        if matrix[row][min_column] == 1 and sum(matrix[row]) > cost_of_max_row:
            max_row = row
            cost_of_max_row = sum(matrix[row])
    min_subset.append(letters[max_row])
    cost += matrix[max_row][-1]
    removed_letters = letters[:max_row] + letters[max_row+1:]
    print(letters)
            
    
    for index, x in enumerate(matrix[max_row]):
        if x == 1:
            matrix = deleting_of_column(matrix, index)
    
    if len(matrix[0]) >= 2:
        min_max_coverage(matrix, letters=removed_letters)
    else:
        print(min_subset, cost)


if __name__ == '__main__':
    matrix = [
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 2],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 3],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 2],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 4],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 1]]
    
    while True:
        n = input('''Розрахувати матрицю, задану в умові задачі - введіть 1,
Ввести матрицю власноруч - введіть - 2\n''')
        if (not n.isnumeric()) or (not n in ['1','2']):
            print('Ви ввели не валідні дані, введіть ще раз!')
            continue;
        elif int(n) == 1:
            min_max_coverage(matrix)
            break;
        elif int(n) == 2:
            matrix = insertion()
            min_max_coverage(matrix)
            break;


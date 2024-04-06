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


def full_coverage(matrix):
    letters = 'АБВГДЕЖЗІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    num_rows = len(matrix)
    num_cols = len(matrix[0]) - 1

    # Генеруємо всі можливі підмножини рядків
    subsets = []
    for i in range(1, 2 ** num_rows):
        subset = []
        for j in range(num_rows):
            if (i >> j) & 1:
                subset.append(j)
        subsets.append(subset)

    # Перевіряємо кожну підмножину
    min_subset = None
    cost_of_min_subset = None
    size_of_min_subset = float('inf')
    cheapest_subset = None
    cost_of_cheapest_subset = float('inf')
    coverages = []
    for subset in subsets:
        covered_cols = set()
        total_cost = 0
        for row_index in subset:
            total_cost += matrix[row_index][-1]
            for col_index in range(num_cols):
                if matrix[row_index][col_index] == 1:
                    covered_cols.add(col_index)
        if len(covered_cols) == num_cols:
            coverages.append((subset, total_cost))
            if total_cost < cost_of_cheapest_subset:
                cheapest_subset = subset
                cost_of_cheapest_subset = total_cost
    
    for subset, cost in coverages:
        if len(subset) < size_of_min_subset:
            min_subset = subset
            cost_of_min_subset = cost
            size_of_min_subset = len(min_subset)
            
    excess_coverages = [c for c, k in coverages if len(c) > size_of_min_subset]
    cheapest_subset = [letters[x] for x in cheapest_subset]
    min_subset = [letters[x] for x in min_subset]

    print("Всі покриття з вартістю:")
    for subset, cost in coverages:
        subset = [letters[x] for x in subset]
        print(f"Покриття: {subset}, Вартість: {cost}")
    print("Кількість покриттів:", len(coverages))
    print("Кількість надлишкових покриттів:", len(excess_coverages))
    

    print("Найдешевше покриття:")
    print(f" {cheapest_subset} - Вартість: {cost_of_cheapest_subset}")
    print("Найкоротше покриття:")
    print(f" {min_subset} - Вартість: {cost_of_min_subset}")



if __name__ == '__main__':
    matrix = [
    [0, 0, 0, 0, 1, 0, 1, 1, 0, 3],
    [1, 0, 0, 1, 0, 1, 0, 0, 0, 2],
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 2],
    [0, 1, 0, 0, 0, 1, 1, 0, 1, 3],
    [0, 0, 1, 0, 1, 0, 1, 0, 1, 2],
    [1, 0, 1, 1, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 2]]
    
    while True:
        n = input('''Розрахувати матрицю, задану в умові задачі - введіть 1,
Ввести матрицю власноруч - введіть - 2\n''')
        if (not n.isnumeric()) or (not n in ['1','2']):
            print('Ви ввели не валідні дані, введіть ще раз!')
            continue;
        elif int(n) == 1:
            full_coverage(matrix)
            break;
        elif int(n) == 2:
            matrix = insertion()
            full_coverage(matrix)
            break;
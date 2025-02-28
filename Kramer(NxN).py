def input_matrix(n):
    """Функция для ввода коэффициентов матрицы"""
    print(f"Введите матрицу коэффициентов {n}x{n}:")
    matrix = []
    for i in range(n):
        row = list(map(float, input(f"Введите {n} чисел для строки {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError(f"Ожидается {n} чисел в строке {i + 1}")
        matrix.append(row)
    return matrix


def input_vector(n):
    """Функция для ввода столбца свободных членов"""
    print(f"Введите столбец свободных членов из {n} чисел:")
    vector = list(map(float, input().split()))
    if len(vector) != n:
        raise ValueError(f"Ожидается {n} чисел")
    return vector


def determinant(matrix):
    """Вычисление определителя матрицы"""
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for col in range(n):
        sub_matrix = [row[:col] + row[col + 1:] for row in matrix[1:]]
        det += ((-1) ** col) * matrix[0][col] * determinant(sub_matrix)
    return det


def cramer_rule(A, B):
    """Метод Крамера"""
    n = len(A)
    det_A = determinant(A)

    if det_A == 0:
        raise ValueError("Определитель матрицы A равен нулю, метод Крамера не применим")

    X = []
    for i in range(n):
        A_i = [row[:i] + [B[j]] + row[i + 1:] for j, row in enumerate(A)]
        det_A_i = determinant(A_i)
        X.append(det_A_i / det_A)
    return X


def main():
    try:
        n = int(input("Введите размерность матрицы (N): "))
        if n <= 0:
            raise ValueError("Размерность матрицы должна быть положительным числом")

        A = input_matrix(n)
        B = input_vector(n)

        solution = cramer_rule(A, B)
        print("Решение системы:")
        for i, x in enumerate(solution):
            print(f"x{i + 1} = {x:.2f}")

    except ValueError as e:
        print(f"Ошибка: {e}")

# Запуск программы
main()
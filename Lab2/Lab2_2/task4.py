def input_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))
    matrix = []
    for i in range(rows):
        row = input(f"Введите {cols} чисел для строки {i+1}, через пробел: ").split()
        row = [int(x) if x.isdigit() else float(x) for x in row]
        matrix.append(row)
    return matrix

def transpose(matrix):
    return [list(row) for row in zip(*matrix)]

mat = input_matrix()

print("Исходная матрица:")
for row in mat:
    print(row)

print("Транспонированная матрица:")
for row in transpose(mat):
    print(row)

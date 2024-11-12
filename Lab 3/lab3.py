#27.	Формируется матрица F следующим образом: если в Е сумма чисел по периметру области 1 больше, чем
# количество нулей по периметру области 4, то поменять в С симметрично области 1 и 3 местами, иначе В и Е
# поменять местами несимметрично. При этом матрица А не меняется. После чего вычисляется выражение:((К*AT)*А)-K*FT .
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import random
def rand_filling_mat(size):
    result = []
    for i in range(size):
        random_numbers = [round(random.uniform(-10, 10), 2) for i in range(size)]
        result.append(random_numbers)
    return result
# Генерация матрицы размером(size,size) случайными значениями от -10 до 10 вкл.
def input_mat(size):
    matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            # Запрашиваем у пользователя числа для каждой ячейки
            value = float(input(f"Введите значение для [{i+1}][{j+1}]: "))
            row.append(value)
        matrix.append(row)
    return matrix
# функция ручного ввода чисел в массив
def add_down(mat1,mat2):
    return mat1 + mat2
# добавляет элементы в верхний массив
def add_right(mat1,mat2):
    result = []
    for i, j in zip(mat1, mat2):
        result.append(i+j)
    return result
# добавляет элементы в нижнии массивы
def add_all(mat1,mat2,mat3,mat4):
    result = add_right(add_down(mat1, mat3), add_down(mat2, mat4))
    return result
def perimetr_left(mat):
    elements = []
    for index_i, i  in zip(range(len(mat)), mat):
        for index_j, j  in zip(range(len(i)), i):
            if (index_i == index_j and len(i)//2 + len(i) % 2 > index_i) or index_j == 0 or (index_i == len(i)-index_j-1 and len(i)//2  <= index_i):
                elements.append(j)
    return elements
# поиск элементов периметра левой области
def perimetr_down(mat):
    elements = []
    for index_i, i  in zip(range(len(mat)), mat):
        for index_j, j  in zip(range(len(i)), i):
            if (index_i == len(i)-1) or (index_i == len(i)-index_j-1 and len(i)//2 <= index_i) or (index_i == index_j and len(i)//2 <= index_i):
                elements.append(j)
    return elements
# поиск элементов периметра нижней области
def replace_elements(mat):
    temp_el = 0
    for index_i, i  in zip(range(len(mat)), mat):
        for index_j, j  in zip(range(len(i)), i):
            if (index_i >= index_j and index_i <= len(i)-index_j-1 ):
                temp_el = mat[index_i][index_j]
                mat[index_i][index_j] = mat[len(i)-1-index_i][len(i)-1-index_j]
                mat[len(i) - 1 - index_i][len(i) - 1 - index_j] = temp_el
    return mat
# поменять в матрице «С» симметрично области 1 и 3 местами
def transpon(mat):
    result = []
    rows = len(mat)
    cols = len(mat[0])
    for j in range(cols):
        transposed_row = []
        for i in range(rows):
            transposed_row.append(mat[i][j])
        result.append(transposed_row)
    return result
# Транспонирование Матриц
def print_mat(mat, description):
    print(description+"\n")
    for i in mat:
        print(i)
    print("\n")
def multiply_matrices(matrix1, matrix2):
    result = []
    rows = len(matrix1)
    cols = len(matrix2[0])
    for i in range(rows):
        row = []
        for j in range(cols):
            value = 0
            for k in range(len(matrix2)):
                value += matrix1[i][k] * matrix2[k][j]
            row.append(round(value, 2))
        result.append(row)
    return result
def add_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    return result
def subtract_matrices(matrix1, matrix2):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(round(matrix1[i][j] - matrix2[i][j], 2))
        result.append(row)
    return result
def multiply_k_matric(k, matrix1):
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(round(matrix1[i][j] * k, 2))
        result.append(row)
    return result

k = int(input("введите число к = "))
n = int(input("введите число n = "))
mat_b = input_mat(n)
#mat_b = rand_filling_mat(n)
print_mat(mat_b, "Матрица b")
mat_c = input_mat(n)
#mat_c = rand_filling_mat(n)
print_mat(mat_c, "Матрица c")
mat_d = input_mat(n)
#mat_d = rand_filling_mat(n)
print_mat(mat_d, "Матрица d")
mat_e = input_mat(n)
#mat_e = rand_filling_mat(n)
print_mat(mat_e, "Матрица e")
mat_a = add_all(mat_b, mat_c, mat_d, mat_e)
print_mat(mat_a, "Матрица a")
mat_f = [[mat_b, mat_c], [mat_d, mat_e]]

if sum(perimetr_left(mat_e)) > perimetr_down(mat_e).count(0):
    mat_f[0][1] = replace_elements(mat_c)
    mat_f = add_all(mat_f[0][0], mat_f[0][1], mat_f[1][0], mat_f[1][1])
    print_mat(replace_elements(mat_f), "Измененная матрица С в матрице А(F)")
else:
    mat_f[0][0] = mat_e
    mat_f[1][1] = mat_b
    mat_f = add_all(mat_f[0][0], mat_f[0][1], mat_f[1][0], mat_f[1][1])
    print_mat(mat_f, "Поменяные матрицы B и E местами")

del mat_b
del mat_c
del mat_e
del mat_d

#result = subtract_matrices(multiply_matrices(multiply_k_matric(k, transpon(mat_a)), mat_a), multiply_k_matric(k, transpon(mat_f)))

result1 = transpon(mat_a)
print_mat(result1, "Транспонирование матрицы А")
result1 = multiply_k_matric(k, result1)
print_mat(result1, "Умножение транспонированной матрицы А на К")
result1 = multiply_matrices(result1, mat_a)
print_mat(result1, "Умножение транспонированной матрицы А умноженной на К и матрицы А")
result2 = transpon(mat_f)
print_mat(result2, "Транспонирование матрицы F")
result2 = multiply_k_matric(k, result2)
print_mat(result2, "Умножение транспонированной матрицы F на К")
result = subtract_matrices(result1, result2)
print_mat(result, "Вычитание ")



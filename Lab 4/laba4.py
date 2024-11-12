#27.	Формируется матрица F следующим образом: скопировать в нее А и  если в Е сумма чисел по периметру больше, чем количество
# нулей по периметру , то поменять местами  В и С симметрично, иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
# После чего если определитель матрицы А больше суммы диагональных элементов матрицы F, то вычисляется выражение: A*AT – K * F,
# иначе вычисляется выражение (A-1 +G-F-1)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все
# матричные операции последовательно.
import numpy as np
from matplotlib import pyplot as plt
n = 0
while (n<6): #Условие рационального выбора
    n = int(input("Введите размер матрицы больше 5 "))
k = int(input("Введите коэф. k "))
A = np.random.randint(-10, 11, size=(n, n))  # создание матрицы
F = A.copy()
print(A, "\n")
def conect_mat(mat, mat1, mat2, mat3, mat4): # Функция для сбора матрицы F
    result = mat
    for i,i1 in zip(range(len(mat)//2), range(len(mat1))): #Область B
        for j,j1 in zip(range(len(mat)//2), range(len(mat1))):
            result[i][j] = mat1[i1][j1]
    for i,i1 in zip(range(len(mat)//2), range(len(mat2))): #Область C
        for j,j1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat2))):
            result[i][j] = mat2[i1][j1]
    for i,i1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat3))): #Область D
        for j,j1 in zip(range(len(mat)//2), range(len(mat3))):
            result[i][j] = mat3[i1][j1]
    for i,i1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat4))): #Область E
        for j,j1 in zip(range(len(mat)//2+len(mat)%2,len(mat)), range(len(mat4))):
            result[i][j] = mat4[i1][j1]
    return result
def print_mat(mat,discription): #Вывод матрицы c Наименованием
    plt.matshow(mat)
    plt.title(discription)
    plt.colorbar()
    plt.show()
size = len(A)//2 #Деление матрицы А
if len(A)%2 == 0: #Для четной матрицы А
    B = A[:size, :size]
    C = A[:size, size:]
    D = A[size:, :size]
    E = A[size:, size:]
else: #Для нечетной матрицы А
    B = A[:size, :size]
    C = A[:size, size+1:]
    D = A[size+1:, :size]
    E = A[size+1:, size+1:]
print_mat(A,"Матрица A:\n") #Вывод матриц
print_mat(B,"Матрица B:\n")
print_mat(C,"Матрица C:\n")
print_mat(D,"Матрица D:\n")
print_mat(E,"Матрица E:\n")
perimeter_e = np.concatenate((E[0, :], E[1:-1, -1], E[-1, ::-1], E[1:-1, 0][::-1])).tolist() # Список элементов по периметру матрицы E
if sum(perimeter_e) > perimeter_e.count(0): # Как и какие матрицы B C E D меняем местами
    (B, C) = (np.flip(C, axis=1), np.flip(B, axis=1)) # B и С меняем местами симметрично если сумма элементов периметра E больше
else:
    (B, E) = (E, B) # B и Е меняем местами несимметрично если количество элементов равных 0 периметра E больше
F = conect_mat(F, B, C, D, E) # Функция для сбора матрицы F
print(F, "\n")
print_mat(F,"Матрица F:\n")
diagonal_sum = np.trace(F) + np.trace(np.fliplr(F)) #Сумма элементов Диагоналей
if np.linalg.det(A) > diagonal_sum: # Сравнение Определителя А и Суммы элементов Диагоналей
    result = np.dot(A, np.transpose(A)) - k * F # Если Определитель больше
    discription = "A*AT – K * F"
else:
    result = (np.linalg.inv(A) + np.tril(A) - np.linalg.inv(F)) * k
    discription = "(A-1 +G-F-1)*K"
print_mat(result, discription) #Вывод Итоговой матрицы

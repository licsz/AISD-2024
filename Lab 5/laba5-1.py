#27 F(1) = 1; F(2) = 2; F(n) = (-1)^n*(F(n-1)- F(n-2) /(2n)!) при n > 2.
import time
import matplotlib.pyplot as plt
from functools import lru_cache
import decimal
"""факториал итерационно"""
def fac_it(m,n):
    factorial = 1
    for i in range(m, n + 1):
        factorial *= i
    return factorial
"""факториал рекурсивно"""
@lru_cache(maxsize=None)
def fac_rec(n):
    if n == 1:
        return 1
    return fac_rec(n - 1) * n

"""Вывод матрицы c Наименованием """
def print_mat(mat,discription):
    plt.matshow(mat)
    plt.title(discription)
    plt.colorbar()
    plt.show()

"""Рекурсионный подход"""
@lru_cache(maxsize=None)
def F_recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        result = -1 if n % 2 == 1 else 1
        z = float(decimal.Decimal(F_recursive(n-2))/fac_rec(2*n))
        return result * (F_recursive(n-1) - z)
"""Итерационный подход"""
def F_iterative(n):
    temp = []
    factorial = 2
    r = -1
    for i in range(1, n+1):
        if i == 1:
            temp.append(1)
        elif i == 2:
            factorial = 24
            temp.append(2)
        elif i > 2:
            factorial *= fac_it(((i - 1) * 2) + 1, i * 2)
            r *=(-1)
            z = float(decimal.Decimal(temp[-2])/factorial)
            temp.append(r * (temp[-1] - z))
    return temp[-1]


"""Координаты для графика Рекурсионного подхода"""
data1 = []
"""Координаты для графика Итерационного подхода"""
data2 = []
"""Время рекурсивного продхода"""
execution_time_recursive = 0
"""Время итерационного продхода"""
execution_time_iterative = 0
time_reaction = float(input("Введите макс время реакции "))
"""Количество итераций(Глубина)"""
iteration = 0
"""цикл тестирования времени выполнения, пока вермя одного из подходов не стало больше макс время реакции"""
while max(execution_time_recursive, execution_time_iterative) < time_reaction:
    """Рекурсионный подход"""
    iteration += 1
    """начало замера"""
    start_time = time.perf_counter()
    result = F_recursive(iteration)
    end_time = time.perf_counter()
    F_recursive.cache_clear()
    """конец замера"""
    execution_time_recursive = end_time - start_time
    data1.append((iteration, execution_time_recursive))
    print("Тест рекурсия ", "Результат выполнения: ", result, " Время выполения: ", execution_time_recursive)

    """Итерационный подход"""
    """начало замера"""
    start_time = time.perf_counter()
    result = F_iterative(iteration)
    end_time = time.perf_counter()
    """конец замера"""
    execution_time_iterative = end_time - start_time
    data2.append((iteration, execution_time_iterative))
    print("Тест итерационно ", "Результат выполнения: ", result, " Время выполения: ", execution_time_iterative)
    """итерации с одинаковым временем выполнения"""

"""Преобразование для вывода инф. теста в график и таблицу"""
x1, y1 = zip(*data1)
x2, y2 = zip(*data2)
#y1 = [x * 1000 for x in y1]
#y2 = [x * 1000 for x in y2]
print_mat([x1,y1], "Тест рекурсия")
print_mat([x2,y2], "Тест итерационно")

"""построение графика"""
plt.plot(x1, y1, label='Тест рекурсия')
plt.plot(x2, y2, label='Тест итерационно')

"""добавление легенды"""
plt.legend()
"""добавление заголовка и меток осей"""
plt.title('График зависимости')
plt.xlabel('Ось X, кол-во итераций')
plt.ylabel('Ось Y, Время выполения')
"""вывод графика на экран"""
plt.show()

print(fac_rec(20))
print(fac_it(1,18)*fac_it(19,20))

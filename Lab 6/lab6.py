'''Вариант 27. У юноши P пиджаков, B брюк, R рубашек, G галстуков. Составьте все возможные костюмы из этих предметов.'''
'''Условия усложнения комбинаций: Каждая вещь имеет вес, нужно создать комбинации не превышающие определеную величину веса(переменная weight)'''
import time
from itertools import product
weight = 6
'''Класс без усложненния, для удобного хранения данных'''
class Outfit_simple:
    pants = None
    shirt = None
    jacket = None
    tie = None

    def __init__(self, pants, shirt, jacket = None, tie = None):
        self.pants = pants
        self.shirt = shirt
        self.jacket = jacket
        self.tie = tie
    def __str__(self):
        return f"Outfit: pants - {self.pants}, shirt - {self.shirt}, jacket - {self.jacket}, tie - {self.tie}"

'''Класс с усложненнием, для удобного хранения данных'''
class Outfit_difficult:
    pants = (None, 0)
    shirt = (None, 0)
    jacket = (None, 0)
    tie = (None, 0)
    weight = 0

    def __init__(self, pants, shirt, jacket = (None,0), tie = (None,0)):
        self.pants = pants
        self.shirt = shirt
        self.jacket = jacket
        self.tie = tie
        self.weight = self.pants[1] + self.shirt[1] + self.jacket[1] + self.tie[1]
    def __str__(self):
        return f"Outfit: pants - {self.pants[0]}, shirt - {self.shirt[0]}, jacket - {self.jacket[0]}, tie - {self.tie[0]}, weight = {weight}"


list1 = {"штаны - 'бухта'": 2, "черные джинсы": 3, "бриджи": 1, "Штаны - спорт": 1.5, "Брюки неглаженные": 2,
         "Штаны спец.одежды": 3, "Штаны зимнего комбинезона": 4}
list2 = {"рубашка белая класическая": 1.8, "футболка - airborn": 1, "майка - 'алкоголичка'": 0.7,
         "Рубашка фирменная 'STIHL'": 2, "Рубашка с короткими рукавами": 1.3, "футболка с воротником": 1.5,
         "кофта серая": 2}
list3 = {None: 0, "Пиджак 'Мажор'": 2, "Ветровка": 1.5, "Куртка осенняя длинная": 3.1}
list4 = {None: 0, "cиний": 0.1, "красный в клетку": 0.1, "длинный и синий": 0.3}
'''через циклы безусложнения'''
start_time = time.perf_counter()
result = []
for l1 in list1.keys():
    for l2 in list2.keys():
        for l3 in list3.keys():
            for l4 in list4.keys():
                result.append(Outfit_simple(l1,l2,l3,l4))
end_time = time.perf_counter()
result_time1 = end_time - start_time

it = 0
for i in result:
    it+=1
    print(it, " ",i)
del result

print("______________________________________________________________")
print("______________________ИСПОЛЬЗУЯ-PRODUCT_______________________")
print("______________________________________________________________")
'''через product безусложнения'''
start_time = time.perf_counter()
combinations = product(list1.keys(), list2.keys(), list3.keys(), list4.keys())
result = [Outfit_simple(*combo) for combo in combinations]
end_time = time.perf_counter()
result_time2 = end_time - start_time

it = 0
for i in result:
    it+=1
    print(it, " ",i)
del result

print("______________________________________________________________")
print("_________________________УСЛОЖНЕНИЕ___________________________")
print("______________________________________________________________")
'''через циклы с усложнением'''


start_time = time.perf_counter()
result = []
for key1, value1 in list1.items():
    for key2, value2 in list2.items():
        for key4, value4 in list4.items():
            for key3, value3 in list3.items():
                if value1 + value2 + value3 + value4 <= weight:
                    result.append(Outfit_difficult((key1, value1), (key2, value2), (key3, value3), (key4, value4)))

end_time = time.perf_counter()
result_time3 = end_time - start_time
it = 0
for i in result:
    it+=1
    print(it, " ",i)
del result

print("______________________________________________________________")
print("________________УСЛОЖНЕНИЕ-ИСПОЛЬЗУЯ-PRODUCT__________________")
print("______________________________________________________________")
'''через product с усложнением'''
weight = 6

start_time = time.perf_counter()
result = []

combinations = list(filter(lambda x: list1[x[0]]+list2[x[1]]+list3[x[2]]+list4[x[3]] <= weight, product(list1, list2, list3, list4)))

for x in combinations:
    result.append(Outfit_difficult((x[0], list1[x[0]]),(x[1], list2[x[1]]),(x[2], list3[x[2]]),(x[3], list4[x[3]])))
end_time = time.perf_counter()
result_time4 = end_time - start_time
it = 0

for i in result:
    it+=1
    print(it, " ",i)
del result


print("Время выполнения")
print(result_time1)
print(result_time2)
print(result_time3)
print(result_time4)

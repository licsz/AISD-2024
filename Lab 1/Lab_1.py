#Написать программу, которая читая символы из бесконечной последовательности (эмулируется конечным файлом, читающимся поблочно),
#распознает, преобразует и выводит на экран лексемы по определенному правилу. Лексемы разделены пробелами. Преобразование делать
#по возможности через словарь. Для упрощения под выводом числа прописью подразумевается последовательный вывод всех цифр числа.
#Регулярные выражения использовать нельзя.
#Вариант 27.
#Шеснадцатиричные нечетные числа, не превышающие 409610 и содержащие более К цифр.
#Вывести числа и их количество. Минимальное число вывести прописью.
def convert_hex_to_dec(number):
    digits = '0123456789abcdef'
    result = 0
    position = 1
    for i in number[::-1]:
        result += position * digits.find(i)
        position *= 16
    return result
def check_number(number):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    for i in number:
        if i.lower() in digits:
            continue
        else:
            return False
    return True

result_dict = {}
k = int(input("Введите число К = "))
file = open('text.txt')
main_check = True
main_input = 0
print("число : кол-во")
counter_leksem = 10
checkword = False
while main_check:
    counter = counter_leksem
    word = ""
    mas = []
    while counter > 0:
        a = file.read(1)
        if a == "\n":
            a = " "
        if a == " ":
            if checkword:
                mas.append(word)
                counter = counter - 1
            checkword = False
            word = ""
        else:
            word = word + a
            checkword = True

    mas_dict = {}
    for i in mas:
        mas_dict[i] = mas_dict.get(i, 0)+1

    mas_dict_result = {}

    for i in mas_dict.keys():
        if len(i) > k and check_number(i):
            temp_dec = convert_hex_to_dec(i)
            if temp_dec % 2 == 1 and temp_dec <= 4096:
                mas_dict_result[i] = mas_dict.get(i)

    del mas_dict

    if not mas_dict_result:
        print('Подходящие элементы не были найдены')
    else:
        for i in mas_dict_result:
            print(i + " : " + str(mas_dict_result.get(i)))

    for i in mas_dict_result.keys():
        if result_dict.get(i) is not None:
            result_dict[i] = result_dict.get(i) + mas_dict_result.get(i)
        else:
            result_dict[i] = mas_dict_result.get(i)

    while True:
        main_input = str(input("Прочитать еще " + str(counter_leksem) + " лексем из файла?\n1. Да\n2. Нет. Подвести итог.\nОтвет: "))
        if main_input == "1" or main_input == "2":
            break
    if main_input != "1":
        main_check = False
    else:
        main_check = True

if not result_dict:
    print("Подходящие элементы не были найдены")
else:
    dec_mas = {}
    for i in result_dict.keys():
        dec_mas[convert_hex_to_dec(i)] = i
    print("число : кол-во")
    min = dec_mas.get(min(dec_mas.keys()))
    for i in result_dict:
        print(i+" : " + str(result_dict.get(i)))
    print('минимальное число = ' + min)

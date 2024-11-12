from tkinter import *
from tkinter import ttk
import tkinter as tk
import json
import os
from tkinter.messagebox import showerror, showwarning, showinfo

class Outfit:
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
        self.weight = float(self.pants[1]) + float(self.shirt[1]) + float(self.jacket[1]) + float(self.tie[1])
    def __str__(self):
        return f"Outfit: pants - {self.pants[0]}, shirt - {self.shirt[0]}, jacket - {self.jacket[0]}, tie - {self.tie[0]}, weight = {self.weight} "

# Функция для чтения данных из JSON файла
def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data

# Функция для записи данных в JSON файл
def write_json_file(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f)

# Функция для добавления нового значения в словарь и записи в JSON файл
def add_to_json_file(file_path, key, value):
    data = read_json_file(file_path)
    data[key] = value
    write_json_file(file_path, data)


# Функция для удаления значения из словаря и записи в JSON файл
def delete_from_json_file(file_path, key):
    data = read_json_file(file_path)
    if key in data:
        del data[key]
        write_json_file(file_path, data)
        showinfo(title="Удалено", message=f"Запись {key} удалена",)
    else:
        showerror(title="Ошибка", message="Запись не найдена")



def add_button():
    file_path = select_type.get()
    name = entry_name.get()
    weight = float(entry_weight.get())
    add_to_json_file(str(file_path), name, weight)

def del_button():
    file_path = select_type.get()
    name = entry_name.get()
    delete_from_json_file(str(file_path), name)


class TableWindow1:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title(select_type.get())

        # Создаем таблицу
        self.table = ttk.Treeview(self.parent, columns=("name", "weight"), show="headings")
        yscrollbar = ttk.Scrollbar(self.parent, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        self.table.heading("name", text="Имя")
        self.table.heading("weight", text="Вес")
        self.table.pack()
        # Добавляем данные в таблицу
        data = read_json_file(select_type.get())

        for key, value in data.items():
            para = (key, value)
            self.table.insert("", END, values=para)





class TableWindow2:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title(select_type.get())
        self.parent.resizable(False, False)
        # Создаем таблицу
        self.table = ttk.Treeview(self.parent, columns=("pants", "shirt", "jacket", "tie", "weight"), show="headings")
        yscrollbar = ttk.Scrollbar(self.parent, orient="vertical", command=self.table.yview)
        self.table.configure(yscrollcommand=yscrollbar.set)
        yscrollbar.pack(side="right", fill="y")
        self.table.heading("pants", text="pants")
        self.table.heading("shirt", text="shirt")
        self.table.heading("jacket", text="jacket")
        self.table.heading("tie", text="tie")
        self.table.heading("weight", text="weight")
        self.table.pack()

        for i in result:
            para = (i.pants[0], i.shirt[0], i.jacket[0], i.tie[0], i.weight)
            self.table.insert("", END, values=para)

if __name__ == "__main__":
    file_paths = ["pants.json", "shirt.json", "jacket.json", "tie.json"]
    for file_path in file_paths:
        if not os.path.isfile(file_path):
            # Создаем пустой словарь
            data = {}
            # Записываем словарь в JSON файл
            with open(file_path, "w") as json_file:
                json.dump(data, json_file)

    root = Tk()  # создаем корневой объект - окно
    root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
    root.geometry("600x400+400+200")  # устанавливаем размеры окна
    root.resizable(False, False)


    select_type = StringVar(value=file_paths[0])

    for c in range(12): root.columnconfigure(index=c, weight=1, minsize=50)
    for r in range(12): root.rowconfigure(index=r, weight=1)

    pants_btn = ttk.Radiobutton(text="pants", value=file_paths[0], variable=select_type)
    pants_btn.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")
    shirt_btn = ttk.Radiobutton(text="shirt", value=file_paths[1], variable=select_type)
    shirt_btn.grid(row=0, column=3, columnspan=2, padx=10, pady=10, sticky="nsew")
    jacket_btn = ttk.Radiobutton(text="jacket", value=file_paths[2], variable=select_type)
    jacket_btn.grid(row=0, column=7, columnspan=2, padx=10, pady=10, sticky="nsew")
    tie_btn = ttk.Radiobutton(text="tie", value=file_paths[3], variable=select_type)
    tie_btn.grid(row=0, column=10, columnspan=2, padx=10, pady=10, sticky="nsew")



    entry_name = ttk.Entry()
    entry_name.grid(row=1, column=0, columnspan=8, sticky=EW, ipady=10)
    entry_name.insert(0, "Название")
    entry_weight = ttk.Entry()
    entry_weight.grid(row=1, column=9, columnspan=3, sticky=EW, ipady=10)
    entry_weight.insert(0, 0)
    btn1 = ttk.Button(text="Заменить/Добавить", command=add_button)
    btn1.grid(row=2, column=0, columnspan=7, sticky=EW, ipady=10)
    btn2 = ttk.Button(text="Удалить", command=del_button)
    btn2.grid(row=2, column=8, columnspan=4, sticky=EW, ipady=10)

    result = []
    for key1, value1 in read_json_file(file_paths[0]).items():
        for key2, value2 in read_json_file(file_paths[1]).items():
            for key4, value4 in read_json_file(file_paths[3]).items():
                for key3, value3 in read_json_file(file_paths[2]).items():
                    if value1 + value2 + value3 + value4 <= 6:
                        result.append(Outfit((key1, value1), (key2, value2), (key3, value3), (key4, value4)))

    button = ttk.Button(text="таблица вещей", command=lambda: TableWindow1(tk.Toplevel(root)))
    button.grid(row=3, column=4, columnspan=4, sticky=EW,ipady=10)
    button = ttk.Button(text="Создать Кобинации", command=lambda: TableWindow2(tk.Toplevel(root)))
    button.grid(row=4, column=4, columnspan=4, sticky=EW, ipady=10)
    root.mainloop()
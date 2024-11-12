import tkinter as tk
from tkinter import filedialog, messagebox
import matplotlib.pyplot as plt
import csv
import os

class CreditContract:
    def __init__(self, contract_id, amount, manager):
        self.contract_id = contract_id
        self.amount = amount
        self.manager = manager

    def __str__(self):
        return f"ID: {self.contract_id}, Amount: {self.amount}, Manager: {self.manager}"

class ContractManager:
    def __init__(self):
        self.contracts = []

    def load_contracts(self, filename):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) != 3:
                        raise ValueError("Incorrect data format")
                    contract_id, amount, manager = row
                    amount = float(amount)
                    self.contracts.append(CreditContract(contract_id, amount, manager))
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка загрузка данных: {e}")

    def segment_by_amount(self):
        small, medium, large = 0, 0, 0
        for contract in self.contracts:
            if contract.amount < 1000:
                small += 1
            elif contract.amount < 10000:
                medium += 1
            else:
                large += 1
        return {'малые': small, 'среднии': medium, 'крупные': large}

    def segment_by_manager(self):
        manager_dict = {}
        for contract in self.contracts:
            if contract.manager in manager_dict:
                manager_dict[contract.manager] += 1
            else:
                manager_dict[contract.manager] = 1
        return manager_dict

    def segment_by_amount_plot(self):
        self.plot_pie_chart(self.segment_by_amount(), "сегментированные данные по сумме")

    def segment_by_manager_plot(self):
        self.plot_pie_chart(self.segment_by_manager(), "сегментированные данные по менеджерам")

    def plot_pie_chart(self, data, title):
        labels = data.keys()
        sizes = data.values()
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.title(title)
        plt.savefig("my_plot.png")
        plt.show()


class App:
    def __init__(self, root):
        self.manager = ContractManager()
        self.root = root
        self.root.title("Кредитные контракты")
        self.root.geometry("600x600")
        self.root.resizable(False, False)
        self.load_button = tk.Button(root, text="загрузить контракты", command=self.load_contracts)
        self.load_button.pack()

        self.segment_amount_button = tk.Button(root, text="сегментировать данные по сумме", command=self.segment_by_amount)
        self.segment_amount_button.pack()

        self.segment_manager_button = tk.Button(root, text="сегментировать данные по менеджерам", command=self.segment_by_manager)
        self.segment_manager_button.pack()
        self.canvas = tk.Canvas(root,width=600, height=600)
        self.canvas.pack()
        print()
        if os.path.isfile("my_plot.png"):

            self.image = tk.PhotoImage(file="my_plot.png")  # Убедитесь, что файл существует
            self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image)
        else:
            self.image_id = self.canvas.create_image(0, 0, anchor=tk.NW)
    def update(self):

        if os.path.isfile("my_plot.png"):
            # Убедитесь, что файл существует
            new_photo = tk.PhotoImage(file="my_plot.png")
            # Замена изображения в Canvas
            self.canvas.itemconfig(self.image_id, image=new_photo)
            self.canvas.image = new_photo

    def segment_by_amount(self):
        if len(self.manager.contracts) != 0:
            self.manager.segment_by_amount_plot()
            self.update()
        else:
            messagebox.showinfo("Инфо", f"Нет данных")
    def segment_by_manager(self):
        if len(self.manager.contracts) != 0:
            self.manager.segment_by_manager_plot()
            self.update()
        else:
            messagebox.showinfo("Инфо", f"Нет данных")

    def load_contracts(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if filename:
            self.manager.load_contracts(filename)
            messagebox.showinfo("Инфо", "Контракты загружены")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Крестики-нолики")

        # Инициализация кнопок и игрового поля
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        # Создание кнопок для игрового поля
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.window, text='', font='normal 20 bold', width=5, height=2,
                                               command=lambda row=i, col=j: self.on_button_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)

    def on_button_click(self, row, col):
        # Обработчик нажатия кнопки
        if self.board[row][col] == '' and self.current_player == 'X':
            self.board[row][col] = 'X'
            self.buttons[row][col].config(text='X')
            if self.check_winner('X'):
                messagebox.showinfo("Крестики-нолики", "Вы выиграли!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Крестики-нолики", "Ничья!")
                self.reset_game()
            else:
                self.current_player = 'O'
                self.computer_move()

    def computer_move(self):
        # Ход компьютера с использованием алгоритма Minimax
        best_score = float('-inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '':
                    self.board[i][j] = 'O'
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ''
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)

        if best_move:
            row, col = best_move
            self.board[row][col] = 'O'
            self.buttons[row][col].config(text='O')
            if self.check_winner('O'):
                messagebox.showinfo("Крестики-нолики", "Компьютер выиграл!")
                self.reset_game()
            elif self.is_draw():
                messagebox.showinfo("Крестики-нолики", "Ничья!")
                self.reset_game()
            else:
                self.current_player = 'X'

    def minimax(self, board, depth, is_maximizing):
        # Алгоритм Minimax для нахождения оптимального хода
        if self.check_winner('O'):
            return 1
        elif self.check_winner('X'):
            return -1
        elif self.is_draw():
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'O'
                        score = self.minimax(board, depth + 1, False)
                        board[i][j] = ''
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == '':
                        board[i][j] = 'X'
                        score = self.minimax(board, depth + 1, True)
                        board[i][j] = ''
                        best_score = min(score, best_score)
            return best_score

    def check_winner(self, player):
        # Проверка, выиграл ли текущий игрок
        for row in range(3):
            if all([self.board[row][col] == player for col in range(3)]):
                return True
        for col in range(3):
            if all([self.board[row][col] == player for row in range(3)]):
                return True
        if all([self.board[i][i] == player for i in range(3)]) or all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False

    def is_draw(self):
        # Проверка на ничью
        return all([self.board[row][col] != '' for row in range(3) for col in range(3)])

    def reset_game(self):
        # Сброс игры
        self.board = [['' for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text='')
        self.current_player = 'X'

if __name__ == "__main__":
    TicTacToe()
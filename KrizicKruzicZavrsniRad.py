import tkinter as tk
from tkinter import messagebox

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}
player = 'O'
bot = 'X'


def checkForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True


def checkWhichMarkWon(mark):
    if board[1] == board[2] and board[1] == board[3] and board[1] == mark:
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False


def spaceIsFree(position):
    return board[position] == ' '


def insertLetter(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        buttons[position].config(text=letter)
        if checkForWin():
            if letter == bot:
                messagebox.showinfo("Game Over", "Bot wins!")
            else:
                messagebox.showinfo("Game Over", "Player wins!")
            resetBoard()
        elif checkDraw():
            messagebox.showinfo("Game Over", "It's a draw!")
            resetBoard()
    else:
        messagebox.showerror("Error", "Can't insert there!")


def playerMove(position):
    if spaceIsFree(position):
        insertLetter(player, position)
        compMove()


def compMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)


def minimax(board, depth, isMaximizing):
    if checkWhichMarkWon(bot):
        return 1
    elif checkWhichMarkWon(player):
        return -1
    elif checkDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, depth + 1, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, depth + 1, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


def resetBoard():
    global board
    board = {1: ' ', 2: ' ', 3: ' ',
             4: ' ', 5: ' ', 6: ' ',
             7: ' ', 8: ' ', 9: ' '}
    for button in buttons.values():
        button.config(text='')


root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = {}

for i in range(1, 10):
    button = tk.Button(root, text=' ', font='normal 20 bold', height=3, width=6,
                       command=lambda i=i: playerMove(i))
    button.grid(row=(i-1)//3, column=(i-1) % 3)
    buttons[i] = button

reset_button = tk.Button(
    root, text='Reset', font='normal 20 bold', height=1, width=6, command=resetBoard)
reset_button.grid(row=3, column=1)

root.mainloop()

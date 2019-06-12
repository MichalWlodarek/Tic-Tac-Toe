import tkinter.messagebox
try:
    import tkinter
except ImportError:
    import Tkinter as tkinter

# Declaring button's functions. Empty button when pressed will display 'X', click will turn to False and the next
# button press will produce a 'O' and the click will turn back to True. Count is used to determine whether the match
# was a draw or not. After each button press the game will run through the winning condition function.
def buttonAction(button):
    global click, count
    if button["text"] == "" and click == True:
        button["text"] = "X"
        click = False
        count += 1
        winningCondition()
    elif button["text"] == "" and click == False:
        button["text"] = "O"
        click = True
        count += 1
        winningCondition()
    else:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "This button has already been used!")

# The winning condition function simply checks all possible combinations which allow the player to win with.
def winningCondition():
    global countWin, countWinb
    if (button1["text"] == "X" and button4["text"] == "X" and button7["text"] == "X" or
        button2["text"] == "X" and button5["text"] == "X" and button8["text"] == "X" or
        button3["text"] == "X" and button6["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button2["text"] == "X" and button3["text"] == "X" or
        button4["text"] == "X" and button5["text"] == "X" and button6["text"] == "X" or
        button7["text"] == "X" and button8["text"] == "X" and button9["text"] == "X" or
        button1["text"] == "X" and button5["text"] == "X" and button9["text"] == "X" or
        button3["text"] == "X" and button5["text"] == "X" and button7["text"] == "X"):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player 1 Wins")
        countWin += 1
        playerA.set(countWin)
    elif (button1["text"] == "O" and button4["text"] == "O" and button7["text"] == "O" or
        button2["text"] == "O" and button5["text"] == "O" and button8["text"] == "O" or
        button3["text"] == "O" and button6["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button2["text"] == "O" and button3["text"] == "O" or
        button4["text"] == "O" and button5["text"] == "O" and button6["text"] == "O" or
        button7["text"] == "O" and button8["text"] == "O" and button9["text"] == "O" or
        button1["text"] == "O" and button5["text"] == "O" and button9["text"] == "O" or
        button3["text"] == "O" and button5["text"] == "O" and button7["text"] == "O"):
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "Player 2 Wins")
        countWinb += 1
        playerB.set(countWinb)

    elif count == 9:
        tkinter.messagebox.showinfo("Tic-Tac-Toe", "DRAW!")

# Restart function will reset the game board but not the scores. It will destroy the frame with buttons and then
# reinitialise the frame.
def restart():
    global bFrame, count, click
    bFrame.destroy()
    bFrame = tkinter.Frame(mainWindow)
    bFrame.grid(row=0, column=0, columnspan=3, rowspan=3)
    count = 0
    click = True
    create()

# Creates all the buttons and puts them in a frame
def create():
    global button1, button2, button3, button4, button5, button6, button7, button8, button9
    button1 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button1))
    button1.grid(row=0, column=0)
    button2 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button2))
    button2.grid(row=0, column=1)
    button3 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button3))
    button3.grid(row=0, column=2)
    button4 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button4))
    button4.grid(row=1, column=0)
    button5 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button5))
    button5.grid(row=1, column=1)
    button6 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button6))
    button6.grid(row=1, column=2)
    button7 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button7))
    button7.grid(row=2, column=0)
    button8 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button8))
    button8.grid(row=2, column=1)
    button9 = tkinter.Button(bFrame, text="", font='Arial 20 bold', bg='light blue', fg='black', height=5, width=10, command=lambda: buttonAction(button9))
    button9.grid(row=2, column=2)


mainWindow = tkinter.Tk()
mainWindow.title("Tic-Tac-Toe")
mainWindow.configure(background="dark blue")
button = tkinter.StringVar()
playerA = tkinter.IntVar()
playerB = tkinter.IntVar()
count = 0
countWin = 0
countWinb = 0
click = True
# Keeps track of the player's score
labelA = tkinter.Label(mainWindow, text="Player 1:", font='Arial 20 bold', background="dark blue", fg='white', height=1, width=6)
labelA.grid(row=4, column=0)
label1 = tkinter.Label(mainWindow, textvariable=playerA, font='Arial 20 bold', fg="black")
label1.grid(row=4, column=1)
labelB = tkinter.Label(mainWindow, text="Player 2:", font='Arial 20 bold', background="dark blue", fg='white', height=1, width=6)
labelB.grid(row=5, column=0)
label2 = tkinter.Label(mainWindow, textvariable=playerB, font='Arial 20 bold', fg="black")
label2.grid(row=5, column=1)
button10 = tkinter.Button(mainWindow, text="Reset", font='Arial 20 bold', bg='black', fg='white', height=2, width=10, command=restart)
button10.grid(row=4, column=2, sticky="en")
bFrame = tkinter.Frame(mainWindow)
bFrame.grid(row=0, column=0, columnspan=3, rowspan=3)

create()
mainWindow.mainloop()

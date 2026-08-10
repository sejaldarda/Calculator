from tkinter import *

root = Tk()
root.title(" Calculator")
root.geometry("330x410")

entry = Entry(root, width=20, borderwidth=4, font=('Arial', 20))
entry.grid(row=0, column=0, columnspan=4, pady=10)

def button_click(item):
    entry.insert(END, item)

def clear_display():
    entry.delete(0, END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, END)
        entry.insert(END, result)
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")

buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','+','='
]

row, col = 1, 0
for b in buttons:
    if b == '=':
        Button(root, text=b, width=10, height=2, command=calculate).grid(row=row, column=col, columnspan=2, padx=5, pady=5)
        col += 2
    else:
        Button(root, text=b, width=5, height=2, command=lambda x=b: button_click(x)).grid(row=row, column=col, padx=5, pady=5)
        col += 1
    if col > 3:
        col = 0
        row += 1

Button(root, text='Clear', width=22, height=2, command=clear_display).grid(row=row+1, column=0, columnspan=4, pady=5)

root.mainloop()

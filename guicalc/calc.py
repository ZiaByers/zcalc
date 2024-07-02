from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Calculator")
root.resizable(False, False)

field = Entry(root, width=35, borderwidth=5, justify=RIGHT)
field.bind("<Key>", lambda _: 'break')
field.insert(0, 0)
field.grid(row=0, column=0, columnspan=4)

operator = ""
lastKey = ""
previous_entry = 0


def clear():
    global previous_entry
    previous_entry = 0
    field.delete(0, "end")
    field.insert(0, 0)


def percent():
    x = float(field.get())
    x = x * .01
    field.delete(0, "end")
    field.insert(0, x)


def flip():
    x = float(field.get())
    if x == 0:
        return
    if x > 0:
        field.insert(0, "-")
    else:
        field.delete(0)


def isWhole(x):
    if x % 1 == 0:
        return int(x)
    return x


def addition(x, y):
    z = float(x) + float(y)
    return isWhole(z)


def subtraction(x, y):
    z = float(x) - float(y)
    return isWhole(z)


def multiplication(x, y):
    z = float(x) * float(y)
    return isWhole(z)


def division(x, y):
    z = float(x) / float(y)
    return isWhole(z)


def calculate(key):
    global lastKey
    global previous_entry
    global operator
    current_entry = field.get()
    if current_entry.__contains__(".") and key == ".":
        return
    if isinstance(key, int) or key == ".":
        if current_entry == "0":
            field.delete(0, "end")
        if lastKey in ("+", "-", "x", "/"):
            previous_entry = current_entry
            field.delete(0, "end")
        field.insert("end", key)
    if key in ("+", "-", "x", "/", "=") and operator:
        if operator == "+":
            field.delete(0, "end")
            field.insert(0, addition(previous_entry, current_entry))
        if operator == "-":
            field.delete(0, "end")
            field.insert(0, subtraction(previous_entry, current_entry))
        if operator == "x":
            field.delete(0, "end")
            field.insert(0, multiplication(previous_entry, current_entry))
        if operator == "/":
            if current_entry == "0":
                messagebox.showinfo("error", "Don't divide by 0, ya dingus")
                return
            field.delete(0, "end")
            field.insert(0, division(previous_entry, current_entry))

    if key == "+":
        operator = "+"
    if key == "-":
        operator = "-"
    if key == "x":
        operator = "x"
    if key == "/":
        operator = "/"
    if key == "=":
        operator = ""
    lastKey = key


clear = Button(root, text="C", padx=39, pady=20, command=clear)
negative = Button(root, text="+/-", padx=34, pady=20, command=flip)
percent = Button(root, text="%", padx=38, pady=20, command=percent)
divide = Button(root, text="/", padx=40, pady=20, command=lambda: calculate("/"))

seven = Button(root, text="7", padx=40, pady=20, command=lambda: calculate(7))
eight = Button(root, text="8", padx=40, pady=20, command=lambda: calculate(8))
nine = Button(root, text="9", padx=40, pady=20, command=lambda: calculate(9))
multiply = Button(root, text="X", padx=39, pady=20, command=lambda: calculate("x"))

four = Button(root, text="4", padx=40, pady=20, command=lambda: calculate(4))
five = Button(root, text="5", padx=40, pady=20, command=lambda: calculate(5))
six = Button(root, text="6", padx=40, pady=20, command=lambda: calculate(6))
minus = Button(root, text="-", padx=40, pady=20, command=lambda: calculate("-"))

one = Button(root, text="1", padx=40, pady=20, command=lambda: calculate(1))
two = Button(root, text="2", padx=40, pady=20, command=lambda: calculate(2))
three = Button(root, text="3", padx=40, pady=20, command=lambda: calculate(3))
plus = Button(root, text="+", padx=39, pady=20, command=lambda: calculate("+"))

zero = Button(root, text="0", padx=87, pady=20, command=lambda: calculate(0))
decimal = Button(root, text=".", padx=42, pady=20, command=lambda: calculate("."))
equals = Button(root, text="=", padx=39, pady=20, command=lambda: calculate("="))

clear.grid(row=1, column=0)
negative.grid(row=1, column=1)
percent.grid(row=1, column=2)
divide.grid(row=1, column=3)

seven.grid(row=2, column=0)
eight.grid(row=2, column=1)
nine.grid(row=2, column=2)
multiply.grid(row=2, column=3)

four.grid(row=3, column=0)
five.grid(row=3, column=1)
six.grid(row=3, column=2)
minus.grid(row=3, column=3)

one.grid(row=4, column=0)
two.grid(row=4, column=1)
three.grid(row=4, column=2)
plus.grid(row=4, column=3)

zero.grid(row=5, columnspan=2)
decimal.grid(row=5, column=2)
equals.grid(row=5, column=3)

root.mainloop()

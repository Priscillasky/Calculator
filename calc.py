from tkinter import *

def button_click(number):
    current = input_value.get()
    input_value.set(current + str(number))

def button_clear():
    input_value.set("")

def button_equal():
    try:
        result = eval(input_value.get())
        input_value.set(str(result))
    except:
        input_value.set("Error")

# Create the main window
main = Tk()
main.title("Calculator")

# Create an input field
input_value = StringVar()
display_text = Entry(main, font=("Arial", 20, "bold"), textvariable=input_value, bd=10, insertwidth=4, width=15, justify="right")
display_text.grid(row=0, column=0, columnspan=4)

# Create number buttons
for i in range(9):
    btn = Button(main, text=str(i+1), padx=16, pady=10, bd=8, font=("Arial", 20, "bold"), command=lambda num=i+1: button_click(num))
    btn.grid(row=(i//3)+1, column=i%3)

# Create operator buttons
operators = ['+', '-', '*', '/']
row = 4
col = 0
for operator in operators:
    btn = Button(main, text=operator, padx=16, pady=10, bd=8, font=("Arial", 20, "bold"), command=lambda op=operator: button_click(op))
    btn.grid(row=row, column=col)
    col += 1

# Create other buttons
btn0 = Button(main, text="0", padx=16, pady=10, bd=8, font=("Arial", 20, "bold"), command=lambda: button_click(0))
btn0.grid(row=5, column=0)

btn_clear = Button(main, text="C", padx=16, pady=10, bd=8, font=("Arial", 20, "bold"), command=button_clear)
btn_clear.grid(row=5, column=1)

btn_equal = Button(main, text="=", padx=16, pady=10, bd=8, font=("Arial", 20, "bold"), command=button_equal)
btn_equal.grid(row=5, column=2)

btn_decimal = Button(main, text=".", padx=16, pady=10, bd=8, font=("Arial", 20, "bold"), command=lambda: button_click('.'))
btn_decimal.grid(row=5, column=3)

# Start the main event loop
main.mainloop()

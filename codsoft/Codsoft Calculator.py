import tkinter as tk

def calculate():
    expression = entry.get()
    try:
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

def button_click(symbol):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current + symbol)
def backspace():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])
def clear():
    entry.delete(0, tk.END)
root = tk.Tk()
root.title("CODSOFT Calculator")
root.geometry("401x370")
root.resizable(0,0)
root.configure(bg='blue')
entry = tk.Entry(root, width=14,font=('Times New Roman',40,'bold'),bd=10)
entry.place(x=0, y=0)
buttons = [
    ('7', 0, 90), ('8', 100, 90), ('9', 200, 90), ('/', 300, 90),
    ('4', 0, 145), ('5', 100, 145), ('6', 200, 145), ('*', 300, 145),
    ('1', 0, 200), ('2', 100, 200), ('3', 200, 200), ('-', 300, 200),
    ('0', 0, 255), ('.', 100, 255),  ('+', 300, 255), 
    ('(',0,310),(')',100,310)
]

for button in buttons:
    symbol, x, y = button
    tk.Button(root, text=symbol,width=6,bd=5,font=("Times New Roman",18,'bold'),command=lambda sym=symbol: button_click(sym)).place(x=x, y=y)
tk.Button(root, text="=",bd=5,width=6,font=("Times New Roman",18,'bold'),  command=calculate).place(x=300, y=310)
tk.Button(root,text="<x",bd=5,width=6,font=("Times New Roman",18,'bold'),  command=backspace).place(x=200,y=255)
tk.Button(root, text="Clear",bd=5,width=6,font=("Times New Roman",18,'bold'),  command=clear).place(x=200, y=310)
root.mainloop()

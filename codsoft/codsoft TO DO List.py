from tkinter import *
from tkinter import messagebox
count=1;
def add_your_button():
    global count
    task=v1.get()
    if task:
        l2.insert(END,task)
        count+=1
        e1.delete(0,END)
    else:
        messagebox.showwarning("Warning ","Please Enter Your Task!")
def remove_your_button():
    selected_task_index=l2.curselection()
    if selected_task_index:
        l2.delete(selected_task_index)
    else:
        messagebox.showwarning("WARNING","Please Select a Task to remove!")
def edit_your_button():
    selected_task_index=l2.curselection()
    if selected_task_index:
        selected_task=l2.get(selected_task_index)
        e1.insert(0,selected_task)
        e1.focus()
        new_text=e1.get()
        l2.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning","Please Select a Task to Edit!")
def clear_your_button():
    l2.delete(0,END)
root=Tk()
root.geometry('450x550')
root.title('TO DO LIST')
root.config(bg='blue')
root.resizable(0,0)
l1=Label(root,text=" CODSOFT TO-DO LIST",font=('Roboto',24,'bold'),fg='black',bg='yellow',borderwidth=10)
l1.place(x=1,y=1)
v1=StringVar()
e1=Entry(root,width=30,font=('Roboto',15,'bold'),textvariable=v1,bg='black',fg='light blue',bd=5)
e1.place(x=45,y=80)
e1.focus()
b1=Button(root,text="Add Your Task",font=('Roboto',10,'bold'),width=10,bg='white',fg='black',command=add_your_button)
b1.place(x=160,y=135)
b2=Button(root,text="DELETE TASK",font=('Roboto',10,'bold'),width=13,bg='RED',fg='white',command=remove_your_button)
b2.place(x=30,y=445)
b2=Button(root,text="EDIT TASK",font=('Roboto',10,'bold'),width=13,bg='brown',fg='white',command=edit_your_button)
b2.place(x=155,y=445)
b3=Button(root,text="CLEAR LIST",font=('Roboto',10,'bold'),width=13,bg='GREEN',fg='white',command=clear_your_button)
b3.place(x=280,y=445)
l2=Listbox(root,width=30,bg='beige',bd=5,font=("Roboto",15,'bold'),fg='dark blue')
l2.place(x=45,y=175)
root.mainloop()

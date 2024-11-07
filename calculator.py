from tkinter import *
from tkinter import ttk
root=Tk()
root.title("Calculator")
root.geometry("400x300")
root.resizable(False,False)
root.config(bg="#1f1f1f")
style = ttk.Style()
style.configure("TRadiobutton", background='#1f1f1f',foreground='white')
style.configure("TButton",background="#1f1f1f")

def calculate():
    operator=choice_val.get()
    try:
        a=float(first_entry.get())
        b=float(second_entry.get())
        result.config(state="normal")
        result.delete(0, END)
        if operator=="+":
            result.insert(0,a+b)
        elif operator=="-":
            result.insert(0,a-b)
        elif operator=="*":
            result.insert(0,a*b)
        elif operator=="/":
            if b==0:
                result.insert(0,"Cannot divide by 0")
            else:
                result.insert(0,a/b)
        result.config(state="normal")
    except ValueError:
        result.config(state="normal")
        result.delete(0, END)
        result.insert(0, "Invalid input")
        result.config(state="readonly")

def clear():
    result.config(state="normal")
    result.delete(0,END)
    first_entry.delete(0,END)
    second_entry.delete(0,END)
    result.config(state="readonly")

heading=Label(root,text="Calculator",font=("Aptos",15),bg="#1f1f1f",fg="white")
heading.pack(pady=10)

main_frame=Frame(root,bg="#1f1f1f")
main_frame.pack()

first_number=Label(main_frame,text="First Number : ",bg="#1f1f1f",fg="white")
first_number.grid(row=0,column=0,sticky="w",pady=8)

first_entry=ttk.Entry(main_frame)
first_entry.grid(row=0,column=1)

second_number=Label(main_frame,text="Second Number : ",bg="#1f1f1f",fg="white")
second_number.grid(row=1,column=0,sticky="w",pady=8)

second_entry=ttk.Entry(main_frame)
second_entry.grid(row=1,column=1)

result_label=Label(main_frame,text="Result : ",bg="#1f1f1f",fg="white")
result_label.grid(row=2,column=0,sticky="w")

result=ttk.Entry(main_frame,state="readonly")
result.grid(row=2,column=1,pady=20)

operation_frame=LabelFrame(root,bg="#1f1f1f",fg="white",text="Operations")
operation_frame.pack()

operation_label=Label(operation_frame,text="Choose : ",bg="#1f1f1f",fg="white")
operation_label.grid(row=0,column=0,pady=8,padx=10)

choice_val=StringVar()
add_btn=ttk.Radiobutton(operation_frame,text="+",value="+",variable=choice_val)
add_btn.grid(row=0,column=1)
sub_btn=ttk.Radiobutton(operation_frame,text="-",value="-",variable=choice_val)
sub_btn.grid(row=0,column=2,padx=5)
mul_btn=ttk.Radiobutton(operation_frame,text="x",value="*",variable=choice_val)
mul_btn.grid(row=0,column=3,padx=5)
div_btn=ttk.Radiobutton(operation_frame,text="/",value="/",variable=choice_val)
div_btn.grid(row=0,column=4,padx=5)

button_frame=Frame(root,bg="#1f1f1f")
button_frame.pack()
calculate_btn=ttk.Button(button_frame,text="Calculate",command=calculate)
calculate_btn.grid(row=0,column=0,pady=20,padx=30)
clear_btn=ttk.Button(button_frame,text="Clear",command=clear)
clear_btn.grid(row=0,column=1,pady=20,padx=30)

root.mainloop()
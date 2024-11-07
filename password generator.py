from tkinter import *
from tkinter import ttk
import random
root=Tk()
root.geometry("300x200")
root.title("Password Generator")
root.config(bg="#1f1f1f")
style=ttk.Style()
style.configure("TButton",background="#1f1f1f")

def generate():
    characters= ['r', ')', 'l', 'S', 'y', '*', 'e', 'q', '3', 'W', '@', 'N', '1', 'P', 'H', '6', 'A', '7', 'm', 'i', 'g', 'C', 'J', '$', '%', 'Z', 'x', 'p', 'd', '9', 'B', 'U', 'j', 'b', 'R', 'V', 'h', 't', 'D', 'K', '2', '0', 'T', 'M', 'x', 's', 'F', 'v', '4', '&', 'Q', 'f', 'G', 'X', 'L', '#', '5', 'E', 'c', 'Y', 'O', 'w', 'n', '!', 'u', 'o', 'k', '(', 'a', 'I', '8']
    len = int(entry1.get())
    password = ''
    for i in range (len):
        password+=random.choice(characters)
        label4.config(text=password)
    print(password)

def copy():
    root.clipboard_clear()
    root.clipboard_append(label4.cget("text"))
    
main_frame=Frame(root,bg="#1f1f1f")
main_frame.pack()

label1=Label(main_frame,text="PASSWORD GENERATOR",font=("Aptos",12),bg="#1f1f1f",fg="white")
label1.grid(row=0,column=0,columnspan=2,pady=10)

label2=Label(main_frame,text="Enter password length : ",bg="#1f1f1f",fg="white")
label2.grid(row =1,column=0)

entry1=ttk.Entry(main_frame)
entry1.grid(row=1,column=1,pady=10)

button1=ttk.Button(main_frame,text="Generate",command=generate)
button1.grid(row=2,column=0,columnspan=2)

label3=Label(main_frame,text="Your password : ",bg="#1f1f1f",fg="white")
label3.grid(row=3,column=0,sticky="w",pady=10)

label4=Label(main_frame,text="",bg="#1f1f1f",fg="white")
label4.grid(row=3,column=1,columnspan=2,sticky="w")

copy_button=ttk.Button(main_frame,text="Copy",command=copy)
copy_button.grid(row=4,column=0,columnspan=2)

main_frame.mainloop()

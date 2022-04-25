from tkinter import *
import tkinter.messagebox as messagebox

tk=Tk()
tk.title('Аuthorization')
tk.geometry('500x500')
tk.resizable(width=False, height=False)

def make_label(text):
    return Label(text=text,font=("Comic Sans MS", 24, "bold"))
make_label('Login').place(x=50,y=150)
make_label('Password').place(x=50,y=250)

def button_click():
    v=Login.get()
    d=Password.get()
    if v=='Admin' and d=='Qwerty123':
        messagebox.showinfo(title='Аuthorization', message='Authorization completed')
    else:
        messagebox.showinfo(title='Аuthorization', message='Invalid login or password')
    login.delete(0, END)
    password.delete(0, END)

def make_logo(t):
    img=PhotoImage(file='log.png')
    lbl_img=Label(t)
    lbl_img.image=img
    lbl_img['image']=lbl_img.image
    lbl_img.place(x=180, y=20)

make_logo(tk)

Login=StringVar()
Password=StringVar()
login=Entry(font=("Comic Sans MS", 20, "bold"), width=15, textvariable=Login)
password=Entry(font=("Comic Sans MS", 20, "bold"), width=15, textvariable=Password)
login.get()
password.get()
login.place(x=200,y=150)
password.place(x=200,y=250)

btn=Button(tk, text='Аuthorization', width=15, height=1, bg='#aaffff',font=("Comic Sans MS", 20, "bold"), command=button_click)
btn.place(x=130, y=350)

tk.mainloop()
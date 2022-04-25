from tkinter import *

def baton():
    if v1.get() == 1:
        lab['bg'] = 'blue'
    elif v1.get() == 2:
        lab['bg'] = 'red'
    elif v1.get() == 3:
        lab['bg'] = 'green'
    elif v1.get() == 4:
        lab['bg'] = 'pink'


root = Tk()
tx = Text(root,width=40,height=3,font='14')
v1 = IntVar()
sca = Scale(root,orient=HORIZONTAL,length=400,from_=1,to=4,tickinterval=1,resolution=1,variable=v1)
sca.pack()

bat = Button(text='Click', font=('Arial',40),command=baton)
bat.pack()

lab = Label(text='Меняю цвет', font=('Arial',40))
lab.pack()

root.mainloop()
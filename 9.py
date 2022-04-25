import tkinter as tk
import cmath
def bat():
    desk= ((int(entry.get())**2) - (4*int(entry1.get())*int(entry2.get())))**0.5
    desk = float(desk)
    if desk != 0 and desk>0:
        x1= (-int(entry1.get())+desk)/2
        x2= (-int(entry1.get())-desk)/2
        text.delete("1.0", tk.END)
        text.insert("1.0", f'The discriminant is: {desk}\n')
        text.insert("1.0", f'X1 is: {x1}\n')
        text.insert("1.0", f'X2 is: {x2}\n')
    elif desk == 0:
        x12= -int(entry1.get())/2
        text.delete("1.0", tk.END)
        text.insert("1.0", f'The discriminant is: {desk}\n')
        text.insert("1.0", f'X1,2 is: {x12}\n')
    else:
        text.delete("1.0", tk.END)
        text.insert("1.0", f'The discriminant is: {desk}\n')
        text.insert("1.0", 'This equation has no solutions\n')

window = tk.Tk()
window.title('Quadratic calculator')

label = tk.Label(text='x**2+', font=('Arial', 20))
label.grid(row=0,column=1)
label1 = tk.Label(text='x+', font=('Arial', 20))
label1.grid(row=0,column=3)
label2 = tk.Label(text='=0', font=('Arial', 20))
label2.grid(row=0,column=5)

entry = tk.Entry(font=('Arial', 20))
entry.grid(row=0,column=0)
entry1 = tk.Entry(font=('Arial', 20))
entry1.grid(row=0,column=2)
entry2 = tk.Entry(font=('Arial', 20))
entry2.grid(row=0,column=4)

button = tk.Button(text='Solve', font=('Arial', 20), command=bat)
button.grid(row=0,column=6)

text = tk.Text(bg='lightblue', font=('Arial', 20))
text.grid(row=1,columnspan=7)
window.mainloop()
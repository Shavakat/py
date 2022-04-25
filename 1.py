import tkinter as tk
import tkinter.messagebox as mb

def bat():
    mb.showinfo('Задание 2', f'Ваше ФИО - {entry.get()} {entry1.get()} {entry2.get()}')
    
window=tk.Tk()
window.title('Задание') 
window.configure(bg='#FFC0CB')

label = tk.Label(text='Фамилия', font=('Arial',40), fg='#008080')
label.grid(row=0, column=0)
label1 = tk.Label(text='Имя', font=('Arial',40), fg='#008080')
label1.grid(row=1, column=0)
label2 = tk.Label(text='Отчество', font=('Arial',40), fg='#008080')
label2.grid(row=2, column=0)

entry = tk.Entry(font=('Arial',40), fg='#008080')
entry.grid(row=0, column=1)
entry1 = tk.Entry(font=('Arial',40), fg='#008080')
entry1.grid(row=1, column=1)
entry2 = tk.Entry(font=('Arial',40), fg='#008080')
entry2.grid(row=2, column=1)

button=tk.Button(text='Вывести сообщение', bg='#00FF7F', font=('Arial',40), fg='#008080', command=bat)
button.grid(row=3, column=1)

window.mainloop()

import tkinter as tk
def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"
def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()
window.title('Задание 2')
window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)
btn_decrease = tk.Button(master=window, text="-", bg='#00FF7F', font=('Comic',100), fg='#08D9D6', command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")
lbl_value = tk.Label(master=window, text="0", bg='#08D9D6', font=('Comic',100), fg='#EAEAEA')
lbl_value.grid(row=0, column=1)
btn_increase = tk.Button(master=window, text="+", bg='#00FF7F', font=('Comic',100), fg='#08D9D6', command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")
window.mainloop()

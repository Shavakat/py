import random
import tkinter as tk
def roll():
	lbl_result["text"] = str(random.randint(1, 6))

window = tk.Tk()
btn_roll = tk.Button(text="Бросить", command=roll,
font=("Comic Sans MS", 20, "bold"),bg='pink')
lbl_result = tk.Label(font=("Comic Sans MS", 20, "bold"),bg='green',fg='white')

btn_roll.grid(row=0, column=0, sticky="nsew")
lbl_result.grid(row=1, column=0)


window.mainloop()

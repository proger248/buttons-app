import tkinter as tk
import time

window = tk.Tk()
window.title("Приложение с кнопками")
window.resizable(False, False)

def btn1_clicked():
    time.sleep(10)


btn1 = tk.Button(text="Игрок 1", command=btn1_clicked, bg="#a6a4a4", height=15, width=100)
btn2 = tk.Button(text="Игрок 2", command=btn1_clicked, bg="#a6a4a4", height=15, width=100)
btn3 = tk.Button(text="Игрок 3", command=btn1_clicked, bg="#a6a4a4", height=15, width=100)
btn1.pack()
btn2.pack()
btn3.pack()

window.mainloop()

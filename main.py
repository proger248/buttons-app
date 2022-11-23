import tkinter as tk
import time

window = tk.Tk()
window.title("Приложение с кнопками")
# window.geometry('900x700')
window.resizable(False, False)


def wait():
    time.sleep(10)


def btn1_clicked():
    # # btn1.configure(bg="#ffea00")
    # btn2["state"] = "disabled"
    # btn3["state"] = "disabled"
    # # btn1.configure(bg="#a6a4a4")
    # # btn2["state"] = "normal"
    wait()


btn1 = tk.Button(text="Игрок 1", command=btn1_clicked, bg="#a6a4a4", height=15, width=100)
btn2 = tk.Button(text="Игрок 2", command=btn1_clicked, bg="#a6a4a4", height=15, width=100)
btn3 = tk.Button(text="Игрок 3", command=btn1_clicked, bg="#a6a4a4", height=15, width=100)
btn1.pack()
btn2.pack()
btn3.pack()

window.mainloop()

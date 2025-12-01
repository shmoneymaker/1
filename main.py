import tkinter as tk
from tkinter import *

root = tk.Tk()
root.iconbitmap(default="free-icon-music-7797380.ico")

root.title("привет")
root.geometry("300x250")

label_1_привет = Label(text = "привет")
label_1_привет.pack()

root.mainloop()

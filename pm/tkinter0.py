from tkinter import *

root = Tk()
root.title("Пошёл на")
root.geometry("400x500")
label = Label(root, text="ОГО")
label.pack()
b = Button(root, text="Саша спит", command=lambda: label.config(text="Саша спит"))

b.pack()

root.mainloop()
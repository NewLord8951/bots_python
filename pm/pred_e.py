import tkinter as tk

r = tk.Tk()
r.title(" ")
r.geometry("100x100+5+500")
q = tk.Label(r, text="README FILE PYTHON OKEY", font=("Arial", 1, "bold"), bg = "Black", fg = "Dark Blue", pady = 1, padx = 1, ipady = 1, ipadx = 1)
q.pack()
w = tk.Entry(r, show="*")
b = tk.Button(r, command="a")
r.mainloop()
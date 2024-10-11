import tkinter as tk
from functools import partial

def square(x):
    return x*x

root = tk.Tk()
var = tk.IntVar(root, value=0) #the variable the gets passed to the class call
menu = tk.OptionMenu(root, var, *[0,1,2,3,4,5]) #a drop-down list to choose a value for the variable
menu.pack()
button = tk.Button(root, text='click', command = lambda x=var.get(): square(x)) #a button that calls the class
button.pack()
root.mainloop()
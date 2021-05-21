"""
Hello World Tkinter
"""
import tkinter as tk

window = tk.Tk()
greeting = tk.Label(
    text='Hello World!',
    foreground='white',
    background='black',
    width=10,
    height=10
)
greeting.pack()
window.mainloop()

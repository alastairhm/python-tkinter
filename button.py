"""
Button Tkinter
"""
import tkinter as tk

window = tk.Tk()
button = tk.Button(
    text='Click me!',
    width=25,
    height=5,
    background='blue',
    foreground='yellow',
)
button.pack()
window.mainloop()

"""
Entry Widgets Tkinter
"""
import tkinter as tk

widgets = []

window = tk.Tk()
widgets.append(tk.Label(text='Name'))
widgets.append(tk.Entry())
widgets.append(tk.Text())

for wid in widgets:
    wid.pack()

window.mainloop()

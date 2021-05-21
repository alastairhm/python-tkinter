import tkinter as tk

window = tk.Tk()

def handle_keypress(event):
    print(event.char)

def handle_click(event):
    print('The Button was clicked!')

button = tk.Button(text='Click me!')
button.pack()


# Bind keypress event to handle_keypress()
window.bind('<Key>', handle_keypress)
window.bind('<Button-1>', handle_click)

window.mainloop()

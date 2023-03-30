from tkinter import Tk, Label, Entry, Button

window = Tk()

label = Label(window, text="Are you human?")
label.grid()

entry = Entry(window)
entry.grid()

button = Button(window, text="submit")
button.grid()

window.mainloop()
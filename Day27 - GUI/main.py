import tkinter

from matplotlib.pyplot import title

window = tkinter.Tk()
window.title("First GUI Program, Not Technically")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="Here is a Label")
my_label.pack()

window.mainloop()
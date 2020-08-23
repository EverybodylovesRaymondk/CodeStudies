import tkinter as Tk

root = Tk()
text = input('What is yout name ? ')
myLabel = Tk.Label(root, text='Hello {}'.format(text))
myLabel.pack()
root.mainloop()
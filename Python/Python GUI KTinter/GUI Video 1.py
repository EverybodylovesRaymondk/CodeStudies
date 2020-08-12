import tkinter

root = Tk()
text = input('What is yout name ? ')
myLabel = Label(root, text='Hello {}'.format(text))
myLabel.pack()
root.mainloop()
# imports every file form tkinter and tkinter.ttk 
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('Canvas')
root.geometry('400x800')


w = 300
h = 600
x = w//2
y = h//2

my_canvas = Canvas(root, width = w, height = h, bg = "white")
my_canvas.pack(pady=50)

my_square = my_canvas.create_rectangle(x, y, x + 30, y + 30, fill="blue")



def left(event):
    x = -30
    y = 0
    my_canvas.move(my_square, x, y)

def right(event):
    x = 30
    y = 0
    my_canvas.move(my_square, x, y)

def up(event):
    x = 0
    y = -30
    my_canvas.move(my_square, x, y)

def down(event):
    x = 0
    y = 30
    my_canvas.move(my_square, x, y)

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)


root.mainloop()
<<<<<<< Updated upstream
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
=======
from tkinter import *

def hello(event):
    print("Single Click, Button-l")
def quit(event):
    print("Double Click, so let's stop")
    import sys; sys.exit()

widget = Button(None, text='Mouse Clicks')
widget.pack()
widget.bind('<Up>', moveUp())
widget.bind('<Double-1>', quit)
widget.mainloop()

def moveUp():
    

'''
master = Tk()

canvas_width = 300
canvas_height = 600
w = Canvas(master, 
           width=canvas_width,
           height=canvas_height)
w.pack()
>>>>>>> Stashed changes

for i in range(21):
    y = int(canvas_height * i / 20)
    w.create_line(0, y, canvas_width, y, fill="#476042")

<<<<<<< Updated upstream

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
=======
for k in range(11):
    x = int(canvas_width * k / 10)
    w.create_line(x, 0, x, canvas_height, fill="#476042")



w.create_rectangle(30, 30, 60, 60, fill="blue")
'''

mainloop()
>>>>>>> Stashed changes

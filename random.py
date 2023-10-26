import tkinter
import random

canvas = tkinter.Canvas(bg='white', width=400, height=300)
canvas.pack()

for i in range(random.randint(10 ,20)):
    x = random.randrange(400)
    y = random.randrange(300)
    r = 10
    farba = random.choice(('red', 'blue', 'green'))
    canvas.create_oval(x-r, y-r, x+r, y+r, fill=farba)

import tkinter

canvas = tkinter.Canvas(width=600, height=200)
canvas.pack()

obr = tkinter.PhotoImage(file='python.png')
canvas.create_image(500, 100, image=obr)

for x in range(100):
   canvas.move(1, -5, 0)
   canvas.update()
   canvas.after(100)

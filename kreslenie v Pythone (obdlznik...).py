
import tkinter

canvas=tkinter.Canvas(width=800,height=600,background="white")
canvas.pack()

premenna = tkinter.PhotoImage(file="had.png")

canvas.create_image(300,200,image=premenna)

id1 = canvas.create_line(10, 20, 30, 40)
id2 = canvas.create_oval(10, 20, 30, 40)

canvas.delete(id1)


id1 = canvas.create_line(10, 20, 30, 40)
id2 = canvas.create_oval(10, 20, 30, 40)
canvas.move(id2, -5, 10)

id1 = canvas.create_line(10, 20, 30, 40)
id2 = canvas.create_oval(10, 20, 30, 40)
canvas.itemconfig()

id1 = canvas.create_line(10, 20, 30, 40)
id2 = canvas.coords(il, 30, 40, 50, 60, 70, 80, 90)


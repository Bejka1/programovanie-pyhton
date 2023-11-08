import tkinter, random

canvas= tkinter.Canvas(bg="white", width= 300,height=300)
canvas.pack()
for i in range(1000):
    x= random.randrange(300)
    y= random.randrange(300)
    if y < 150:
        if x <150:
            farba = "red"
        else:
            farba="blue"
    else:
        farba= "green"
        if y >150:
            if x > 150:
                farba="yellow"
    canvas.create_oval(x-5,y-5,x+5,y+5,fill=farba, outline="")
    


   

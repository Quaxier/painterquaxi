from tkinter import *

color = 'black'
p = 1
lastx1, lasty1 = 0, 0

def painterpg():
    painter = Tk()
    painter.geometry('600x600')
    painter.title('그림판')
    painter.resizable(0, 0)

    def paint(event):
        global lastx1, lasty1
        lastx1, lasty1 = event.x, event.y
        x1, y1 = (event.x - p), (event.y - p)
        x2, y2 = (event.x + p), (event.y + p)
        canvas.create_oval(x1, y1, x2, y2, fill=color, outline=color)

    def change_black():
        global color
        color = 'black'

    def change_red():
        global color
        color = 'red'

    def change_blue():
        global color
        color = 'blue'

    def change_green():
        global color
        color = 'green'

    def increase_p():
        global p
        p = p + 1
        if p > 50:
            p = 50

    def decrease_p():
        global p
        p = p - 1
        if p < 1:
            p = 1

    def clear():
        canvas.delete('all')

    def erase():
        global color
        color = '#f0f0f0'

    canvas = Canvas(painter, width=400, height=400, relief = "solid", bd = 3)
    canvas.pack(side = "top")
    canvas.bind('<B1-Motion>', paint)

    b1 = Button(painter, bg='red', width=3, height=1, command=change_red)
    b2 = Button(painter, bg='blue', width=3, height=1, command=change_blue)
    b3 = Button(painter, bg='green', width=3, height=1, command=change_green)
    b4 = Button(painter, text='UP', font='Arial', width=6, height=1, command=increase_p)
    b5 = Button(painter, text='DOWN', font='Arial', width=6, height=1, command=decrease_p)
    b6 = Button(painter, text='전체 지우기', font='Arial', width=8, height=1, command=clear)
    b7 = Button(painter, text='지우개', font='Arial', width=6, height=1, command=erase)
    b8 = Button(painter, bg='black', width=3, height=1, command=change_black)

    b1.place(x=0, y=575)
    b2.place(x=30, y=575)
    b3.place(x=60, y=575)
    b4.place(x=20, y=0)
    b5.place(x=20, y=35)
    b6.place(x=515, y=5)
    b7.place(x=0, y=530)
    b8.place(x=90, y=575)

    painter.mainloop()
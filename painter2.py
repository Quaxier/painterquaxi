import tkinter

color = 'black'
p = 1
lastx1, lasty1 = 0, 0

def painterpg2():

    # 기본 설정
    painter = tkinter.Tk()
    painter.geometry('600x600')
    painter.title('그림판')
    painter.resizable(0, 0)

    # 프레임 설정
    frame_canvas = tkinter.Frame(painter, width = 400, height = 400, relief = "solid", bd = 3)
    frame_canvas.pack(anchor = "center")
    frame_label = tkinter.Frame(painter, width = 300, height = 100, relief = "solid", bd = 3)
    frame_label.pack()
    frame_button = tkinter.Frame(painter, width = 66, height = 400, relief = "solid", bd = 3)
    frame_button.pack(anchor = "w")
    frame_button.place(x = 0, y = 0)

    # 캔버스 설정
    canvas = tkinter.Canvas(frame_canvas, width = 400, height = 400, cursor = "pencil")

    # 페인트 툴
    def paint(event):
        global lastx1, lasty1
        lastx1, lasty1 = event.x, event.y
        x1, y1 = (event.x - 0.1), (event.y - 0.1)
        x2, y2 = (event.x + 0.1), (event.y + 0.1)
        canvas.create_line(x1, y1, x2, y2, fill = color, width = p)

    def painting(event):
        global lastx1, lasty1
        canvas.create_line(lastx1, lasty1, event.x, event.y, fill = color, width = p)
        lastx1, lasty1 = event.x, event.y

    # 색 지정
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

    def change_yellow():
        global color
        color = 'yellow'

    # 선 굵기 지정
    def scroll(event):
        global p
        if p < 20:
            if event.delta == 120:
                p += 1
        if p > 1:
            if event.delta == -120:
                p -= 1
        else:
            pass

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

    # 전체 지우기, 지우개 툴
    def clear():
        canvas.delete('all')

    def erase():
        global color
        color = '#f0f0f0'

    # 메인화면으로 나가기
    def exit():
        from main_window1 import painter_main
        painter.destroy()
        painter_main()

    # 캔버스 설정 2
    canvas.bind('<Button-1>', paint)
    canvas.bind("<B1-Motion>", painting)
    canvas.bind('<MouseWheel>', scroll)
    canvas.pack()

    # 버튼 설정
    b_black = tkinter.Button(painter, bg='black', width=3, height=1, command=change_black)
    b_red = tkinter.Button(painter, bg='red', width=3, height=1, command=change_red)
    b_blue = tkinter.Button(painter, bg='blue', width=3, height=1, command=change_blue)
    b_green = tkinter.Button(painter, bg='green', width=3, height=1, command=change_green)
    b_yellow = tkinter.Button(painter, bg='yellow', width=3, height=1, command=change_yellow)
    b_eraser = tkinter.Button(painter, text='지우개', font='Arial', width=6, height=1, command=erase)
    b_thickup = tkinter.Button(painter, text='펜 굵기 증가', font='Arial', width=9, height=1, command=increase_p)
    b_thickdown = tkinter.Button(painter, text='펜 굵기 감소', font='Arial', width=9, height=1, command=decrease_p)
    b_eraseall = tkinter.Button(painter, text='전체 지우기', font='Arial', width=9, height=1, command=clear)
    b_mainwindow = tkinter.Button(painter, text='메인화면', font='Arial', width=9, height=1, command=exit)

    # 버튼 배치
    b_black.place(x=3, y=3)
    b_red.place(x=33, y=3)
    b_blue.place(x=3, y=28)
    b_green.place(x=33, y=28)
    b_yellow.place(x=3, y=53)
    b_eraser.place(x=0, y=530)
    b_thickup.place(x=3, y=100)
    b_thickdown.place(x=3, y=135)
    b_eraseall.place(x=507, y=5)
    b_mainwindow.place(x=507, y=40)

    painter.mainloop()

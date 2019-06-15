import tkinter
from painter1 import painterpg
from painter2 import painterpg2

def painter_main():
    main_window = tkinter.Tk()
    main_window.title("그림판 메뉴")
    main_window.geometry("200x200+100+100")
    main_window.resizable(False, False)

    def start_painter():
        main_window.destroy()
        painterpg()

    def start_painter2():
        main_window.destroy()
        painterpg2()

    def close_painter():
        main_window.destroy()

    button1 = tkinter.Button(main_window, text = '그림판 실행', command = start_painter,
                             anchor = "center", width = 10, height = 1)
    button2 = tkinter.Button(main_window, text = '그림판 백업', command = start_painter2,
                             anchor = "center", width = 10, height = 1)
    button3 = tkinter.Button(main_window, text = '종료', command = close_painter,
                             anchor = "center", width = 10, height = 1)

    button1.place(x=65, y=20)
    button2.place(x=65, y=90)
    button3.place(x=65, y=160)

    main_window.mainloop()

if __name__ == "__main__":
    painter_main()
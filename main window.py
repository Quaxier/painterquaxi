import tkinter
from painter1 import painterpg
from tkinter import messagebox

def painter_main():
    main_window = tkinter.Tk()
    main_window.title("그림판 메뉴")
    main_window.geometry("200x200+100+100")
    main_window.resizable(False, False)

    def start_painter():
        main_window.destroy()
        painterpg()

    def close_painter():
        question_box = tkinter.messagebox.askquestion(title = '종료', message = '종료 하시겠습니까?')
        if question_box == 'yes':
            main_window.destroy()
        else:
            pass

    button1 = tkinter.Button(main_window, text = '그림판 실행', command = start_painter, anchor = "s",
                             width = 10, height = 1).place(x = 65, y = 40)
    button2 = tkinter.Button(main_window, text = '종료', command = close_painter, anchor = "s",
                             width = 10, height = 1).place(x = 65, y = 130)

    main_window.mainloop()

if __name__ == "__main__":
    painter_main()
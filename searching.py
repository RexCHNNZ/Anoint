import webbrowser
from tkinter import *

def Search():
    # Initializing the main GUI window
    win = Tk()
    win.title('Alex - Search/Encyclopedia Mode')
    win.geometry('330x80')
    win.resizable(0,0)
    win.iconbitmap("src\search_icon.ico")
    win.config(background="#4fb39f")

    # Function 2 Search/Encyclopedia
    def get_input1():
        webbrowser.open("https://bing.com/search?q="+entry1.get())
    def get_input2():
        webbrowser.open("https://baike.baidu.com/item/"+entry1.get())
    entry1 = Entry(win)
    entry1.grid(row=0,column=0,ipadx=100)
    btn1 = Button(win, text="Search on Bing", command=get_input1)
    btn1.grid(row=1,column=0)
    btn2 = Button(win, text="Baidu Encyclopedia", command=get_input2)
    btn2.grid(row=2,column=0)
    win.mainloop()
Search()
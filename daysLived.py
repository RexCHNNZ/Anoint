from tkinter import *
import keyboard
import datetime

def DaysLived():
    # Initializing the main GUI window
    root = Tk()
    root.title('Alex - Days Lived Mode')
    root.geometry('450x70')
    root.iconbitmap("src\days_icon.ico")
    root.resizable(0, 0)
    root.config(background="#0f4c5c")

    # Function 4 Days Lived
    frame = Frame(root)
    entryYear = Entry(frame)
    entryYear.insert(0, "Year: (please replace)")
    entryMonth = Entry(frame)
    entryMonth.insert(0, "Month: (please replace)")
    entryDay = Entry(frame)
    entryDay.insert(0, "Day: (please replace)")
    label = Label(frame)

    def CalcDays():
        birthYear = int(entryYear.get())
        birthMonth = int(entryMonth.get())
        birthDay = int(entryDay.get())
        birth = datetime.date(birthYear, birthMonth, birthDay)
        ansOfCalc = "You have lived for " + str(current.__sub__(birth).days) + " days"
        label.config(text = ansOfCalc)

    Btn = Button(root, text ="Calculate", command = CalcDays)
    keyboard.add_hotkey("enter", lambda: CalcDays())
    entryYear.grid(row = 0, column = 0, ipadx = 18)
    entryMonth.grid(row = 0, column = 1)
    entryDay.grid(row = 0, column = 2)
    currentYear = int(datetime.datetime.now().strftime('%Y'))
    currentMonth = int(datetime.datetime.now().strftime('%m'))
    currentDay = int(datetime.datetime.now().strftime('%d'))
    current = datetime.date(currentYear,currentMonth,currentDay)
    label.grid(row = 1, column = 0)
    Btn.grid(row = 1, column = 0)
    frame.grid(row = 0)

    root.mainloop()
DaysLived()
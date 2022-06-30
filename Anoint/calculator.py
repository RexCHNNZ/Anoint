from tkinter import *
import keyboard

# Initializing the main GUI window
root = Tk()
root.title('Alex - Calculator Mode')
root.geometry('424x52')
root.resizable(0, 0)
root.iconbitmap("src\calculator_icon.ico")
root.config(background="#0f4c5c")

# Function 1 Calculator
frame = Frame(root)
entry = Entry(frame)
label = Label(frame)

def Calculator():
    def Calc():
        try:
            results = str(eval(expression.get()))
            ansOfCalc = "= " + results
            label.config(text = ansOfCalc)
        except ZeroDivisionError:
            label.config(text = errorZero)
        except NameError:
            label.config(text = errorName)
        except SyntaxError:
            label.config(text = errorSyn)
    
    expression = StringVar()

    entry['textvariable'] = expression
    Btn = Button(root, text ="Calculate", command = Calc)
    keyboard.add_hotkey("enter", lambda: Calc())
    entry.grid(row = 0,column = 0, ipadx = 60)
    label.grid(row = 0,column = 1)
    Btn.grid(row = 1,column = 0)
    frame.grid(row = 0)

    root.mainloop()

Calculator()
root.mainloop()
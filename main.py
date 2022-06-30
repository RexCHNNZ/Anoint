import sys
import keyboard
import webbrowser
from tkinter import *
sys.path.append('calculator.py')
sys.path.append('daysLived.py')
sys.path.append('searching.py')
sys.path.append('quiz.py')
sys.path.append('planefight.py')

print('There are three functions:')
print('1) Calculator')
print('2) Search')
print('3) Quiz')
print('4) Days Lived')
print('5) Play Plane Fight GAME!')

choice = int(input('Enter your choice:\n'))
if choice == 1:
    import calculator
elif choice == 2:
    import searching
elif choice == 3:
    import quiz
elif choice == 4:
    import daysLived
elif choice == 5:
    import planefight
else:
    print("Invalid Input!")
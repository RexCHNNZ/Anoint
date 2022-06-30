from tkinter import *
from tkinter import messagebox as mb
import json
import random

print('''Alex: Please choose the quiz topic: 
        1. Chemistry
        2. Computer Science
        3. Biology
        4. Physics
        5. Capital City''')
topic = int(input())

root = Tk()
root.geometry("950x600")
root.title("Alex - Quiz Mode")
root.iconbitmap("src\quiz_icon.ico")

with open('quiz.json') as f:
    obj = json.load(f)
if topic == 1:
    q = (obj['cheques'])
    options = (obj['cheoptions'])
    a = (obj['cheans'])
elif topic == 2:
    q = (obj['csques'])
    options = (obj['csoptions'])
    a = (obj['csans'])
elif topic == 3:
    q = (obj['bioques'])
    options = (obj['biooptions'])
    a = (obj['bioans'])
elif topic == 4:
    q = (obj['phyques'])
    options = (obj['phyoptions'])
    a = (obj['phyans'])
elif topic == 5:
    q = (obj['capques'])
    options = (obj['capoptions'])
    a = (obj['capans'])
z = zip(q, options, a)
l = list(z)
random.shuffle(l)
q,options,a=zip(*l)


class Quiz:
    def __init__(self):
        self.qn = 0
        self.qno = 1
        self.quest = StringVar()
        self.ques = self.question(self.qn)
        self.opt_selected = IntVar()
        self.opts = self.radiobtns()
        self.display_options(self.qn)
        self.buttons()
        self.correct = 0

    def question(self, qn):
        t = Label(root, text="Quiz", width=120, height=2, bg="#00008b", fg="white", font=("Consolas", 20))
        t.place(x=0, y=2)
        self.quest.set(str(self.qno)+". "+q[qn])
        qn = Label(root, textvariable = self.quest, width=60, font=("Georgia", 10, "bold"), anchor="w")
        qn.place(x=70, y=100)
        return qn

    def radiobtns(self):
        val = 0
        b = []
        yp = 150
        while val < 4:
            btn = Radiobutton(root, text=" ", variable=self.opt_selected, value=val + 1, font=("Georgia", 14))
            b.append(btn)
            btn.place(x=100, y=yp)
            val += 1
            yp += 40
        return b

    def display_options(self, qn):
        val = 0
        self.opt_selected.set(0)
        self.ques['text'] = q[qn]
        for op in options[qn]:
              self.opts[val]['text'] = op
              val += 1

    def buttons(self):
        nbutton = Button(root, text="Next",command=self.nextbtn, width=10,bg="green",fg="white",font=("Consolas",16,"bold"))
        nbutton.place(x=200,y=380)
        quitbutton = Button(root, text="Quit", command=root.destroy,width=10,bg="red",fg="white", font=("Consolas",16,"bold"))
        quitbutton.place(x=400,y=380)

    def checkans(self, qn):
        if self.opt_selected.get() == a[qn]:
             return True
        
    def nextbtn(self):
        if self.checkans(self.qn):
            self.correct += 1
        self.qn += 1
        self.qno += 1
        if self.qn == 10:
            self.display_result()
            root.destroy()
        else:
            self.quest.set(str(self.qno)+". "+q[self.qn])
            self.display_options(self.qn)       
        

    def display_result(self):
        score = int(self.correct / 10 * 100)
        result = "Score: " + str(score) + "%"
        wc = 10 - self.correct
        correct = "No. of correct answers: " + str(self.correct)
        wrong = "No. of wrong answers: " + str(wc)
        mb.showinfo("Result", "\n".join([result, correct, wrong]))



quiz=Quiz()
root.mainloop()
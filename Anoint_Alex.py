import random
import re
import bs4
import urllib.request
from bs4 import BeautifulSoup
import urllib.parse
import sys
import time
import random
from random import randint
import datetime

daysInAYear = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
daysFromBeginningOfYear = 0

def calculator():
    expression = input("Alex: Enter you equation:")
    time.sleep(1)
    print(eval(expression))
def encyclopedia():
    search_item = input("Alex: Enter what you want to search:")
    print("Alex: Please wait...")
    try:
        url = "https://baike.baidu.com/item/"+urllib.parse.quote(search_item)
        html = urllib.request.urlopen(url)
        content = html.read().decode('utf-8')
        html.close()
        soup = BeautifulSoup(content, "html.parser")
        text = soup.find('div', class_="lemma-summary").children
        print("Alex: Search result:")
        for x in text:
            word = re.sub(re.compile(r"<(.+?)>"),'',str(x))
            words = re.sub(re.compile(r"\[(.+?)\]"),'',word)
            print(words)
    except AttributeError:
        print("Alex: Failed *crys*")
def quiz():
    time.sleep(1)
    print("Alex: Which of the following topics would you like the quiz to be about?")
    print("      1) Capital cities of countries")
    print("      2) Chemistry")
    print("      3) Computer Science")
    topic = int(input())
    if topic == 1:
        capital()
    elif topic == 2:
        chemistry()
    elif topic == 3:
        cs()
    else:
        print("Alex: Invalid topic selected, please try again")
        print("Alex: Which of the following topics would you like the quiz to be about?")
        print("Alex: 1) Capital cities of countries")
        print("      2) Chemistry")
        print("      3) Computer Science")
        topic = int(input())
def capital():
    easy = [["Alex: What is the capital city of China?","beijing"],["Alex: What is the capital city of the United Kingdom?","london"],["Alex: What is the capital city of the United States of America?","washington"],["Alex: What is the capital city of France?","paris"],["Alex: What is the capital city of Germany?","berlin"],["Alex: What is the capital city of Spain?","madrid"],["Alex: What is the capital city of Italy?","rome"],["Alex: What is the capital city of South Korea?","seoul"],["Alex: What is the capital city of Japan?","tokyo"],["Alex: What is the capital city of the largest country in the world?","moscow"],["Alex: Cairo is the capital city of which country?","egypt"],["Alex: Which place in Southeast Asia is both a capital city and a country?","singapore"]]
    medium = [["Alex: Known as the windiest city, what is the capital city of New Zealand?","wellington"],["Alex: What is the capital city of Australia?","canberra"],["Alex: What is the capital city of Canada?","ottawa"],["Alex: What is the capital city of India?","new delhi"],["Alex: What is the capital city of Mexico?","mexico city"],["Alex: Which country hosts the 2022 FIFA World Cup and has Doha as its capital city?","qatar"],["Alex: What is the capital of the American state which has a basketball team that just became the 2022 NBA champions?","sacramento"],["Alex: Bern is the capital city of which European country?","switzerland"],["Alex: Which European capital city shares the same name as a green vegetable?","brussels"],["Alex: What is the capital state of Texas?","austin"],["Alex: Which African country has 3 capital cities?","south africa"],["Alex: What is the capital city of Malaysia?","kuala lumpur"]]
    hard = [["Alex: What is the capital city of the country that is currently ranked first in the world for FIFA mens football team?","brasilia"],["Alex: What is the capital city of the country with the most significant length:width ratio?","santiago"],["Alex: What is the capital city of the country that is to the East of the Andes Mountains?","buenos aires"],["Alex: What is the capital city of the country that is located in the North Atlantic Ocean and is surrounded by water?","reykjavik"],["Alex: Which country has the capital city Montevideo and has won the first ever FIFA World Cup?","uruguay"],["Alex: What is the capital city of the country where IKEA is founded?","stockholm"],["Alex: Addis Ababa is the capital city of which African country?","ethiopia"],["Alex: What is the capital city of the country with a double-triangle shaped flag?","kathmandu"],["Alex: What is the capital city of Croatia?","zagreb"],["Alex: Which country has the lowest average elevations in the world and has Male as its capital city?","maldives"]]
    score = 0
    easyChose = [0 for i in range(0,11)]
    mediumChose = [0 for i in range(0,11)]
    hardChose = [0 for i in range(0,9)]
    time.sleep(1)
    print("Alex: Choose the difficulty: Easy (e), Medium (m) or Hard (h)(warning: hard difficulty is linked to knowledges of other fields)")
    difficulty = input()
    inde = random.randint(0,11)
    indm = random.randint(0,11)
    indh = random.randint(0,9)
    if difficulty != "e" and difficulty != "m" and difficulty != "h":
        print("Alex: Invalid difficulty selected, please try again")
        print("Alex: Choose the difficulty: Easy (e), Medium (m) or Hard (h)")
        difficulty = input()
    elif difficulty == "e":
        for i in range(6):
            time.sleep(1)
            print(easy[inde][0])
            easyChose[inde] = True
            ans = input()
            if ans.lower() == easy[inde][1]:
                score = score + 1
                time.sleep(1)
                print("Alex: Your answer is correct :b")
            else:
                print("Alex: Your answer is incorrect, the correct answer is "+easy[inde][1].title())
            while easyChose[inde]:
                inde = random.randint(0,11)
        time.sleep(1)
        print("Alex: You got "+str(score)+" out of 6.")
        score = 0
    elif difficulty == "m":
        for i in range(6):
            time.sleep(1)
            print(medium[indm][0])
            mediumChose[indm] = True
            ans = input()
            if ans.lower() == medium[indm][1]:
                score = score + 1
                time.sleep(1)
                print("Alex: Your answer is correct :b")
            else:
                print("Alex: Your answer is incorrect, the correct answer is "+medium[indm][1].title())
            while mediumChose[indm]:
                indm = random.randint(0,11)
        time.sleep(1)
        print("Alex: You got "+str(score)+" out of 6.")
        score = 0
    elif difficulty == "h":
        for i in range(6):
            time.sleep(1)
            print(hard[indh][0])
            hardChose[indh] = True
            ans = input()
            if ans.lower() == hard[indh][1]:
                score = score + 1
                time.sleep(1)
                print("Alex: Your answer is correct :b")
            else:
                print("Alex: Your answer is incorrect, the correct answer is "+hard[indh][1].title())
            while hardChose[indh]:
                indh = random.randint(0,9)
        time.sleep(1)
        print("Alex: You got "+str(score)+" out of 6.")
def chemistry():
    pereasy = [["Alex: What is the most reactive non-metal?","fluorine"],["Alex: What is the name of the first element in the Periodic Table?","hydrogen"],["Alex: What is the name of the element with symbol C?","carbon"],["Alex: What is the symbol of oxygen?","o"],["Alex: What is the name of group 8 (helium, neon, argon etc.)?","noble gas"],["Alex: Which group is called the alkali metals?","group 1"],["Alex: What is the name of the gas that makes up 78 percent of air?","nitrogen"],["Alex: What is the boiling point of pure water in degrees Celsius?","100"],["Alex: What is the most reactive non-radioactive metal?","potassium"],["Alex: Which industrial process is used to make ammonia?","haber process"],["Alex: Which hydrocarbon group has the general formula CnH2n?","alkenes"]]
    perhard = [["Alex: Does the density of metals increase down group 1? (true of false)","true"],["Alex: What is the symbol of tin?","sn"],["Alex: Which element has the symbol Pb?","lead"],["Alex: Which carbon conducts electricity?","graphite"],["Alex: What is the only liquid metal under room temperature?","mercury"],["Alex: What is the most recent element discovered on the periodic table (element 118)?","oganesson"],["Alex: What is the word used to describe the feature that metals can be drawn into wires?","ductile"],["Alex: What is the name of KMnO4?","potassium permanganate"],["Alex: What is the name of the ester formed from C2H5OH and CH3COOH?","ethyl ethanoate"],["Alex: What is the equation of the catalyst used in the Contact Process?","v2o5"],["Alex: What is the name of the catalyst used in Hydrogenation reaction?","nickel"]]
    easyChose = [0 for i in range(0,40)]
    hardChose = [0 for i in range(0,40)]
    score = 0
    time.sleep(1)
    print("Alex: Choose the difficulty: Easy (e) or Hard (h)")
    difficulty = input()
    inde = random.randint(0,len(pereasy))
    indh = random.randint(0,len(perhard))
    if difficulty != "e" and difficulty != "h":
        print("Alex: Invalid difficulty selected, please try again")
        print("Alex: Choose the difficulty: Easy (e) or Hard (h)")
        difficulty = input()
    elif difficulty == "e":
        for i in range(6):
            time.sleep(1)
            print(pereasy[inde][0])
            easyChose[inde] = True
            ans = input()
            if ans.lower() == pereasy[inde][1]:
                score = score + 1
                time.sleep(1)
                print("Alex: Your answer is correct :p")
            else:
                time.sleep(1)
                print("Alex: Your answer is incorrect, the correct answer is "+pereasy[inde][1].title())
            while easyChose[inde]:
                inde = random.randint(0,len(pereasy))
        time.sleep(1)
        print("Alex: You got "+str(score)+" out of 6.")
        score = 0
    elif difficulty == "h":
        for i in range(6):
            time.sleep(1)
            print(perhard[indh][0])
            hardChose[indh] = True
            ans = input()
            if ans.lower() == perhard[indh][1]:
                score = score + 1
                time.sleep(1)
                print("Alex: Your answer is correct :p")
            else:
                time.sleep(1)
                print("Alex: Your answer is incorrect, the correct answer is "+perhard[indh][1].title())
            while hardChose[indh]:
                indh = random.randint(0,len(perhard))
        time.sleep(1)
        print("Alex: You got "+str(score)+" out of 6.")
        score = 0
def cs():
    cseasy = [["Alex: Convert the binary number 11 to denary","3"],["Alex: Convert the hexadecimal number 3A to 8-bit binary","00111010"],["Alex: How many bits of data do serial data transmission transmit at one time?(write a number)","1"],["Alex: True or false? Half-duplex data transmission transmits data in both directions at the same time","false"],["Alex: Which touchscreen cannot be used with gloved hands?","capacitive"],["Alex: What is the full name of LCD?","liquid crystal display"],["Alex: True of false? OLED technology uses back-lighting","false"],["Alex: Which register is used to hold results from a calculation?(write its abbreviation)","acc"],["Alex: Is address bus unidirectional or bidirectional?","unidirectional"],["Alex: Which shape is used to represent process in a flowchart?","rectangle"],["Alex: Which process is represented by a diamond shape in a flowchart?","decision"]]
    cshard = [["Alex: True or false? Assemble language uses mnemonics?","true"],["Alex: Which optical storage uses concentric tracks?","dvd-ram"],["Alex: What is the full name of DVD?","digital versatile disk"],["Alex: What is the sequence of the registers down the fetch-decode-execute cycle?(use a - to separate)","pc-mar-mdr-cir"],["Alex: True or false? Freeware is copyleft","false"],["Alex: True or false? Python doesn't have post-condition iteration structure","true"],["Alex: What is the full name of MAC(address)?","media access control"],["Alex: True or false? DLP technology uses micro-mirrors","true"],["Alex: What is the full name of URL?","uniform resource locator"],["Alex: Is firewall a software or a hardware or both?","both"],["Alex: What is the other separate layer in TLS beside handshake layer?","record"]]
    easyChose = [0 for i in range(0,11)]
    hardChose = [0 for i in range(0,10)]
    score = 0
    print("Alex: Choose the difficulty: Easy (e) or Hard (h)")
    difficulty = input()
    inde = random.randint(0,11)
    indh = random.randint(0,10)
    if difficulty != "e" and difficulty != "h":
        print("Alex: Invalid difficulty selected, please try again")
        print("Alex: Choose the difficulty: Easy (e) or Hard (h)")
        difficulty = input()
    elif difficulty == "e":
        for i in range(6):
            time.sleep(1)
            print(cseasy[inde][0])
            easyChose[inde] = True
            ans = input()
            if ans.lower() == cseasy[inde][1]:
                score = score + 1
                time.sleep(1)
                print("Alex: Your answer is correct :b")
            else:
                time.sleep(1)
                print("Alex: Your answer is incorrect, the correct answer is "+cseasy[inde][1].title())
            while easyChose[inde]:
                inde = random.randint(0,11)
        time.sleep(1)
        print("Alex: You got "+str(score)+" out of 6.")
        score = 0
    elif difficulty == "h":
        for i in range(6):
            time.sleep(1)
            print(cshard[indh][0])
            hardChose[indh] = True
            ans = input()
            if ans.lower() == cshard[indh][1]:
                score = score + 1
                time.sleep(1)
                print("Alex: Your answer is correct :b")
            else:
                time.sleep(1)
                print("Alex: Your answer is incorrect, the correct answer is "+cshard[indh][1].title())
            while hardChose[indh]:
                indh = random.randint(0,10)
        time.sleep(1)
        print("Alex: You got "+str(score)+" out of 6.")
        score = 0

def dayslived():
    time.sleep(1)
    birthYear = int(input("Alex: Please enter your year of birth: "))
    time.sleep(1)
    birthMonth = int(input("Alex: Please enter your month of birth: "))
    time.sleep(1)
    birthDay = int(input("Alex: Please enter your day of birth: "))
    time.sleep(2)
    birth = datetime.date(birthYear,birthMonth,birthDay)
    currentYear = int(datetime.datetime.now().strftime('%Y'))
    currentMonth = int(datetime.datetime.now().strftime('%m'))
    currentDay = int(datetime.datetime.now().strftime('%d'))
    current = datetime.date(currentYear,currentMonth,currentDay)
    print("Alex: You have lived for "+str(current.__sub__(birth).days)+" days")

line1 = ["Alex: Greetings, my name is Alex, what is your name?","Alex: Hello, I'm Alex, could you tell me your name?","Alex: Hi, this is Alex, what's your name?"]
print(random.choice(line1))
name = input()
line2 = [", how are you doing?",", how are you?", ", what's up?"]
time.sleep(1)
print("Alex: Hello", name.title() + random.choice(line2))
how = input()
howl = how.lower()
comfort = ["Sorry to hear that :( hope you feel better soon","Awwww :’( hope you get over it soon"]
cheer = ["Glad you are doing fine :D","Good to hear that :)"]
time.sleep(1)
if "bad" in howl or "sad" in howl or "annoyed" in howl or "angry" in howl or "frustrated" in howl or "furious" in howl or "irritated" in howl or "infuriated" in howl or "seething" in howl or "blue" in howl or "depressed" in howl or "disappointed" in howl or "empty" in howl or "gloomy" in howl or "hurt" in howl or "rejected" in howl or "remorseful" in howl or "worthless" in howl or "despair" in howl or "anxious" in howl or "worried" in howl or "bored" in howl:
    print("Alex: "+random.choice(comfort))
else:
    print("Alex: "+random.choice(cheer))
time.sleep(2)
select = 999999999
bye = ["Bye, take care...","See you next time...","Goodbye..."]
while select != 0:
    print("Alex: These are my 3 functions:")
    print("      1. Calculator (enter 1)")
    print("      2. Encyclopedia in Chinese (enter 2)")
    print("      3. Quiz (enter 3)")
    print("      4. Calculate how many days you lived (enter 4)")
    print("      0. Exit (enter 0)")
    select = int(input())
    if select == 1:
        calculator()
        time.sleep(2)
    elif select == 2:
        encyclopedia()
        time.sleep(2)
    elif select == 3:
        quiz()
        time.sleep(2)
    elif select == 4:
        dayslived()
        time.sleep(2)
    else:
        print("Alex: Exit")
time.sleep(1)
print("Alex: "+random.choice(bye))
time.sleep(5)
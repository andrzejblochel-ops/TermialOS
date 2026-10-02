secretCode = 6501477


import os
import time
import random
from math import *
user=input("Input a username: ")
time.sleep(0.5)
inf=99999999
splashes=[
    "We hate bloatware!",
    "Joke powered operating system!",
    "May contain bloatware!",
    "sudo rm -rf /!",
    "System32!",
    "Sudo? we don't do that here!",
    "Made with 64 braincells!",
    "Has its own kernel! (might be a lie)",
    "Certified to run!™",
    "Powered by Python and some random stuff!",
    "50*2+24 lines of code!"
]
print("    T E R M I A L  O S  1 . 0  BUILD 3    ")
print(f"     {random.choice(splashes)}    ")
while True:
    termial_os=input(f"Termial:|System64|{user}>")
    #Just the restart
    if termial_os=="restart":
        print("    T E R M I A L  O S  BUILD 3    ")
        print(f"    {random.choice(splashes)}    ")
        #Shutdown the system.
    elif termial_os=="shutdown":
        print("Turning off Termial OS...")
        time.sleep(0.5)
        quit()
        #Help message
    elif termial_os=="help":
        print("help:Types this message")
        print("shutdown:Turns off the OS")
        print("restart:Restarts the OS")
        print("calc:Opens up the calculator")
        print("dice:Just a dice")
        print("test:Test message")
        print("newfeature:Check new features")
        print("openfile:Opens files")
        print("notepad:Notepad that saves files onto your machine")
        #Calculator
    elif termial_os=="calc":
        while True:
            print("Calculator 1.0")
            print("How to use:")
            print("add=additon,sub=subtraction,mlt=multiplication,div=division,sqrt=square root")
            calculator=input(f"Termial:|System64|{user}|Calculator1.0>")
            if calculator == "end":
                break
            elif calculator == "add":
                a = int(input("a = "))
                b = int(input("b = "))
                print(f"{a} + {b} = {a+b}")
            elif calculator == "sub":
                a = int(input("a = "))
                b = int(input("b = "))
                print(f"{a} - {b} = {a-b}")
            elif calculator == "mlt":
                a = int(input("a = "))
                b = int(input("b = "))
                print(f"{a} * {b} = {a*b}")
            elif calculator == "div":
                a = int(input("a = "))
                b = int(input("b = "))
                print(f"{a} / {b} = {a/b}")
            elif calculator == "sqrt":
                a = int(input("sqrt(a = "))
                print(f"sqrt({a}) = {sqrt(a)}")
    elif termial_os=="dice":
        print("Litterally just a dice.")
        dice = int(input("How many times? "))
        for i in range(dice):
            print(f"Dice:{random.randint(1,6)}")
    elif termial_os=="test":
        print("This might stay as a test feature and will not be included in the release 1.0.")
    elif termial_os=="newfeature":
        print("New features:")
        time.sleep(0.3)
        print("sqrt Function added to Calculator!")
        time.sleep(0.2)
        print("New splash text depicting how many lines of code are there using math.")
        time.sleep(0.1)
        print("File opener, but since i don't know how to make notepad on this, i added in a little secret")
        time.sleep(0.4)
        print("Notepad that saves files onto your actual machine, but not the OS")
    elif termial_os=="openfile":
        while True:
            open = input("OpenFile:")
            if open == "poo.txt":
                print("CONTENTS OF poo.txt:")
                poop = int(input("passcode: "))
                if poop == secretCode:
                    print("File not found, may be corrupted or deleted.")
    elif termial_os == "notepad":
        while True:
            notepad=input("")
            if notepad == "end":
                break
            elif notepad == "save":
                saveFile = input("(please do a file format because it could turn into a file)Name of file: ")
                UserName=input("What is your user name? (check this in C:/Users)")
                print("Saving file...")
                time.sleep(0.5)
                file = f"C:\\Users\\{UserName}\\Desktop\\{saveFile}"
                with open(file, "w", encoding='utf-8') as f:
                    f.write(f"{notepad}")




#There's no fucking nucking ducking way someone's gonna wait for 3.17 years for this fucking message XD
time.sleep(inf)
turnoff_message=(
    "There's no fucking way you waited for this message, what a waste of your life.",
)
print(turnoff_message)
time.sleep(1)
print("Shutting down Termial OS...")
time.sleep(2)
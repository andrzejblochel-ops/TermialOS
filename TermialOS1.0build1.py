import time
import random
import math
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
    "Has its own kernel!",
    "Certified to run!™",
    "Powered by Python and some random stuff!"
]
print("    T E R M I A L  O S  1 . 0  BUILD 1    ")
print(f"    {random.choice(splashes)}    ")
while True:
    termial_os=input(f"Termial:|System64|{user}>")
    #Just the restart
    if termial_os=="restart":
        print("    T E R M I A L  O S  BUILD 1    ")
        print(f"    {random.choice(splashes)}    )
        #Shutdown the system.
    elif termial_os=="shutdown":
        print("Turning off Termial OS...")
        quit()
        time.sleep(0.5)
        #Help message
    elif termial_os=="help":
        print("help:Types this message")
        print("shutdown:Turns off the OS")
        print("restart:Restarts the OS")
        print("calc:Opens up the calculator")
        print("dice:Just a dice")
        #Calculator
    elif termial_os=="calc":
        print("Calculator 1.0")
        print("How to use:")
        print("add=additon,sub=subtraction,mlt=multiplication,div=division")
    elif termial_os=="mlt":
        a=int(input("a = "))
        b=int(input("b = "))
        time.sleep(0.5)
        print(f"{a}*{b}={a*b}")
    elif termial_os=="add":
        a=int(input("a = "))
        b=int(input("b = "))
        time.sleep(0.5)
        print(f"{a}+{b}={a+b}")
    elif termial_os=="div":
        a=int(input("a = "))
        b=int(input("b = "))
        time.sleep(0.5)
        print(f"{a}/{b}={a/b}")
    elif termial_os=="sub":
        a=int(input("a = "))
        b=int(input("b = "))
        time.sleep(0.5)
        print(f"{a}-{b}{a-b}")
    elif termial_os=="dice":
        print("Litterally just a dice.")
        print(f"Dice:{random.randint(1,6)}")

#There's no fucking nucking ducking way someone's gonna wait for 3.17 years for this fucking message XD
time.sleep(inf)
turnoff_message=(
    "There's no fucking way you waited for this message, what a waste of your life.",
)
print(turnoff_message)
time.sleep(1)
print("Shutting down Termial OS...")
time.sleep(2)

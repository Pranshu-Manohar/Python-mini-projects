
# USE RANDOM LIB AND IF ELSE STATEMENT AND USE IT 
# AGR USER LO OR MATCH KHELNA HAI TO USKE LIYE LOOP LGA LO 
import random
import pyttsx3
engine=pyttsx3.init

a=int(input("number of games:- "))
i=1
pyttsx3.speak("Press 2 for Tails")
pyttsx3.speak("Press 1 for head")

while(i<=a):
    b=int(input(":> "))
    x=["Heads","Tails"]
    c=random.choice(x)
    if(c=="Heads"):
        b="Heads"
        pyttsx3.speak("and this is heads, User wins the toss., haa  heehe haa haa  ")
    else:
        pyttsx3.speak("Sorry you loose")
        
    if(a>i):
        pyttsx3.speak("next match")
    i=i+1

    


import random

#IT IS A STONE PAPER GAME 
#
# I WILL TAKE INPUT FROM THE USER AND THE RANDOM NUMBER FROM THE COMPUTER 
# I WILL DECLARE THE INPUTS TO THE STONE PAPER AND SCISSOR
# IT IS GOING TO BE EASY BUT NOT THAT MUCH . 
'''
STEP1- TAKE INPUT FROM THE USER

STEP2- TAKE THE RANDOM NUMBER OR USE THE CHOISE FUNCTION TO COOSE FROM THE STONE PAPER AND SCISSOR FROM THE COMPUTER 

STEP3= USER HAVE TO GIVE THE INPUT FROM THE INDEX POV

STEP4- SHOW THE OUTPUT OF BOTH 

STEP5= USE IF ELSE TO DECLARE THE WINNER AND USE in  STATEMENT 

STEP6- AFTER THE COMPARISION DONE THEN PRINT THE RESULT

STEP7= YOU CAN ALSO USE THE WHOLE CODE IN LOOP FOR THE SERIES LEVEL GAME 

'''
# E Enoy the coding - QUICK SUCESS NEVER GIVES HAPPINESS 
import pyttsx3
engine=pyttsx3.init
print("IN THIS GAME YOU HAVE THE RIGHT AMOUNT OF TIME TO SELEct  YOU OPTIONS :)")

matches=int(input("Enter the number of matches :-> "))
print("1 for stone")
print("2 for paper")
print("3 for scissor")

i=1
while(i<=matches):


        # pyttsx3.speak("Thala for a reason")
        user=int(input("Enter your choise:-> "))
        comp=random.randint(1,3)
        # comp=random.choice(1,3)

        if(user==comp):
                pyttsx3.speak("IT'S A DRAW !")
                print("IT'S A DRAW")

        elif(user==1 and comp==2):
                pyttsx3.speak("Computer wins ")
                print("Computer wins")
                # print("user=stone\n comp= paper")

        elif(user==1 and comp==3):
                pyttsx3.speak("User wins")
                print("***User wins***")

        elif(user==2 and comp==1):
                print("***User wins***")
                pyttsx3.speak("USer wins")

        elif(user==2 and comp==3):
                print("***Comp wins***")
                pyttsx3.speak("Computer Wins")

        elif(user==3 and comp==1):
                print("***comp wins***")
                pyttsx3.speak("Computer wins")

        elif(user==3 and comp==2):
                print("***User wins***")
                pyttsx3.speak("User wins")

        elif(comp==1 and user==2):
                print("***Computer wins*** ")
                pyttsx3.speak("Computer wins")     

        elif(comp==1 and user==3):
                print("***User wins***")
                pyttsx3.speak("User wins")

        elif(comp==2 and user==1):
                print("***User wins***")
                pyttsx3.speak("user wins")

        elif(comp==2 and user==3):
                print("***Comp wins***")
                pyttsx3.speak("Computer wins")

        elif(comp==3 and user==1):
                print("***comp wins***")
                pyttsx3.speak("Computer wins")

        elif(comp==3 and user==2):
                print("***User wins***")
                pyttsx3.speak("User wins")
        
        i=i+1
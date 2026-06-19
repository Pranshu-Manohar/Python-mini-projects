import math
add=lambda x,v:x+v
sub=lambda x,v:x-v
mul=lambda x,v:x*v
div=lambda x,v:x/v

def root():
    a=int(input("Enter the number:- "))
    print(math.sqrt(a))

def fact():
    a=int(input("Enter the number:- "))
    print(math.factorial(a))

print("press 1 for add")
print("press 2 for sub")
print("press 3 for mul")
print("press 4 for div")
print("press 5 for sqrroot")
print("press 6 for factorial")

try:
    op=int(input("Enter the operation you wanna: "))

    if(op==1):
        a=int(input("Enter the number:- "))
        b=int(input("Enter the number:- "))
        print(add(a,b))

    elif(op==2):
        a=int(input("Enter the number:- "))
        b=int(input("Enter the number:- "))
        print(sub(a,b))
    elif(op==3):
        a=int(input("Enter the number:- "))
        b=int(input("Enter the number:- "))
        print(mul(a,b))
    elif(op==4):
        a=int(input("Enter the number:- "))
        b=int(input("Enter the number:- "))
        print(div(a,b))
    elif(op==5):
        root()

    elif(op==6):
        fact()

    else:
        print("Enter the valid input")

except ZeroDivisionError:
    print("Cannot divide the number by zero")
    

except ValueError:
    print("Cannot get the correct value")

except RuntimeError:
    print("SOmething happened in the program,check it ")


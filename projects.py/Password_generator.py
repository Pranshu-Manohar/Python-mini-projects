import random
a=[]
y=[]
for i in range(10):
    a.append(i)

b=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
b1=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
c=['@','$','!','*','(',')','^','+','&','-','_']
d=a+b+b1+c

user=int(input("Enter the number of char you wnat in password:- "))

for i in range(user):
    x=random.choice(d)
    y.append(x)
    # for i in range(len(y)):
    #     z=y.index( i in y)
    #     print(z)
        


passw="".join(str(item) for item in y)



print("\n")

print(f"Your pass word is --> \"{ passw}\"")
print("\n")

point=0

'''POINTS DISTRIBUTION TABLE'''

for iteam in a:
    if iteam in y:
        point=point+1
    if(point!=0):
        point=1

        

for iteam in b:
    if iteam in y:
        point=point+1

    if(point>1):
        point=2

for iteam in b1:
    if iteam in y:
        point=point+1

    if(point>2):
        point=3

for iteam in c:
    if iteam in y:
        point=point+1
   
'''CONDITION TABLE '''

if(point==2):
    print("Password frequency- \"WEAK\"")

elif (point==3):
    print("Password frequency-\"MEDIUM\"")

# elif (point==4):
#     print("Password Frequency-\"STRONG\"")

elif(point==4):
    print("Password Frequency-\"SUPER STRONG\"")

else:
    print("super duper strong")
          


# for ct in d:
#     if ct in y:
#         print("password is strong ")
# yahi tareeka use kr or sabko seperate kro 
'''
if (int in x && char in x):
    print("your password is  seems to be strong )

this is so amazing that no one is going to match . i believe i can do any thing alone too . i just need a potential 
boooster to run and active myself.










'''

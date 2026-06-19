a=[]

for i in range(100):
    ipt=input("Enter the tasks :- ")
    if ipt=="":
        break
    else:
        a.append(ipt)

for elements in a:
    print(f"* {elements}")
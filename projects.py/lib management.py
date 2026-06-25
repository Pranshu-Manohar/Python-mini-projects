#create a class with a bank aaccount with a pvt attribute bal implemetn depo, withraw ,func


# class bankacc:
#     bal=None
#     def __init__(self):
#         self.__bal=int(input("Enter the balance: "))
#         print("Press 1 for depo")
#         print("Press 2 for withdrawal")
#         print("Press 3 for checkbal")
#         __choice=int(input("Enter your choice: "))

#         if (__choice==1):
#             __depo=int(input("Enetr the depo amount: "))
#             self.__bal=self.__bal+__depo
#             print("Your new bal is",self.__bal)
        
#         elif(__choice==2):
#             __withamt=int(input("Enter the withamt: "))
#             if(self.__bal>__withamt):
#                 self.__bal=self.__bal-__withamt
#                 print("your new bal is ",self.__bal)
#             else:
#                 print("Amount is too high")
#         elif(__choice==3):
#             print("Your new bal is ",self.__bal)


# obj=bankacc()

# print(obj.__bal) # this error is causing because of the private class


#create a class stu with pvt marks update the marks +5 , s.name,rolln,course ,marks

# class stu:
#     s_name=None
#     s_roll=None
#     course=None
#     __s1=0
#     __s2=0
#     __s3=0
#     __s4=0

#     def __init__(self):
#         self.s_name=input("Enetr the s name : ")
#         self.s_roll=int(input("Enetr the s roll : "))
#         self.course=input("Enetr the s course : ")
#         self.__s1=int(input("Enetr the s s1 : "))
#         self.__s2=int(input("Enetr the s s2 : "))
#         self.__s3=int(input("Enetr the s s3 : "))
#         self._s4=int(input("Enetr the s s4 : "))

#     def update(self):
#            self.__s1=self.__s1+5
#            self.__s2=self.__s2+5
#            self.__s3=self.__s3+5
#            self.__s4=self.__s4+5
#            print("S1:",self.__s1)
#            print("S2:",self.__s2)
#            print("S3:",self.__s3)
#            print("S4:",self.__s4)

# student1=stu()

# student1.update()

# print(student1.__s1) # this is because of the pvt method that uses the two underscores


#create a classes circle ,rect and tri find the area of the all the classes with the all the method named area 

# class circle:
#     def area(self,pi,r):
#         print("area of circle:",pi*(r**2))

# class rect(circle):
#     def area(self, l, b):
#         print(l*b)

# class tri(circle):
#     def area(self, b,h):
#         print(1/2*b*h)


# ac=circle()
# ac.area(3.14,4)
# at=tri()
# at.area(2,2)
# ar=rect()
# ar.area(3,4)

#lib mang system using the oops properties
"""
class book:
    def __init__(self):
          
        self.name=input("Enter the book name :")
        self.__author=input("Enter the author name :")

class booktype:
         def __init__(self):
              self.bt=input("Enter the book type: ")


class lib(book,booktype):
    def __init__(self):
         book.__init__(self)
         booktype.__init__(self)
         self.b_id=int(input('Enter the book id: '))
    def __str__(self):
            return (f"Book name: {self.name}\nAuthor name:{self._book__author}\nBooktype: {self.bt}")

b1=lib()

print(b1)


"""
# a="hello"

# it=iter(a)
# for i in range(0,len(a)):
#     print(next(it))

# print(next(it))

#when we have already built data then we use the iter
# when we have to build the data we use yield (generator)
# def sq(n):
#     for i in range(1,n+1):
#         yield i*i

# for i in sq(8):
#     print(i)


#create an iter class named even number that generates even no

# class itt:
#     def __init__(self):
#         self.no=int(input("Enter the number till you need: "))

#         self.l=[]
#         for i in range(2,self.no+1):
#             if(i%2==0):
#                 self.l.append(i)

           

#         self.a=iter(self.l)
#         for i in range(0,len(self.l)):
#                  print(next(self.a))


# it=itt()


#using the iter use the odd no square 

class itt:
    def __init__(self):
        self.no=int(input("Enter the number till you need: "))

        self.l=[]
        for i in range(self.no+1):
            if(i%2!=0):
                self.l.append(i)

           

        self.a=iter(self.l)
        for i in range(0,len(self.l)):
                 print((next(self.a))**2)


it=itt()

print(type(it))


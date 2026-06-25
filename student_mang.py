class stu:
    s_name=None
    s_roll=None
    course=None
    __s1=0
    __s2=0
    __s3=0
    __s4=0

    def __init__(self):
        self.s_name=input("Enetr the s name : ")
        self.s_roll=int(input("Enetr the s roll : "))
        self.course=input("Enetr the s course : ")
        self.__s1=int(input("Enetr the s s1 : "))
        self.__s2=int(input("Enetr the s s2 : "))
        self.__s3=int(input("Enetr the s s3 : "))
        self._s4=int(input("Enetr the s s4 : "))

    def update(self):
           self.__s1=self.__s1+5
           self.__s2=self.__s2+5
           self.__s3=self.__s3+5
           self.__s4=self.__s4+5
           print("S1:",self.__s1)
           print("S2:",self.__s2)
           print("S3:",self.__s3)
           print("S4:",self.__s4)

student1=stu()

student1.update()

# print(student1.__s1) # this is because of the pvt method that uses the two underscores

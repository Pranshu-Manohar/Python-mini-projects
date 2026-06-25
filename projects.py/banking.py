
class bankacc:
    bal=None
    def __init__(self):
        self.__bal=int(input("Enter the balance: "))
        print("Press 1 for depo")
        print("Press 2 for withdrawal")
        print("Press 3 for checkbal")
        __choice=int(input("Enter your choice: "))

        if (__choice==1):
            __depo=int(input("Enetr the depo amount: "))
            self.__bal=self.__bal+__depo
            print("Your new bal is",self.__bal)
        
        elif(__choice==2):
            __withamt=int(input("Enter the withamt: "))
            if(self.__bal>__withamt):
                self.__bal=self.__bal-__withamt
                print("your new bal is ",self.__bal)
            else:
                print("Amount is too high")
        elif(__choice==3):
            print("Your new bal is ",self.__bal)


obj=bankacc()

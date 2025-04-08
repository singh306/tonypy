class Account:
    bank="union"
    def __init__(self,accname,acc,bal):
        self.accname=accname
        self.acc=acc
        self.bal=bal
    def login (self,pin):
        if pin == 0000:
            print("wellcome",self.accname)
            b=int(input("enter your choice \n 1.debit \n2.credit \n3.balance \n4.account detals \n:"))
            if b==1:
                print(self.debit(float(input("enter amount"))))
            elif b ==2 :
                print(self.credit(float(input("enter amount "))))
            elif b==3:
                    print(self.getbal())
            elif b==4:
                    print(self.__init__())    
        else :
            print("worng pin")
            exit
    def debit(self,miamount):
        self.bal -= miamount
        print("the debited amount:",miamount)
        print(self.getbal())

    def credit(self,plamount):
        self.bal += plamount
        print("the credit amount:",plamount)
        print("total bal:",self.getbal())

    def getbal(self):
        return self.bal
    
acc1 = Account("tony",123456,25000)
a =int(input("enter a pin "))
acc1.login(a)
print("end")
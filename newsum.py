class Interest:
    def __init__(self,name,amount,rate,time):
        self.name = name
        self.amount=amount
        self.rate=rate
        self.time=time

    def print(self):
        print(self.name)
        print(self.amount)
        print(self.rate)
        print(self.time)

int = Interest(input("name:"),float(input("amount:")),float(input("rate:")),float(input("time:")))
int.print()
rat=int.amount*int.rate*int.time/100
sum=rat+int.amount
print("interest amount to pay :",rat)
print("the loan amount:",int.amount)
print("total amount:",sum)
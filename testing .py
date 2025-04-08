class Detals:
    def accept(self):
        self.name = input("enter your name")
        self.idnum= input("enter your id")
        self.address= input("enter your address")
        self.dob= input("enter your DOB")
        self.num= input("enter your num")

    def print(self):
        print("employ detals:-","emply name:",self.name,"emply id:",self.idnum)
        print("employ address:",self.address,"employ dob:",self.dob,"employ numder:",self.num)
d1 = Detals()
# name = input("enter your name")
d1.accept()
d1.print()
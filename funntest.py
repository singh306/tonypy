# program for bank 


def show_balance(balance): #for showing account balance 
    print("__________________") #for macking program more attractive
    print(f"your balance is Rs{balance:.2f}")

def deposit(): # for deposit amount in your account 
    print("__________________")
    amount = float(input("enter an amount to be deposited :"))
    print("teansaction successfull")

    if amount < 0 :
        print("_________________________")
        print("That amount is not valid ")
        print("transaction faild")
        return 0
    else:
        return amount

def withdraw(balance): # for withdraw on account 
    print("___________________")
    amount = float(input("enter amount to be withdraw:"))
    print("transaction successful")

    if amount > balance:
        print("_____________________________")
        print("insufficient funds in account")
        print("transaction faild")
        return 0
    elif amount < 0:
        print("_____________________________")
        print("amount must be more then zero")
        print("transaction faild")
        return 0
    else:
        return amount

def main():
    balance =0
    is_running = True

    while is_running:
        print("______________")
        print("BANK SYSTEM")
        print("______________")
        print("1.show Balance")
        print("______________")
        print("2.Deposit amount")
        print("______________")
        print("3.Withdraw amount")
        print("______________")
        print("4.Exit Bank system")
        print("_______________")

        choice = input("Eter your work (1to 4):")

        if choice == "1":
            show_balance(balance)
        elif choice == "2":
            balance+= deposit()
        elif choice == "3":
            balance -= withdraw(balance)
        elif choice == "4":
            is_running = False
        else:
            print("that is not a valid choise")

    print("Thank you ")

if __name__ == "__main__":
    main()
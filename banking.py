class Bankaccount:

    def __init__(self,name,balance=0):
        self.name = name
        self.balance = balance
       
    def deposite(self,amount):
        self.balance += amount
        print(f"successfully deposited Rs.{amount}/- \nTotal balance Rs.{self.balance}")

    def widthdrawl(self,amount):
        if (amount>self.balance):
            print("Insuffecient balance")
        else:
            self.balance -= amount
            print(f"successfully withdrawl Rs.{amount}/- \nTotal balance Rs.{self.balance}")

    def checkBalace(self):
        print(f"Total Account Balance Rs.{float(self.balance)}/-")

    
def main():

    account={}
    active= True

    while active:
        print("\n*** Welcome to Online ATM ***\n")

        print("1.Create Account")
        print("2.Log In")
        print("3.Exit")

        choice = input("\nChoose One Number :- ")

        if (choice== "1"):
            name = input("\nEnter your name : ")
            if name in account:
                print("\nAlready exist. login\n")
            else:
                account[name] = Bankaccount(name)
                print("\nAccount created successfully...\n")

        elif(choice=="2"):
            name = input("Enter your name : ")
            if name in account:
                print(f"\nWelcome back {name}\n")
                dep = account[name]
                while True:
                    print("1.deposit")
                    print("2.widthdrawl")
                    print("3.balance enqurie")
                    print("4.logout")

                    userchoice= int(input("\nchoose option : "))
                    if userchoice==1:
                        damount = int(input("Enter amount : "))
                        dep.deposite(damount)
                    elif userchoice==2:
                        wamount = int(input("Enter amount : "))
                        dep.widthdrawl(wamount)
                    elif userchoice==3:
                        dep.checkBalace()
                    elif userchoice==4:
                        print("\nloggout successfully\n")
                        break
                    else:
                        print("\ninvalid entry\n")
            else:
                print("Sorry, no name registered")
        
        elif(choice=="3"):
            print("\nThankyou for banking with us...")
            active=False

        else:
            print("\ninvalid entry\n")

if __name__ == "__main__" :
    main()






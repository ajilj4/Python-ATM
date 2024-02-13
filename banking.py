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

        choice = int(input("\nChoose One Number :- "))

        if (choice== 1):
            name = input("Enter your name : ")
            if name in account:
                print("Already exist. login")
            else:
                account[name] = Bankaccount(name)
                print("Account created successfully...")
        
        elif(choice==3):
            print("\nThankyou for banking with us...")
            active=False

if __name__ == "__main__" :
    main()






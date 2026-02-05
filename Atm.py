'''balance = 100000# Initial balance
correct_pin=1234
print("insert the card")
print("welcome Lakshmi")
attempts=3

# PIN Verification
while attempts > 0:
    pin = int(input("Enter your ATM PIN: "))

    if pin==correct_pin:
        print("PIN verified successfully!\n")
        break
    else:
        attempts-=1
        print(f"Wrong PIN! Attempts left: {attempts}")

if attempts==0:
    print("ATM card blocked. Please contact your bank.")
else:
    while True:
        print("\n----- ATM MENU -----")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice=int(input("Enter your choice (1-4): "))

        if choice==1:
            print(f"Your balance is: ₹{balance}")

        elif choice==2:
            amount=int(input("Enter deposit amount: ₹"))
            if amount>0:
                balance+=amount
                print("Amount deposited successfully.")
            else:
                print("Invalid amount!")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: ₹"))
            if amount > 0 and amount <= balance:
                balance -= amount
                print("Please collect your cash.")
            else:
                print("Insufficient balance or invalid amount!")

        elif choice == 4:
            print("Thank you for using ATM. Visit again")
            break

        else:
            print("Invalid choice! Try again.")'''

task:
a=2
b=4
while True:
    def calculate(a,b):
        print("1.the sum is",a+b)
        print("2.the diff is",a-b)
        print("3.the product is",a*b)
    calculate(2,4)
    choose=int(input("enter the choice:"))
    if choose==1:
        print(a+b)
    elif choose==2:
        print(a-b)
    elif choose==3:
        print(a*b)
    else:
        print("not print")

Method 2:

def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a=int(input("a value"))
    b=int(input("b value"))
    option=int(input(choose the options
                             1.add
                             2.sub
                             3.mul))
    if option==1:
        add()
    elif option==2:
        sub()
    elif option==3:
        mul()

Task 2:
while True:
    a=int(input("enter the ammount:"))
    b=int(input("how many member:"))
    c=a//b
print("per head is {}".format(c))

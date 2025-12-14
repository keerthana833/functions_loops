#Ask user for pin 
#Ask what they want
#Then exit


balance=4000
pin=2345

user_pin=int(input("Enter the pin: "))

if user_pin==pin:
    while True:
        print("\nWelcome to ATM")
        print("1.Check Balance")
        print("2.Deposit Money")
        print("3.Withdraw Money")
        print("4.Exit")

        choice=int(input("Enter your choice (1-4): "))

        if choice==1:
            print(f"Your current balance: {balance}")
        elif choice==2:
            deposit=int(input("Enter amount to deposit: "))
            balance+=deposit
            print(f"Deposit successful.New balance:{balance}")
        elif choice==3:
            Withdraw=int(input("Enter amount to withdraw: "))
            if Withdraw<=balance:
                balance-=Withdraw
                print(f"Withdrawl successful.New balance: {balance}")
            else:
                print("Insufficient balance")
        elif choice==4:
            print("Thankyou for using ATM.Goodbye!")
            break
        else:
            print("Invalid choice!please try again.")

else:
    print("Incorrect PIN.Access Denied")
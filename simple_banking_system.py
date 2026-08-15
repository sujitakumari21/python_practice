#SIMPLE_BANKING_SYSTM


balance = 0
transaction_history = []
def deposit():
    global balance
    amount= float(input("Enter amount is deposit :"))
    if amount >0:
        balance += amount 
        transaction_history.append(f"Deposited ${amount:.2f}")
        print("Deposit successfull")
    else:
        print("Invalid amount")

def withdraw():
    global balance
    amount = float(input("Enter amount to Withdraw : $"))

    if amount <= 0:
        print("Invalid amount !")
    elif amount > balance:
        print ("Insufficient Balance !")
    else:
        balance -= amount
        transaction_history.append(f"Withdraw ${amount:.2f}")
        print("Withdrawal successfull !")

def show_transation():
        print(f"\ncurrent Balance : ${balance :.2f}")

    
def show_transaction():
    if len(transaction_history)==0:
            print("\nNo transation available.")
    else:
            print("\n ----Transaction History----")

            for transation in transaction_history:
                print("transaction")

    #Main program
while True:
        print("\n========Simple Banking Systen")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check")
        print("4.Transaction History")

        choice = input("Enter your choice (1-5):")
        if choice == "1":
         deposit()
        elif choice == "2":
             withdraw()
        
        elif choice == "4":
             show_transaction()
        elif choice =="5":
            print("\nThank you for using our Bank System!")
            break

        else:
             print("Invalid choice please try again!")

# now that we have enclose in the main functions, we need add the variable in the parameters of the function.

def show_balance(balance):
    # print(f"Your balance is ${balance}") 
    print(f"Your balance is ${balance:.2f}") # we add :.2f to add two decimals

def deposit():
    amount = float(input("Enter an amount to be deposited: ")) # we will typ cast it to a number floating
    if amount < 0:
        print("That's not a valid amount.")
        return 0 #let's just return 0 if there is a problem with the value
    else:
        return amount 
    
def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficients funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

# we can now enclose all of this code within a main function
def main():
    balance = 0
    is_running = True #we create a boolean so that we can exit the program when needed. 

    while is_running:
        print("Banking programm")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1': # because actually input is a string data
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False # si choice == 4 we want to exit so we need to exit the while loop and we can do that by making is_running = false
        else:
            print("That is not a valid choice")
        
    print("Thank you! Have a nice day!")
    
if __name__ == "__main__":
    main()

def show_balance(balance):
    print(f"Your actual balance is ${balance:.2f}.") 

def deposit(): 
    user_input = input("Enter an amount to be deposited (or type 'quit' to return): ").strip()
    if user_input.lower() == "quit":
        print("Returning to main menu.")
        return 0
    try:
        amount = float(user_input) 
        if amount <= 0:
            print("That's not a valid amount.")
            return 0 
        else:
            return amount 
    except ValueError:
        print("Invalid input.")    
        return deposit()
        
    
def withdraw(balance):
    user_input = input("Enter amount to be withdrawn (or type 'quit' to return): ").strip()
    if user_input.lower() == "quit":
        print("Returning to main menu.")
        return 0
    try:
        amount = float(user_input)
        if amount > balance:
            print("Insufficients funds.")
            return 0
        elif amount < 0:
            print("Amount must be greater than 0.")
            return 0
        else:
            return amount
    except ValueError:
        print("Invalid input.")
        return withdraw(balance)

def add_delimitation(type_delimitation = "-", length = 30):
    for i in range(length):
        print(type_delimitation, end="")
    print()  # pour ajouter un saut de ligne après la ligne de délimitation

    
def main():
    add_delimitation()
    print(" Welcome to Your Banking App")
    add_delimitation()

    balance = 0
    is_running = True 

    while is_running:
        print("Banking Menu")
        print("\t1️. Show Balance")
        print("\t2️. Deposit")
        print("\t3️. Withdraw")
        print("\t4️. Exit")
        add_delimitation()
        choice = input("Enter your choice (1-4): ").strip()
        
        print()  # Ligne vide pour l'aération

        if choice == '1': # because actually input is a string data
            add_delimitation()
            print("***** Section Balance *****") 
            show_balance(balance)
            add_delimitation()

        elif choice == '2':
            add_delimitation()
            print("***** Section Deposit *****") 
            show_balance(balance)
            balance += deposit()
            show_balance(balance)
            add_delimitation()
        elif choice == '3':
            add_delimitation()
            print("***** Section Withdraw *****") 
            show_balance(balance)
            balance -= withdraw(balance)
            show_balance(balance)
            add_delimitation()
        elif choice == '4':
            is_running = False 
            print("Exiting... Thank you for banking with us!")
            add_delimitation()
        else:
            add_delimitation()
            print("That is not a valid choice. Please enter 1-4.")
            add_delimitation()
        
    print("Thank you! Have a nice day!")
    
if __name__ == "__main__":
    main()
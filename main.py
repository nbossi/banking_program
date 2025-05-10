from colorama import init, Fore, Style

# Initialise colorama (utile sur Windows)
init(autoreset=True)

# Visuel
def print_header(title):
    print(Style.BRIGHT + Fore.CYAN + f" MENU {title.upper()} ".center(40, "*"))

def print_menu():
    menu_options = {
        "1": "Show Balance",
        "2": "Deposit",
        "3": "Withdraw",
        "4": "View Transactions",
        "5": "Exit"
    }
    print("\n" + Style.BRIGHT + Fore.CYAN + " MAIN MENU ".center(40, "="))
    for key, value in menu_options.items():
        print(Style.BRIGHT + Fore.CYAN + f"\t{key}. {value}" )
    print(Style.BRIGHT + Fore.CYAN +"="*40)

def add_delimitation(type_delimitation = "-", length = 30):
    print(Fore.CYAN + type_delimitation*length)
    # for i in range(length):
    #     print(type_delimitation, end="")
    # print()  # pour ajouter un saut de ligne après la ligne de délimitation

# Transactions basiques
def show_balance(balance):
    print(Fore.GREEN +f"Your actual balance is ${balance:.2f}.") 

def get_amount(prompt, max_amount=None):
    is_amount = True
    while is_amount:
        print(Fore.CYAN + prompt, end='')
        user_input = input(Fore.MAGENTA).strip()
        if user_input.lower() == "quit":
            is_amount = False
            return 0
        try:
            amount = float(user_input)
            if amount < 0:
                print(Fore.RED + "Amount must be positive")
                continue
            elif (max_amount or max_amount == 0) and amount > max_amount:
                print(Fore.RED + f"Amount exceeds available ${max_amount:.2f}")
                continue
            return amount
        except ValueError:
            print(Fore.RED + "Invalid amount. Please enter a number")
            
def deposit(): 
    return get_amount("Enter an amount to be deposited (or type 'quit' to return): ")
    
def withdraw(balance):
    return get_amount("Enter amount to be withdrawn (or type 'quit' to return): ", balance)
    
def main():
    add_delimitation('_', 40)
    print("\n" +Fore.CYAN + "Welcome to Your Banking App".center(40, " "))
    add_delimitation('_', 40)

    balance = 0
    is_running = True 

    while is_running:
        print_menu()
        print(Fore.CYAN + "Enter your choice (1-5): ", end='')
        choice = input(Fore.MAGENTA).strip()
        
        print()  # Ligne vide pour l'aération

        if choice == '1': # because actually input is a string data
            print_header("balance")
            show_balance(balance)

        elif choice == '2':
            print_header("DEPOSIT")
            show_balance(balance)
            balance += deposit()
            show_balance(balance)
        elif choice == '3':
            print_header("WITHDRAW")
            show_balance(balance)
            balance -= withdraw(balance)
            show_balance(balance)
        elif choice == '4':
            print_header("TRANSACTIONS")
            print("TODO ... sorry")
        elif choice == '5':
            is_running = False 
            print(Fore.MAGENTA + "Exiting... Thank you for banking with us!")
        else:
            print(Fore.RED + "That is not a valid choice. Please enter 1-5.")
            
    add_delimitation('_', 40)
    print(Fore.MAGENTA + "\nThank you! Have a nice day!")
    add_delimitation('_', 40)

if __name__ == "__main__":
    main()
# simple banking program
# step 1 : when creating a project, divide that project into smaller sections then handle them one at a time 
#   so we'll do that by declaring all the functions we'll need first with the banking program

# 1. Show Balance : we'll need to show a user their balance
# 2. Deposit : we'll need to make a deposit
# 3. Withdraw : we'll need to make a withdraw

def show_balance():
    pass #place holder

def deposit():
    pass

def withdrawal():
    pass

# def main():
#     return 0

#we will handle the main function at the end just to contain everything
#so we need these 3 functions (show_balance, deposit, withdrawal) + the main function
#now we need to think about the variables we need :
balance = 0
is_running = True #we create a boolean so that we can exit the program when needed. 

#so with the majority of our code we will place it within a while loop 
#while is_running == True : # but is_running is already a boolean so we can just put 
while is_running:
    #if is_running becomes false we exit the code
    #in the loop we will print some sort of welcome message
    print("Banking programm")
    print("1. Show Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    # we will set a choice variable to equal some user input so that they chose between show balance, deposit, withdraw or exit.
    choice = input("Enter your choice (1-4): ")
    # we will ad a few if and else if statement
    if choice == '1': # because actually input is a string data
        show_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdrawal()
    elif choice == '4':
       is_running = False # si choice == 4 we want to exit so we need to exit the while loop and we can do that by making is_running = false
    else:
        print("That is not a valid choice")
# now let see what we're working with currently to test everything 
# we haven't written anything within these functions yet show balance, deposit or withdraw so we can type one to four 
    

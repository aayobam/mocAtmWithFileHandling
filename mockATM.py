import random
from datetime import datetime as dt
import database
from validation import account_number_validation
from getpass import getpass
from auth_session.session import (delete_login_session, create_login_session)


date_time= dt.now()


        
 
#customers makes complaints
def complaint():
    complaint = input("What issue will you like to report?: ")
    print("Your Complaint goes thus: ", complaint)
    print("Thank you for contacting us.")
    response = input("Would you like to perform another operation? type y/yes or n/no: ".lower())
    if response == "yes" or response == "y":
        login()
    elif response == "no" or response == 'n':
        print("Thanks for banking with us")
        exit()

  
#funds withdrawal function
def withdrawal():
    withdrawal = int(input("How much would you like to withdraw?: "))
    database.withdraw_funds(accountNumberFromUser, withdrawal)
    response = input("Would you like to perform another operation? type y/yes or n/no: \n".casefold())
    if response == "yes" or response == "y":
        login()
    elif response == "no" or response == 'n':
        print("Thanks for banking with us, you may take your card")
        exit()
        

# funds deposit function   
def deposit():
    deposit = int(input("How much would you like to deposit?: "))
    database.deposit_funds(accountNumberFromUser, deposit)
    response = input("Would you like to perform another operation? type y/yes or n/no: ".lower())
    if response == "yes" or response == "y":
        login()
    elif response == "no" or response == 'n':
        print("Thanks for banking with us, you may take your card")
        exit()
        

   
def current_balance():
    database.get_current_balance(accountNumberFromUser)

   
#selected operations function 
def bankOperation(user):
    print("Welcome", user[0].upper(), user[1].upper(), "you are logged in on :", date_time, "\n")
    print("The below are the operations you can perform")

    print("[1] - CASH DEPOSIT.\n[2] - CASH WITHDRAWAL.\n[3] - CHECK BALANCE.\n[4] - COMPLAINTS.\n[5] - LOGOUT.\n[6] - EXIT.\n")
    selectedOption = int(input("Which operation would you like to perform ?: "))
    
    if selectedOption == 1:
        deposit()
        
    elif selectedOption == 2:
        withdrawal()
        
    elif selectedOption == 3:
        current_balance()
        
    elif selectedOption == 4:
        complaint()
        
    elif selectedOption == 5:
        delete_login_session(accountNumberFromUser)
        logout()
        
    elif selectedOption == 6:
        print("Please take your card and thanks for banking with us.")
        delete_login_session(accountNumberFromUser)
        exit()
    else:
        print("invalid option selected please try again")
        bankOperation()


accountNumberFromUser = "" # declared this so the session.delete_login_session(accountNumberFromUser) could access its current value which is the account number
# User Login
def login():
    print("*** Login into your Account ***")
    global accountNumberFromUser
    accountNumberFromUser = int(input("Enter your Account Number: "))
    
    is_valid_account_number = account_number_validation(accountNumberFromUser)
    
    if is_valid_account_number:
        password = getpass("Enter your password: ")
        user = database.authenticated_user(accountNumberFromUser, password)
        if user:
            create_login_session(accountNumberFromUser)
            bankOperation(user)
        else:
            print("Invalid account or Password")
    else:
        print("Account Number Invalid: check that you have up to number is 10 digits and only integers")
        login()


# log out of current session   
def logout():
    login()

    
#Account number generating function  
def generateAccountNumber():
    return random.randrange(1111111111,9999999999)

    
# New Users registeration function. 
def register():
    print("******* Create an Account *******\n")
    email = input("Enter your email address: ")
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    password = getpass("Enter your password: ")
    
    account_number = generateAccountNumber()
    
    
    is_user_created = database.create_record(account_number, first_name, last_name, email, password)
    
    if is_user_created:
        print("Your Account Has Been Created\n")
        print("==== ====== ====== ===== =====")
        print("Your account number is: ", account_number)
        print("Make sure you keep it safe.")
        print("==== ====== ====== ===== =====\n")
        login()
    else:
        print('Something went wrong, Please try again')
        register()

 
# Start of the applications  function
def init():
    print("Welcome to bankPHP")
    try:
        haveAccount = int(input("Do you have an account with us: 1 for (Yes), 2 (No)?: "))
        if haveAccount == 1:
            login()  
            
        elif haveAccount == 2:
            register() 
        else:
            print("invalid selection\n")
            init()
    except ValueError:
        print("Digit value expected\n")
        init()
init()
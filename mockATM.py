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
    try:
        response = input("Would you like to perform another operation? type y/yes or n/no: ".lower())
        if response == "yes" or response == "y":
            login()
            
        elif response == "no" or response == 'n':
            print("Thanks for banking with us")
            exit()
            
        else:
            print("Invalid response supplied")
            bankOperation()
    except TypeError:
        print("character value Expected")
    finally:
        bankOperation()


# Check available balance
def current_balance(user):
    current_balance = user[4]
    print(f"Hello {user[0].upper()} {user[1].upper()} your available balance is: {current_balance}")
    response = input("Would you like to perform another operation? type y/yes or n/no: ".casefold())
    try:
        if response == "yes" or response == "y":
            bankOperation(user)  
            
        elif response == "no" or response == 'n':
            print("Thanks for banking with us, you may take your card")
            delete_login_session(accountNumberFromUser)
            exit()
            
        else:
            print("Invalid response suplied, please try again")
            bankOperation(user)    
    except TypeError:
        print("Character value expected")
    finally:
        bankOperation(user)
    

# Withdraws funds from current user's account.
def withdrawal(user):
    current_balance = user[4]
    try:
        withdrawal = float(input("How much would you like to withdraw?: "))
        if current_balance == 0 or withdrawal > current_balance:
            print("Insufficient funds")
            response = input("Would you like to make a deposit ? Type y for YES or n for NO: ".lower())
            if response == "y":
                deposit(user)
            elif response == "no":
                print("Thanks for banking with us")
                bankOperation(user)
        elif withdrawal <= 0:
            print(f"You cannot withdraw {withdrawal} from your account, try a higher value")
            withdrawal()
            
        else:
            current_balance = float(current_balance) - withdrawal
            print(f"you withdrew {withdrawal} and your available balance is : {current_balance}")
            user[4] = current_balance
    except ValueError:
        print("Invalid Input supplied")
        deposit(user)
        
    except TypeError:
        print("Digit value expected")
        deposit(user)
    finally:
        updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])
        
        user_db_path = "data/user_record/"
        file = open(user_db_path + str(accountNumberFromUser) + ".txt", "w")
        file.write(updated_user)
        file.close()
        try:
            response = input("Would you like to perform another operation? type y/yes or n/no: ".casefold())
            if response == "yes" or response == "y":
                bankOperation(user)
                
            elif response == "no" or response == 'n':
                print("Thanks for banking with us, you may take your card")
                delete_login_session(accountNumberFromUser)
                exit()
                
            else:
                print("Invalid value supplied, please try again")
                bankOperation(user)     
        except TypeError:
            print("Digit input expected, please try again")  
        finally:
            bankOperation(user)


# Deposit funds to current user account   
def deposit(user):
    current_balance = user[4]
    try:
        deposit = float(input("How much would you like to deposit?: "))
        if deposit <= 0:
            print(f"You cannot deposit {deposit} into your account, try a higher value")
            deposit(user)
        else:
            current_balance = float(current_balance) + deposit
            print(f"You deposited {deposit} and your available balance is: {current_balance}")
            user[4] = current_balance
    except ValueError:
        print("Invalid Input supplied")
        deposit(user)
    except TypeError:
        print("Digit value expected")
        deposit(user)
    finally:
        updated_user = user[0] + "," + user[1] + "," + user[2] + "," + user[3] + "," + str(user[4])
        user_db_path = "data/user_record/"
        file = open(user_db_path + str(accountNumberFromUser) + ".txt", "w")
        file.write(updated_user)
        file.close()
        
        try:
            response = input("Would you like to perform another operation? type y/yes or n/no: ".lower())
            if response == "yes" or response == "y":
                bankOperation(user)
                
            elif response == "no" or response == 'n':
                print("Thanks for banking with us, you may take your card")
                #delete_login_session(accountNumberFromUser)
                exit()
                
            else:
                print("Invalid value supplied, please try again")
                bankOperation(user)  
        except TypeError:
            print("Digit input expected, please try again")
        finally:
            bankOperation(user)
        
 
#selected operations function 
def bankOperation(user):
    print("Welcome", user[0].upper(), user[1].upper(), "you are logged in on :", date_time, "\n")
    print("The below are the operations you can perform")

    print("[1] - CASH DEPOSIT.\n[2] - CASH WITHDRAWAL.\n[3] - CHECK BALANCE.\n[4] - COMPLAINTS.\n[5] - LOGOUT.\n[6] - EXIT.\n")
    try:
        selectedOption = int(input("Which operation would you like to perform ?: "))
        
        if selectedOption == 1:
            deposit(user)
            
        elif selectedOption == 2:
            withdrawal(user)
            
        elif selectedOption == 3:
            current_balance(user)
            
        elif selectedOption == 4:
            complaint()
            
        elif selectedOption == 5:
            delete_login_session(accountNumberFromUser)
            logout()
            
        elif selectedOption == 6:
            print("Please take your card and thanks for banking with us.")
            exit()
            delete_login_session(accountNumberFromUser)
        else:
            print("invalid option selected please try again")
            bankOperation(user)
    except ValueError:
        print("Digit is expected")
    finally:
        bankOperation(user)


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

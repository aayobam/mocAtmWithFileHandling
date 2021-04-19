# This module creates record, reads record, edits record and  deletes record.
import os
from validation import account_number_validation


user_db_path = "data/user_record/"
currentBalance = ""
ledger_balance = ""

    
# Create a file, name of file would be account_number.txt, add the user details to file. 
def create_record(account_number, first_name, last_name, email, password):
    user_data = first_name + "," + last_name + "," + email + "," + password + "," + str(0)
    
    
    if does_account_number_exist(account_number):
        return False
        
    if does_email_exist(email):
        print("User already exists")
        return False
    
    completion_state = False
    try:
        file = open(user_db_path + str(account_number) + ".txt", "x")
            
    except FileExistsError:
        
        does_file_contains_data = read_record(user_db_path + str(account_number) + ".txt")
        if not does_file_contains_data:
            delete_record(account_number)
    else:
        file.write(user_data)
        completion_state = True   
    finally:
        file.close()
        return completion_state


#  find user with account nummber, fetch content of the file and return it. 
def read_record(account_number):
    
    is_valid_account_number = account_number_validation(account_number)
    
    try:
        if is_valid_account_number:
            file = open(user_db_path + str(account_number) + ".txt", "r")
            
        else:
            file = open(user_db_path + account_number, "r")
        
    except FileNotFoundError:
        print("user not found")
        
    except FileExistsError:
        print("User doesn't exist")
        
    except TypeError:
        print("Invalid account number format")
        
    else:
        return file.read()
    return False


# find user with account nummber, feth content of the file, update the content of the file and save the file.
def update_record(account_number):
    pass


# find user with account nummber, delete the user record and save the file.   
def delete_record(account_number):
    is_delete_successful = False
    
    if os.path.exists(user_db_path + str(account_number) + ".txt"):
        try:
            os.remove(user_db_path + str(account_number) + ".txt")
            is_delete_successful = True
            
        except FileNotFoundError:
            print("User not found")
            
        finally:
            return is_delete_successful

        
# find user in the record folder. 
def does_email_exist(email):

    all_users = os.listdir(user_db_path)
    for user in all_users:
        user_list = str.split(read_record(user), ',')
        if email in user_list:
            return True
    return False

      
# checks if account number exist
def does_account_number_exist(account_number):
    all_users = os.listdir(user_db_path)
    for user in all_users:
        if user == str(account_number) + ".txt":
           return True
    return False


# checks if account number is in file and password is valid and correct.
def authenticated_user(account_number, password):
    if does_account_number_exist(account_number):
        user = str.split(read_record(account_number), ',')
        print(user)
        if password == user[3]:
            return user
    return False

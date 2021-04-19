import os
from datetime import datetime as dt
user_session_path = "auth_session/"


#create login session immediately a user logs in
def create_login_session(account_number):
    file = open(user_session_path + str(account_number) +"_session" + ".txt", 'x')
    date_time = dt.now()
    logged_in_date = date_time.strftime("%d-%b-%Y")
    logged_in_time = date_time.strftime("%H:%M:%S.%p")
    login_details = str(account_number) + " logged on " +  str(logged_in_date + " at " + str(logged_in_time))
    file.write(login_details)
    print("Session Successfully Created")
    file.close()



def delete_login_session(account_number):
    if os.path.exists(user_session_path + str(account_number) + "_session" + ".txt"):
        try:
            os.remove(user_session_path + str(account_number)+ "_session" + ".txt")
            is_delete_successful = True
            print("Session successfully deleted")
            
        except FileNotFoundError:
            print("User session not found")
            
        finally:
            return is_delete_successful
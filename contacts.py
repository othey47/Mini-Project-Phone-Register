# => Mini project: Phone Register.

# 1. Storage data in contacs list.
contacts = [    
    {"Name" : "Amal"    , "Phone" : 1111111111},
    {"Name" : "Mohammed", "Phone" : 2222222222},
    {"Name" : "Khadijah", "Phone" : 3333333333},
    {"Name" : "Abdullah", "Phone" : 4444444444},
    {"Name" : "Rowan"   , "Phone" : 5555555555},
    {"Name" : "Faisal"  , "Phone" : 7777777777}
]

#===============================================================
# 2. Menu Contacts.
def show_menu():
    print("=========== Welcome to Phone Contacts ===========")
    print("============= Phone Register Window =============")
    print(" => 1.Search by Name.")
    print(" => 2.Search by Phone.")
    print(" => 3.Exit.")
    print('=================================================')

#================================================================

# 3. search by number in records. 
def search_number(user_number):
    for record in contacts:
        if user_number == record['Phone']:
            return True, record['Name']
    # if don't found anything ,return False.
    return False,None

#================================================================

# 4. search by name in records.
def search_name(user_name):
    for record in contacts:
        if user_name == record['Name']:
            return True, record["Phone"]
    # if don't found anythingm return False.
    return False, None

#===============================================================
# 5.  handle input user.

def check_number_input(number):

    # Message for user.
    message_1 = str("Invalid input, Number not integer.")
    message_2 = str("Invalid input, the number should be 10 digits.")
    message_3 = str("Valid input.")

    # store value of length validition
    valid_length = not(len(str(number)) == 10)

    if not isinstance(number, int):
        return False, message_1
    elif (valid_length):
        return False, message_2
    else:
        return True, message_3
     

def check_name_input(name):

    # Message for user.
    message_1 = str("Invalid input, should be characters.")
    message_2 = str("Invalid input, limits is 20 characters .")
    message_3 = str("Valid input.")

    length = len(name)
    
    if not(name.isalpha()):
        return False, message_1
    elif not(length > 2 and length < 10):
        return False, message_2
    else:
        return True, message_3

          
#===============================================================
# 6. Add new user:
def add_user(contacts):

    message = str([])
    attempts = 0
    
    print("Add section : ")
    user_name = str(input("Enter Name: ").rstrip())
    
    while(attempts < 3):

        try:
            user_phone = int(input("Enter phone: "))
        except ValueError:
            print("This is invalid number.")
            continue

        result, message =  check_input(user_phone)    
        
        attempts += 1

        if  result != True:
            print(f"{message}.")
        else:
            user_dict = {"Name" : user_name,"Phone": user_phone}
            contacts.append(user_dict)
            return user_dict

    print("You reached the limit.")
    
#===============================================================

# 7. main controll to connect all func.
def main():

    attempts = 0
    user_number = 0
    user_name = ''
    choice = -1


    while(choice != 3):

        show_menu()
        choice = int(input("Enter choice:"))

        # 1. Search by Name :
        if choice == 1:

            while (attempts < 3):
                try:
                    user_name = str(input("Enter Name : ").rstrip())
                except ValueError:
                    print("This is invalid Name.")
                    continue
            
                attempts += 1

                message = str([])
                result , message = check_name_input(user_name)
            
                # if input invalid print message to user
                if result != True:
                    print(message)
                # if input valid print message to user.
                else:
                    print(message)
                    break
                
            check_phone_val ,phone_record = search_name(user_name)

            if(check_phone_val == True):
                print(f"Phone = {phone_record}")
            elif(check_phone_val != True):
                print("=> Sorry, the name is not found.")
                print("=> Add user record [Yes] or [NO] :")
                choice_for_rec = input("Enter your choice: ")

                if choice_for_rec.lower() == 'yes':
                    new_user = add_user(contacts)
                    print(f"New user : {new_user}.")    

                elif choice_for_rec.lower() == 'no':
                    print("Exit Program.")
        
        # 2. Search by Phone : 
        elif choice == 2:

            while (attempts < 3):

                try:
                    user_number = int(input("Enter Phone number: "))
                except ValueError:
                    print("This is invalid number.")
                    continue

                attempts += 1

                message = str([])
                result , message = check_number_input(user_number)
            
                # if input invalid print message to user
                if result != True:
                    print(message)
                # if input valid print message to user.
                else:
                    print(message)
                    break
                
            check_name_val ,name_record = search_number(user_number)

            if(check_name_val == True):
                print(f"Name = {name_record}")

            elif(check_name_val != True):
                print("=> Sorry, the number is not found.")
                print("=> Add user record [Yes] or [NO] :")
                choice_for_rec = input("Enter your choice: ")

                if choice_for_rec.lower() == 'yes':
                    new_user = add_user(contacts)
                    print(f"New user : {new_user}.")    

                elif choice_for_rec.lower() == 'no':
                     print("Exit Program.")
        
        # 3. Exit.
        elif choice == 3:
            print('=' * 15,"Exit window.",'=' * 15)
            print(" => Exit Program. ")
        
        # if something else happed.
        else:
            print("Invalid input, try again")

            

# 8. Run main func.
main()

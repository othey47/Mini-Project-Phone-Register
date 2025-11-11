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

# 2. search on number in records. 
def search_number(user_number):
    for record in contacts:
        if user_number == record['Phone']:
            return True, record['Name']
    # if don't found anything ,return False.
    return False,None

#================================================================

# 3. search on name in records.
def search_name(user_name):
    for record in contacts:
        if user_name == record['Name']:
            return True, record["Name"]
    # if don't found anythingm return False.
    return False, None

#===============================================================
# 4.  handle input user.

def check_input(num):

    # Message for user.
    message_1 = str("Invalid input, Number not integer.")
    message_2 = str("Invalid input, the number should be 10 digits.")
    message_3 = str("Valid input.")

    # store value of length validition
    valid_length = not(len(str(num)) == 10)

    if not isinstance(num, int):
        return False, message_1
    elif (valid_length):
        return False, message_2
    else:
        return True, message_3
     
#===============================================================
# 5. Add new user:
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

# 6. main controll to connect all func.
def main():

    attempts = 0
        
    print("==> Welcome to Phone Contacts.")
    number = 0

    while (attempts < 3):

        try:
            number = int(input("Enter Phone number: "))
        except ValueError:
            print("This is invalid number.")
            continue

        attempts += 1

        message = str([])
        result , message = check_input(number)
            
        # if input invalid print message to user
        if result != True:
            print(message)
        # if input valid print message to user.
        else:
            print(message)
                
    check_num_val ,name_record = search_number(number)

    if(check_num_val == True):
        print(f"Name = {name_record}")

    else:
        print("=> Sorry, the number is not found.")
        print("=> Add user record [Yes] or [NO] :")
        choice = input("Enter your choice: ")

        if choice.lower() == 'yes':
            new_user = add_user(contacts)
            print(f"New user : {new_user}.")    

        elif choice.lower() == 'no':
            print("Exit Program.")

# 7. Run main func.
main()

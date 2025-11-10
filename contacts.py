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
# 2. Check if number in records. 
def check_number(user_number):
    for Record in contacts:
        if user_number == Record['Phone']:
            return True, Record
    # if don't found anything ,return False
    return False,None

#================================================================
# 3. handle input user.
def check_input(num):

    message_1 = str("Invalid input, Number not interger.")
    message_2 = str("Invalid input, the number should be in range of 7-12 digits.")
    message_3 = str("Input valid.")

    if type(num) != type(int(num)):
        return False, message_1
    elif not(num in range(11111111,999999999999)):
        return False, message_2
    else:
        return True, message_3
     
#===============================================================


# 4. main controll to connect all func.
def main():
    try:

        value = False
        attemps = 0
        
        print("Welcome to Phone Contacts")
        number = 0

        while (value == True or attemps != 3):

            
            number = int(input("Enter Phone number: "))
            attemps += 1

            message = str([])
            result , message = check_input(number)
            
            # if input invalid print message to user
            if result != True:
                print(message)
            # if input valid print message to user.
            else:
                print(message)
        

        
        check_num_val ,content_record = check_number(number)

        if(check_num_val == True):
                print(f"Record = {content_record}")
        else:
            print("Not found, try again")
 
    except ValueError:
        print("Program crach. try again.")


# 5. Run main func.
main()

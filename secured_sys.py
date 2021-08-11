import random

def select_random_codes(codes):
    _list = []
    i = 0
    while i < 3:
        #_list.append(codes[random.randint(0, len(codes) - 1)])
        _list.append(random.choice(codes))
        i = i + 1
    return _list


print (f'''
            ================================
            || WELCOME TO SECURED SYSTEMS ||
            ================================
        
Our security systems are based on a highly selected secured encrypted
encoding systems.

''')

username = "lesotho"
password = "les123"
codes = ['mango', 'table', 'trees', 'apple', 'dress']
new_list = []

    
while True:
    _username = input("Enter your username: ")
    _password = input("Enter your password: ")
    
    if _username == username and _password == password:
        new_list = select_random_codes(codes)
        #print(random.choice(new_list[0]))
    else:
        print ('Invalid username or password')

    print(f'''
            Welcome {_username.upper()} to your own secured system.
            Your security word list are:

            {new_list}
            
            Please save this to be used when required for any of the following processes.

            SELECT OPTION
            Choose from the list of actions to proceed
            1. Get account information
            2. Reset password
            3. Change username
            ''')

    # Getting a random index of the position of the each letter of the random word code given.
    position = ["FIRST", "SECOND", "THIRD", "FOURTH", "FIFTH"]

    select_option = input(">>> ")
    if select_option == "2" or '3':
        first = random.randint(0, len(position) - 1)
        second = random.randint(0, len(position) - 1)
        third = random.randint(0, len(position) - 1)
        letter_code = [[first, position[first]], [second, position[second]], [third, position[third]]]

        # inputting the security letter code
        _secureCode = input(f'''Input the {letter_code[0][1]} letter of the first word, {letter_code[1][1]} letter of the second word and the {letter_code[2][1]} letter of the third word  of your security list  ''')
        trial_count = 0
        trial_limit = 2
        while trial_count < trial_limit:
            trial = input ("Secure code does not match. Try again!  ")
            trial_count += 1
            # _secureCode = input(f'''Input the {letter_code[0][1]} letter of the first word, {letter_code[1][1]} letter of the second word and the {letter_code[2][1]} letter of the third word  of your security list  ''')
            sec_input1 = new_list[0][first]
            sec_input2 = new_list[1][second]
            sec_input3 = new_list[2][third]

            if _secureCode == sec_input1 + sec_input2 + sec_input3:
                print ("OK")
                break
        else:
            print ("Please, try again later")




            # if _secureCode != sec_input1 + sec_input2 + sec_input3:     
            #     trial = input("Secure code does not match. Try again!  ")
            #     trial_count += 1
            #     trial = input("Try again!  ")
            #     print("Error, please try again later")
            # else:
            #     print("OK")
            
            #changing password and username
        if select_option == "2":
            new_password = input("Please enter your new password  ")
            confirm_password = input("Confirm your new password  ")
            if new_password == confirm_password:
                password = new_password
                print("Successfully changed password")
                break

        if select_option == "3":
            new_username = input("Enter a new username  ")
            username = new_username
            print("Username successfully changed")
            break
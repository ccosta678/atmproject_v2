

#register
# - first name, last name, password, email
# - generate user account

#login
# - account number, password

#create new


#bank operations

#Initializing the system
import random
database = {}  # dictionary

def init():
    
    print("Welcome to BankPHP")  

    haveAccount = int(input("Do you have an account with us: 1 (yes) 2 (no) "))
        
    if(haveAccount ==1):
        login()
    
    elif(haveAccount == 2):
        register()

    else:
        print("You have selected invalid option.")   
        init()       

database_user = {
    '0123456789':'passwordChandra',
    '0000000000':'passwordCameron',
    '1111111111':'passwordChristian'
}

def login():
    #login function here
    account = input("What is your account? \n")
    password = input("Your password? \n")
    if(account in database_user and password == database_user[account]):
        print("Welcome to BankPHP!")
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False



def register():
    print("*****Register an account*****")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself: \n")

    accountNumber = generateAccountNumber()

    database[accountNumber] = [first_name, last_name, email, password]

    print("Your account has been created.")
    print(" == === ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == === ====== ===== ===")

    login()


def bankOperation(user):

    print("Welcome %s %s" % (user[0], user[1]))

    
    selectedOption = int(input("What would you like to do? (1) Deposit (2) Withdrawal (3) Logout (4) Exit \n"))

    if(selectedOption == 1):
        depositOperation()

    elif(selectedOption == 2):
        withdrawalOperation()
    elif(selectedOption == 3):
        logout()
    elif(selectedOption == 4):   
        exit()
    else:
        
        print("Invalid option selected")  
        bankOperation(user)

def withdrawalOperation():
    print("withdrawal")

def depositOperation():
    print("Deposit Operations")
            

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)   

def logout():
    login()

 ##### ACTUAL BANKING SYSTEM  ####

init()
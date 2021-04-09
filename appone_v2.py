#register
# - first name, last name, password, email
# - generate user account


#login
# - account number & password


#bank operations

#Initializing the system
import random
from datetime import datetime
now = datetime.now()
#database = {} #dictionary

def init():
   
    print("Welcome to Bank of Northwind")
    haveAccount = int(input("Do you have account with us: 1 (yes) 2 (no) \n"))

    if(haveAccount == 1):      
        login()

    elif(haveAccount == 2):      
        register()

    else:
        print("You have selected invalid option")
        init()


databaseUser={1111111111: ['Seyi','Onifade','seyionifade@zuriteam.com', 'PasswordSeyi'],
              2222222222:["Wendy", "Rice", "wrice@team.com", "PasswordRice"],
              0000000000:["Michelle","May","mmay@gmail.com","PasswordMay"]}

def login():
    
    counter=0 

    accountNumberFromUser = int(input("\nWhat is your Account Number?\n"))
    password = input("\nWhat is your password?\n")

    for accountNumber,userDetails in databaseUser.items():
        if (accountNumber==accountNumberFromUser and userDetails[3]==password) :               
            counter=1
            bankOperation()
    
    
    if (counter==0):
        print("Invalid account or password")
        userContinue=input("Would you like to continue y/n?\n")
        if (userContinue=='y'): login()
        else: 
            print("Good Bye\n")
            exit()



def register():

    print("****** Register *******")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password for yourself \n")

    accountNumber = generateAccountNumber()

    databaseUser[accountNumber] = [ first_name, last_name, email, password ]

    print("Your Account Has been created")
    print(" == ==== ====== ===== ===")
    print("Your account number is: %d" % accountNumber)
    print("Make sure you keep it safe")
    print(" == ==== ====== ===== ===")

    login()

def bankOperation():
   
    print("\n***************  Welcome to Bank of Northwind  ****************")
    dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
    print("Current date and time:", dt_string) 

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
        bankOperation()


def withdrawalOperation():
    balance = 250
    withdrawalAmt = int(input('How much do you want to withdraw? '))
    if withdrawalAmt > balance:
        print('The amount requested is greater than the balance. ')
    else:
        balance = balance - withdrawalAmt
        print('Take your cash. Your balance is $%s.' % balance) 
        bankOperation()        
        
def depositOperation():
    balance = 250   
    depositAmt = int(input('How much do you want to deposit? '))
    balance = depositAmt + balance
    print('Your deposit was successful. Balance: $%d.' % balance)
    bankOperation()
        

def generateAccountNumber():
    return random.randrange(1111111111,9999999999)   

def logout():
    init()

 ##### ACTUAL BANKING SYSTEM  ####

init()


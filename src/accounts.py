import getpass
accounts = {}


def add_account(name, password):
   
    while name not in accounts:
        name = input("Enter your name your name to signup\n")
        if name not in accounts:
             accounts[name] = password
        break
        print("Sorry, that user name is already in use") 

    while len(password)<4:
           password = input("Please assign a password to this account, pin should be at least 5 characters\n")         
           if len(password)>4:
               print("Your have successfully signed up")  
               accounts[name] = password
               break
           print("Sorry, that is a short password") 
    return accounts


def login(password, name):

    while password not in accounts: 
        name = input("Enter your username\n")
        password = input("Enter your password\n")
        if password in accounts:
            userpassword = password
            username = name
            return accounts
        else:
            print("Sorry %, Wrong password")    
            again = input("Would like to type in your password again? (y/n)")
            if again.lower()=='y':
                login("","")
            else:
                print("Bye bye, thank you")
                exit()    
        

  





    
  



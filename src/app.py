from tasks import todo_list, create_filewrite, delete_account 
from accounts import accounts, add_account, login
import getpass

def main():
    opt_list = [add_account("", ""), 
                login("", ""), 
                create_filewrite,
                delete_account,
                ]

    while(True):            
        print ("SELECT OPTION:")  
        print ("1\tadd account")
        print ("2\tlogin")
        print ("3\tcreate user")
        print ("4\tdelete user")
     
        opt_choice = int(input("SELECTION: "))
        opt_choice -= 1
        #opt_list[opt_choice]()
        opt_list(opt_choice)()

        
    return

if __name__ == "__main__":
    main()                 
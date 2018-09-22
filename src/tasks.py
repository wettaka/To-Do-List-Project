
todo_list = []


def create_filewrite(item):
    if item==accounts:
        text = open("accountsfile.txt")
        for i in item:
            text.write(i +"\n")
        text.close()        

def delete_account(name):
    accountnumber = accounts.index(name)
    del accounts[accountnumber]


    

class Login() :
    
    def login():
        lst = []
        userName,passWord = [],[]
        with open("./db/account.txt","r") as file :
            data = file.read().splitlines()            
            for line in data :
                lst = line.split()
                userName.append(lst[3])
                passWord.append(lst[4])
            print(userName,passWord)
        username = input("Enter username : ")
        password = input("Enter password : ")
        while username not in userName and password not in passWord :
            print("\n#### Login fail! ####")
            print("Invalid username or password!")
            username = input("Enter username : ")
            password = input("Enter password : ")
        print("\n#### Login completed! ####")

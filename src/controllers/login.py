class Login() :
    
    def login():
        lst = []
        userName,passWord = [],[]
        # username = input("Enter username : ")
        # password = input("Enter password : ")
        with open("./db/account.txt","r") as file :
            data = file.read().splitlines()            
            for line in data :
                lst = line.split()
                userName.append(lst[3])
                passWord.append(lst[4])



print(Login.login())

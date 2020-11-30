import base64

class Login() :
    def login():
        lst = []
        userName,passWord = [],[]
        with open("./db/account.txt","r") as file :
            data = file.read().splitlines()            
            for line in data :
                lst = line.split()
                decrypt = lst[4][2:18]
                base64_bytes = decrypt.encode('ascii')
                message_bytes = base64.b64decode(base64_bytes)
                message = message_bytes.decode('ascii')
                userName.append(lst[3])
                passWord.append(message)
        username = input("Enter username : ")
        password = input("Enter password : ")
        while username not in userName or password not in passWord :
            print("\n#### Login fail! ####")
            print("Invalid username or password!")
            username = input("Enter username : ")
            password = input("Enter password : ")
        print("\n#### Login completed! ####")

import string
import random
letter = list(string.ascii_lowercase)

class Register:
    def __init__(self,first,last,email,phone,idCard,balance,auth):
        self.first = first
        self.last = last
        self.email = email
        self.phone = phone
        self.idCard = idCard
        self.balance = balance
        self.auth = auth
    
    #@method generate number
    # def rand_x_digit_num(x, leading_zeroes=True):    
    #     if not leading_zeroes:
    #     # wrap with str() for uniform results
    #         return random.randint(10**(x-1), 10**x-1)  
    #     else:
    #         if x > 6000:
    #             return ''.join([str(random.randint(0, 9)) for i in range(x)])
    #         else:
    #             return '{0:0{x}d}'.format(random.randint(0, 10**x-1), x=x)

    
    def __str__(self):
        with open("./db/account.txt","a+") as file :
            acc = random.randint(100000000000,999999999999)
            username = self.first.lower()+"."+self.last[0].lower()
            password = self.phone[0:2] + self.first[2].upper() + self.email[0].lower() + str(len(self.first)) + self.last[:2].upper() + self.auth[5] + self.first[1] + self.last[1] + str(acc)[5]
            data = self.first + " " + self.last + " " + str(acc) +" " + username +" " + password +" " + self.email + " " + self.phone + " " + str(self.idCard) + " " + str(self.balance) + self.auth +  "\n"
            file.writelines(data)
            lines = "="*20
            result = "Name : " + self.first + " " + self.last + " Email : " +self.email + " Phone : " + self.phone + ""
            final = "\n" + lines + " Your Data Information " + lines + "\n" + result + "\n" + lines +"  Username & Password  " +lines+ "\n" + "Username : " + username + "\n" + "Password : " + password 
        return final


    def acc() :
        fname = input("Enter Fname : ")
        lname = input("Enter Lname : ")
        email = input("Enter mail : ")
        while "@" not in email : 
            email = input("Enter mail : ")       
        phone = input("Enter phone : ")
        idCard = input("Enter ID-Card number : ")
        while len(idCard) != 13 :
            print("Invalid! Please try again!")
            idCard = input("Enter ID-Card number : ")
        balance = float(input("Please deposit cash more than ฿500 for open account : "))
        while balance < 500 :
            print("Please deposit cash more than ฿500 for open account!")
            balance = float(input("Please deposit cash more than ฿500 for open account : "))
        auth = input("Enter security number for 6 digits ex.(123456) : ")
        while len(auth) != 6:
            print("Please input for 6 digit ex.(123456)!")
            auth = input("Enter security number for 6 digits ex.(123456) : ")
        account = Register(fname,lname,email,phone,idCard,balance,auth)
        print(account)


            
        

            

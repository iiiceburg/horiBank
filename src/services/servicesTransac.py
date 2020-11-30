class Services():
    def servMenu():
        from datetime import datetime
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        dt_object = datetime.fromtimestamp(timestamp)
        lst = []
        name,pin,balance,accNumber = [],[],[],[]
        with open("./db/account.txt","r") as file :
            data = file.read().splitlines()            
            for line in data :
                lst = line.split()
                fullname = lst[0] + " " + lst[1]
                name.append(fullname)
                balance.append(lst[8])
                pin.append(lst[9])
                accNumber.append(lst[2])
        lines = "="*20
        head = lines + " PLEASE CHOOSE SERVICES " + lines
        print(head)
        menu = """
            1.Transfer          2.Withdrawal Cash
            3.Make a Deposit    4.Exit     
        """
        print(menu)
        print("="*len(head))
        menu = input("Please choose services 1,2,3 or 4 : ")
        while menu != "4" :
            while menu not in ["1","2","3","4"]:
                print("Invalid! Please try again!")
                menu = input("Please choose services 1,2,3 or 4 :") 

            #Transfer service

            if menu == "1" :
                print("\nTransfer service")
                account = input("Enter Account number to transfer : ")
                while account not in accNumber:
                    print("Not found account number for transfer!")
                    account = input("Enter Account number to transfer : ")
                endPoint = accNumber.index(account)
                print("Account Name : %s"%name[endPoint])
                blcData = balance[endPoint] # Fisnd position of balance by endpoint
                print("Hori+ can transfer money 0.01 to 10,000,000.00")
                amount = float(input("Enter amount : "))
                while amount <=0 :
                    print("Hori+ can transfer money 0.01 to 10,000,000.00")
                    amount = float(input("Enter amount : "))
                total1 = float(blcData) + amount
                # print("Total = %.2f"%total)               
                confirm = input("Are you sure to tranfer? (y/n) : ")
                while confirm.lower() not in ["y","n","yes","no"]:
                    print("Please select Yes or No (y/n)")
                    confirm = input("Are you sure to tranfer? (y/n) : ")
                if confirm.lower() in ["yes","y"]:
                        with open("./db/log_transfer.txt","a+") as file:
                            status =  str(dt_object) +" Status : Transfer completed "  + " From : " + name[endPoint] + " To : " + name[endPoint] + " Account : " + account + " Amount : " + str(amount) + " Balance : " +  str(total1)
                            file.writelines(status + "\n")
                        print("### Status : Completed! ###")

                else :
                    with open("./db/log_transfer.txt","a+") as file:
                        status =  str(dt_object) +" Status : Transfer Cancel "  + " Name : " + name[endPoint] + " Account : " + account + " Amount : " + str(amount) + " Balance : " +  str(blcData)
                        file.writelines(status + "\n")
                        print("### Status : Cancel! ###") 

            #Witdrawal service                   
                
            elif menu == "2":
                print("\nWithdrawal Cash service")
                pinAuth = input("Enter pin : ")
                while pinAuth not in pin:
                    print("Invalid pin! Please try again.")
                    pinAuth = input("Enter pin : ")
                print("You can withdrawal only Banknote 100,500,1000")
                pinEndpoint = pin.index(pinAuth)            
                blcCheck = balance[pinEndpoint]
                accounCheck = accNumber[pinEndpoint]
                accName = name[pinEndpoint]
                print("Account name : %s "%(accName))
                print("Balance : %.2f"%(float(blcCheck)))
                amount = int(input("Enter amount for withdrawal : "))
                total =  float(blcCheck) - float(amount)
                while amount > float(blcCheck) :
                    print("You can't withdrawal cash more than your balance in account")
                    print(blcCheck)
                    amount = int(input("Enter amount for withdrawal : "))
                confirm = input("Are you sure to tranfer? (y/n) : ")
                while confirm.lower() not in ["y","n","yes","no"]:
                    print("Please select Yes or No (y/n)")
                    confirm = input("Are you sure to tranfer? (y/n) : ")
                if confirm.upper() in ["YES","Y"]:
                    with open("./db/log_withdrawal.txt","a+") as file:
                        status =  str(dt_object) +" Status : Withdrawal completed "  + " Name : " + name[pinEndpoint] +  " Account : " + accounCheck + " Amount : " + str(amount) + " Balance : " +  str(total)
                        file.writelines(status + "\n")
                    print("### Status : Completed! ###")
                    print("Balance : %.2f "%total)
                elif confirm.upper() in ["NO","N"] :
                    with open("./db/log_withdrawal.txt","a+") as file:
                        status =  str(dt_object) +" Status : Withdrawal Cancel "  + " Name : " + name[pinEndpoint] + " Account : " + accounCheck + " Amount : " + str(amount) + " Balance : " +  str(blcCheck)
                        file.writelines(status + "\n")  
                    print("### Status : Cancel! ###") 
                    print("Balance : %.2f "%blcCheck)     

            #Make a deposit service

            elif menu == "3" :
                print("\nMake a deposit service")
                account = input("Enter Account number to deposit : ")
                while account not in accNumber:
                    print("Not found account number for deposit!")
                    account = input("Enter Account number to deposit : ")
                endPoint = accNumber.index(account)
                print("Account Name : %s"%name[endPoint])                
                pinAuth = input("Enter pin : ")
                while pinAuth not in pin:
                    print("Invalid pin! Please try again.")
                    pinAuth = input("Enter pin : ")
                pinEndpoint = pin.index(pinAuth)            
                blcCheck = balance[pinEndpoint]
                accounCheck = accNumber[endPoint]
                print("You can deposit cash 100 to 100,000")
                amount = int(input("Enter amount for deposit : "))
                total = float(amount) + float(blcCheck)
                while amount not in range(100,100000):
                    print("You can deposit cash 100 to 100,000!")
                    amount = int(input("Enter amount for deposit : "))
                confirm = input("Are you sure to Deposit? (y/n) : ")
                while confirm.lower() not in ["y","n","yes","no"]:
                    print("Please select Yes or No (y/n)")
                    confirm = input("Are you sure to Deposit? (y/n) : ")
                if confirm.upper() in ["YES","Y"]:
                    with open("./db/log_deposit.txt","a+") as file:
                        status =  str(dt_object) +" Status : Deposit completed "  + " Name : " + name[pinEndpoint] + " Account : " + accounCheck + " Amount : " + str(amount) + " Balance : " +  str(total)
                        file.writelines(status + "\n")
                    print("### Status : Completed! ###")
                    print("Balance : %.2f "%total)
                    
                elif confirm.upper() in ["NO","N"] :
                    with open("./db/log_deposit.txt","a+") as file:
                        status =  str(dt_object) +" Status : Deposit Cancel "  + " Name : " + name[pinEndpoint] + " Account : " + accounCheck + " Amount : " + str(amount) + " Balance : " +  str(blcCheck)
                        file.writelines(status + "\n")
                    print("### Status : Cancel! ###")   
                    print("Balance : %.2f "%blcCheck)    
            menu = input("\n Please choose services 1,2,3 or 4 :")
        print("========== Hori+ Thank you! ==========")    
        print("Exit program")
         
                                  

            
            

            


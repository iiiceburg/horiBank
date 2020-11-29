class services():
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
            print(balance,pin)
        lines = "="*20
        head = lines + " PLEASE CHOOSE SERVICES " + lines
        print(head)
        menu = """
            1.Transfer          2.Withdrawal Cash
            3.Make a Deposit    4.Balance Check 
            5.Exit        
        """
        print(menu)
        print("="*len(head))
        menu = input("Please choose services 1,2,3,4 or 5 : ")
        while menu not in ["1","2","3","4","5"]:
            print("Invalid! Please try again!")
            menu = input("Please choose services 1,2,3,4 or 5 :")
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
            total = float(blcData) + amount
            # print("Total = %.2f"%total)
            balance[endPoint] = str(total)
            lst2 = [] #list for check and transfer
            for line in data :
                lst2 = line.split()
                if account in lst2:
                    with open("./db/log_transactionTransfer.txt","a+") as file:
                        status =  str(dt_object) +" Status : Transfer completed "  + " Name : " + name[endPoint] + " Account : " + account + " Amount : " + str(amount) + " Balance : " +  str(total)
                        file.writelines(status + "\n")
                print(lst2)
            print(balance)
            
        elif menu == "2":
            print("\nWithdrawal Cash service")
            pinAuth = input("Enter pin : ")
            while pinAuth not in pin:
                print("Invalid pin! Please try again.")
                pinAuth = input("Enter pin : ")
            print("You can withdrawal only 100,500,100")
            amount = int(input("Enter amount for withrawal : "))

            

services.servMenu()
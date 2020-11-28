class services():
    def servMenu():
        lst = []
        pin,balance,accNumber = [],[],[]
        with open("./db/account.txt","r") as file :
            data = file.read().splitlines()            
            for line in data :
                lst = line.split()
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
            print(balance)
            account = input("Enter Account number to transfer : ")
            while account not in accNumber:
                print("Not found account number for transfer!")
                account = input("Enter Account number to transfer : ") 
            endPoint = accNumber.index(account)
            blcData = balance[endPoint] # Find position of balance by endpoint
            print("Hori+ can transfer money 0.01 to 10,000,000.00")
            amount = float(input("Enter amount : "))
            while amount <=0 :
                print("Hori+ can transfer money 0.01 to 10,000,000.00")
                amount = float(input("Enter amount : "))
            total = float(blcData) + amount
            # print("Total = %.2f"%total)
            balance[endPoint] = str(total)
            print(balance)
            
        elif menu == "2":
            pass

            

services.servMenu()
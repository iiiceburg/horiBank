from controllers.login import Login
from controllers.register import Register
from services.servicesTransac import Services

lines = "="*20
head = lines + " Welcome to Hori+ Bank " + lines
sep = "\n"+"="*len(head)  # seperate lines

def welcome():         
    print(head)
    print("\n"+" "*len(lines)+"1.Login      2.Register")
    print(sep)
    

def menu():
    menu = input("\n Please select 1 or 2 : ")
    while menu not in ["1","2"] :
        menu = input("Please select 1 or 2 : ")   
        print(sep)
    if menu == "1" :
        print("\n=== Login === \n ")
        Login.login()
        Services.servMenu()
    elif menu == "2" :
        print("\n=== Registration === \n")
        Register.acc()
        Services.servMenu()

welcome()
menu()    

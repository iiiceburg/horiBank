from controllers.login import Login
from controllers.register import Register
def welcome():
    lines = "="*20
    print(lines + " Welcome to Hori+ Bank " + lines)
    print("\n1.Login      2.Register")

def menu():
    menu = input("Please select 1 or 2 : ")
    while menu not in ["1","2"] :
        menu = input("Please select 1 or 2 : ")   
    if menu == "1" :
        print("\n=== Login === \n ")
        Login.login()
    elif menu == "2" :
        print("\n=== Registration === \n")
        Register.acc()

# def transaction():
#     pass
welcome()
menu()    

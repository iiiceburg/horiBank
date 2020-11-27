with open("account.txt","r") as file:
    data = file.read()
    lst = []
    for line in data:
        lst = data.splitlines()
    print(lst)
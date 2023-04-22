import json
import createstatement
InitialAccountNumber = 6000000000
def updatefile():
    usersFile = open("users.txt", "w")
    contentString = ""
    for i in usersListConverted:
        contentString = contentString + str(i) + "\n"
    usersFile.write(contentString)

def viewaccountdetails():
    for i in userData:
        if(i=="password"):
            continue
        print(i,":",userData[i])
def deposit(user):
    amount=float(input("Enter the amount: "))
    for i in usersListConverted:
        if i['username']==user:
            i['accountBalance']=i['accountBalance']+amount
    updatefile()
    createstatement.createEntry(user, amount, "debit")
    print("Amount deposited")
def withdraw(user):
    amount=float(input("Enter the amount: "))
    if(amount>userData["accountBalance"]):
        print("Not enough balance in your account")
        return
    for i in usersListConverted:
        if i['username']==user:
            i['accountBalance']=i['accountBalance']-amount
    updatefile()
    createstatement.createEntry(user,amount,"credit")
    print("Amount withdrawed")
def transfer(user):
    accountnumber=int(input("Enter the recipient account number for the transaction "))

    amount=float(input("Enter the amount to be transfered"))
    if(amount>userData["accountBalance"]):
        print("Not enough balance in your account")
        return
    accountexist=0
    for i in usersListConverted:
       if (i["accountNumber"]==accountnumber):
           accountexist=1
       if(accountexist==0):
           print("This account number does not exits")
           return

    for i in usersListConverted:
        if(i["username"]==user):
            i["accountBalance"]=i["accountBalance"]-amount
        if(i["accountNumber"]==accountnumber):
            i["accountBalance"]=i["accountBalance"]+amount
    updatefile()
    createstatement.createEntry(user, amount, "debit")
    print("Transfer Sucessful!")
def viewaccountstatement():
    statementfile=open("accountstatement.txt")
    filecontent=statementfile.read()
    filecontentSplit=filecontent.split("\n")
    for i in filecontentSplit:
        linesplit=i.split()
        if len(linesplit) > 0 and linesplit[0] == userName:
            print(i)
userData={}
usersListConverted = list()
def validateUser(userName, password):
    global userData
    global usersListConverted
    usersFile = open("users.txt")
    fileContent = usersFile.read()
    fileContentSplit = fileContent.split("\n")

    for i in fileContentSplit:
        if i == "":
            continue
        stringConverted = i.replace("'", "\"")
        usersListConverted.append(json.loads(stringConverted))
    userFound=0
    foundPassword=""
    for user in usersListConverted:
        if user["username"] == userName:
            userFound=1
            foundPassword=user["password"]
            userData=user
    if userFound==0:
        print("Invalid username !")
    elif userFound==1:
        if(foundPassword==password):
            print("Login Successful")
            return "success"

        else:
            print("Invalid Password !")
def getNumberofUsers():
    usersFile = open("users.txt")
    fileContent = usersFile.read()
    fileContentSplit = fileContent.split("\n")
    numberOfUsers = len(fileContentSplit)
    return numberOfUsers


def register():
    userCount = getNumberofUsers()
    accountNumber = InitialAccountNumber + userCount
    name = input("Enter the Name: ")
    phoneNumber = input("Enter the Phone Number: ")
    address = input("Enter the Address:")
    email = input("Enter the MailID: ")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    usersfile = open("users.txt", "a")
    userData = {
        "name": name,
        "phoneNumber": phoneNumber,
        "address": address,
        "email": email,
        "username": username,
        "password": password,
        "accountNumber": accountNumber,
        "accountBalance":0
    }
    userDataConverted = str(userData)
    userDataConverted = userDataConverted + "\n"
    usersfile.write(userDataConverted)
    print("Registration Success !")

print("Welcome to Progress bank.\nPlease choose one of the following options: ")
option = input("\n1.Login\t2.Register")
if option == "1":
    userName = input("Enter Username: ")
    password = input("Enter Password: ")
    validateResult=validateUser(userName, password)
    if (validateResult=="success"):
        print("Select one of the following options:\n1.View account\n2.Deposit\n3.Withdraw\n4.Transactions\n5.View account Statement")
        option2=input()
        if(option2=="1"):
            viewaccountdetails()
        elif(option2=="2"):
            deposit(userName)
        elif(option2=="3"):
            withdraw(userName)
        elif(option2=="4"):
            transfer(userName)
        elif(option2=="5"):
            viewaccountstatement()
        else:
            print("Invalid input !")

elif option == "2":
    register()
else:
    print("Invalid Input!")
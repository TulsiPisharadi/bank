import datetime

def createEntry(username,amount,transactiontype):
    statementfile=open("accountstatement.txt","a")
    currentdate=datetime.datetime.now()
    currentdateconverted=str(currentdate)
    statementfile.write(username+" "+str(amount)+" "+transactiontype+" "+currentdateconverted+"\n")

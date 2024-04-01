class Balance:
    def __init__(self,bal,accinfo):
            self.bal=bal
            self.accinfo=accinfo
               
    def debitmoney(self,debit):
            self.bal -=debit
            print(debit,end="")
            print("\t\t\t\t\t",self.printbal())
    
    def creditmoney(self,credit):
            self.bal +=credit 
            print("\t\t",credit,end="")
            print("\t\t\t",self.printbal())
    
    def printbal(self):
            return self.bal
    

accinfo=int(input("Enter the account number: "))
bal=int(input("Enter the current balance: "))
acc1=Balance(bal,accinfo)
print("Enter the amount to transacted:")
print("To debit write 'D' after the amount")
print("TO credit write 'C' after the amount")
print("To end Type 'END'")
transaction=[]
transactchoice=input("Enter the amount along with letter for transaction or enter END to terminate: ")
while(transactchoice!="END"):
        transaction.append(transactchoice)
        transactchoice=input("Enter the amount along with letter for transaction or enter END to terminate: ")
txt='@'
print(65*txt)
print("The ACCOUNT NUMBER is: ",accinfo)
print("DEBIT\t\t\tCREDIT\t\tBALANCE")
print("\t\t\t\t\t",bal)
amt=0
count=0
ch=''
for x in transaction:
        if('C'in x):
                amt=int(x[:len(x)-1])
                acc1.creditmoney(amt)
                count+=1
                
        elif('D'in x):
                amt=int(x[:len(x)-1])
                acc1.debitmoney(amt)
                count+=1
               
finalbal=acc1.printbal()
print("FINAL BALANCE:\t\t",finalbal)
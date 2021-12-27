
class Bank_account:        #a class to get bank accounts
    def __init__(self,name,age,sex,balance):   #attrib. of each account
        self.name=name
        self.age=age
        self.sex=sex
        self.balance=balance 
        self.withd_status="False"  #statuse of withdrowal
        #self.all=self.name,self.age,self.sex,self.balance  #all info. of each account
    def withdraw(self,a):   #withdraw method
        if (a>self.balance):     #first cheak balance and the wanted amount
            print("Max. Allowed Withdraw :",self.balance)
        elif a<=0:
            raise NameError("Error Withdrawal Input")
        else:
            self.balance-=a      #if amount is acceptable then subtract
            self.withd_status="True"    #from balance
            print("Withdrawal :\n",a,
            "\nRemaining Amount :",self.balance,) #show remaining amount
    def deposit(self,a):  #deposit method 
        if a<=0:      #amount should not be under zero!!
            raise NameError("Error Deposit Input")
        self.balance+=a      #add the saved amount to balance if above zero
        print("Deposit :\n",a,
        "\nCurrent Amount :",self.balance)  #show final balance
    def update_det(self):     #update account info. after withdraw or deposit
        self.all=self.name,self.age,self.sex,self.balance,self.withd_status
    def get_details(self):  #show final ditails when called
        self.update_det()
        print("Account details :",self.all )
class Bank():   #class as Bank to save bank accounts also add\remove...
    def __init__(self):
        self.name="N&D Bank"    #attrib of each bank
        self.adress="Berlin-Mitte"
        self.nu_account=0
        self.all_acc=[]
    def add_acc(self,account:Bank_account):  #method to add singel account
        (self.all_acc).append(account)
        self.nu_account+=1
    def add_multi_acc(self,AccList):  #method to add multi. accounts
        for acc in AccList:
            self.add_acc(acc)
    def remov_acc(self,account:Bank_account):  #remove an account
        (self.all_acc).remove(account)
        self.nu_account-=1
    def get_info(self):   #details of bank with total nu. of accounts
        print("Name of Bank :",self.name)
        print("Adress :",self.adress)
        print("Nu. od Accounts",self.nu_account)
    def get_acc(self,a):   #method to get ditails of a specific account
        if a<=self.nu_account-1:
            self.all_acc[a].get_details()
        else:
            raise ValueError
    def read_acc_list(self,filename,a): #method to read accounts data from a file
        f=open(filename,"r") #read file
        for k in range(a): #read out unneeded lines
            f.readline()
        i=0 #list starts at 0
        Namelist=[] #list for each variable
        Sexlist=[]
        Agelist=[]
        Balancelist=[]
        tmp_acc_list=[]
        for line in f: #extract coulumns in each line & add each coulumn
                        #to its variable list 
            line=line.strip() 
            coulumn=line.split()
            Namelist.append(coulumn[0])
            Sexlist.append(coulumn[1].strip(",")) #stripping unneeded str.(",")
            Agelist.append(int(coulumn[2].strip(",")))
            Balancelist.append(float(coulumn[3].strip(",")))
            tmp_acc_list.append(Bank_account(Namelist[i],Agelist[i],Sexlist[i],Balancelist[i]))
            i+=1
        return tmp_acc_list #return a list with all acounts details saved in
    def sub_from_acc(self,w,age): #method to subtract fees from all acount
        self.w=w
        self.age=age #age of holders to start subtracting
        for a in range(self.nu_account):
            if (self.all_acc[a].balance > w) and (self.all_acc[a].age > age):
                self.all_acc[a].withdraw(w)
    def write_infile(self,filename): #method to print the final data of all accounts intto a file
        f=open(filename,"w")
        #up headers to tell details of the data saved
        f.write("=======================================================================================\n")##another way??!!
        f.write("************************** Confidential **************************\n")##another way??!!
        f.write("This is a File contanins the first {} Accounts in our Bank\n\n".format(self.nu_account)) #nu. of accounts
        #fees/age to start subtracting
        f.write("(-{0:0}$ from each Account when holder is over {1:0} years old)\n\nSignature: Ahmed\n".format(self.w,self.age)) 
        f.write("=======================================================================================\n")
        #info. of each coulumn in data list
        f.write("{0:16},{1:16},{2:16},{3:16},{4:16}\n".format(str("Name"),str("Sex"),str("Age"),str("Balance"),str("Withdraw Status")))
        f.write("---------------------------------------------------------------------------------------\n")
        #printing data of the bank accounts in the after headers
        for i in self.all_acc:
            f.write("{0:16},{1:16},{2:16},{3:0.3f}\t{4:10},{5:1}\n".format(i.name,i.sex,str(i.age),i.balance,str(""),i.withd_status))
        f.close()


my_bank=Bank()
##my_bank.add_acc(Bank_account(Namelist[i],Agelist[i],Sexlist[i],Balancelist[i]))##
x=my_bank.read_acc_list("Bank_Accounts.dat",7)
##for i in range(0,len(x)):
 ##   x[i].withdraw(20)##
my_bank.add_multi_acc(x)
my_bank.sub_from_acc(10,18)
for i in range(my_bank.nu_account):
    print (my_bank.all_acc[i].withd_status)
my_bank.get_info()
my_bank.write_infile("myfile.txt")

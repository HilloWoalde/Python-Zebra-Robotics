from CreditCardGen import luhn_algorithm
accounts=[]
class BankAccount:
    def __init__(self, name, dob, sin, phone, pin, balance = 0.00, acctNum = luhn_algorithm()):

        self.name = str(name)
        
        # Save DOB as "12/31/2023"
        
        self.dob = str(dob)
        
        self.sin = str(sin)
        
        # Save Phone Number as 16474365206
        
        self.phoneNum = str(phone)
        
        self.balance = 0.00
        
        self.pin = str(pin)

        self.acctNum = acctNum

        self.deposit(float(balance))

    def checkUser(self, acct, pin):
        q = False
        for i in accounts:
            if i.acctNum == acct and i.pin == pin:
                q = True
        return q
    
    def stringify(self):
        x=""
        x += ("Name:" + self.name)
        x += ("\n")
        x += ("DOB:" + self.dob)
        x += ("\n")
        x += ("SIN:" + self.sin)
        x += ("\n")
        x += ("Phone:" + self.phoneNum)
        x += ("\n")
        x += ("Pin:" + self.pin)
        x += ("\n")
        x += ("Balance:" + str(self.balance))
        x += ("\n")
        x += ("AcctNum:" + str(self.acctNum))
        x += ("\n")
        return(x)

    def deposit(self, money):

        if float(money) <= 1.00:
            print("You have deposited too little.")
        
        elif float(money) >= 1000000.00:
            print("You have deposited too much.")

        elif isinstance(money, float) or isinstance(money, int):
            self.balance += money
    
        else:
            print("An error occurred. Please try again later, or ask an assistant for help.")

    def withdraw(self, money):

        if money <= 0.04:
            print("You have withdrawn too little.")
        
        elif money >= 1000000.00 or money > self.balance:
            print("You have withdrawn too much.")

        elif isinstance(money, float) or isinstance(money, int):
            self.balance -= money
        
        else:
            print("An error occurred. Please try again later, or ask an assistant for help.")

def LogIn(acct, pin):
    for i in accounts:
        if i.acctNum == acct and i.pin == pin:
            return i
    else:
        print("Error")

def findAcct(acct, pin):
    for i in accounts:
        if i.acctNum == acct and i.pin == pin:
            q += i
    return q

def createdAcct(acct, pin):
        q = False
        for i in accounts:
            if i.acctNum == acct and i.pin == pin:
                q = True
        return q

donateAcct = BankAccount("Help", "01/01/0001", "000000000", "1416000000", "Empty", 10.00, 5448333145138020)

file = open("Intermediate/71BankAccounts.txt")

lines = file.readlines()

i=0

while True:
    acct = lines[0+(i)].split(":")[1].strip()
    a = (lines[0+(i)].split(":")[1].strip("\n"), lines[1+(i)].split(":")[1].strip("\n"), lines[2+(i)].split(":")[1].strip("\n"), lines[3+(i)].split(":")[1].strip("\n"), lines[4+(i)].split(":")[1].strip("\n"), lines[5+(i)].split(":")[1].strip("\n"), lines[6+(i)].split(":")[1].strip("\n"))
    accounts.append(BankAccount(a[0], a[1], a[2], a[3], a[4], a[5], a[6]))
    i+=7
    if i == len(lines):
        break

# Login
while True:
    donaterAcct=False
    menuoption = input("Select one option using numbers \n 1.  Create an Account\n 2.  Sign In\n")
    if menuoption == "1":
        currentUser = (BankAccount(input("What is the Account Holder's Name? \n"), input("What is the Account Holder's Date of Birth? (Format as MM/DD/YYYY) \n"), input("What is the Account Holder's Social Insurance Number? (Format as 164856194) \n"), input("What is the Account Holder's Phone Number? (Format as 14160425618)\n"), input("What is the PIN for this account? \n"), input("How much would you like to transfer to this account?? \n")))
        accounts.append(currentUser)
        break
    if menuoption == "2":
        currentUser = LogIn(input("What is your Account Number?"), input("What is your PIN?"))
        break

# On Account for Help
while True:
    if currentUser.name == donateAcct.name and currentUser.dob == donateAcct.dob and currentUser.sin == donateAcct.sin and currentUser.phoneNum == donateAcct.phoneNum:
        donaterAcct = True
        menuoption = input("Select one option using numbers \n 1.  Create an Account\n 2.  Sign In\n 3.  Withdraw \n 4.  Donate \n 5.  End Session + Sign Out \n ")
        if menuoption == "1":
            currentUser = (BankAccount(input("What is the Account Holder's Name? \n"), input("What is the Account Holder's Date of Birth? (Format as MM/DD/YYYY) \n"), input("What is the Account Holder's Social Insurance Number? (Format as 164856194) \n"), input("What is the Account Holder's Phone Number? (Format as 14160425618)\n"), input("What is the PIN for this account? \n"), input("How much would you like to transfer to this account?? \n")))
            accounts.append(currentUser)
            break
        elif menuoption == "2":
            currentUser = LogIn(input("What is your Account Number?"), input("What is your PIN?"))
            break
        elif menuoption == "3":
            currentUser.withdraw(float(input("How much are you withdrawing?")))
        elif menuoption == "4":
            currentUser.deposit(float(input("How much are you donating?")))
        elif menuoption == "5":
            file = open("Intermediate/71BankAccounts.txt", "w")
            for i in accounts:
                file.write(i.stringify())
            file.close()
            break
    else:
        break

# On Personal Account
while True:
    if currentUser.name != donateAcct.name or currentUser.dob != donateAcct.dob or currentUser.sin != donateAcct.sin or currentUser.phoneNum != donateAcct.phoneNum:
        menuoption = input("Select one option using numbers \n 1.  Deposit\n 2.  Withdraw\n 3.  Check Balance \n 4.  Change Phone Number \n 5.  Change PIN \n 6.  End Session + Sign Out \n ")
        if menuoption == "1":
            currentUser.deposit(float(input("How much are you depositing?")))
        elif menuoption == "2":
            currentUser.withdraw(float(input("How much are you withdrawing?"))) 
        elif menuoption == "3":
            print("Your balance is:" + str(currentUser.balance))
        elif menuoption == "4":
            currentUser.phoneNum=input("What is the Account Holder's New Phone Number? (Format as 14160425618)\n")
        elif menuoption == "5":
            currentUser.pin=input("What is the New PIN? (Format as 14P052ef18)\n")
        elif menuoption == "6":
            file = open("Intermediate/71BankAccounts.txt", "w")
            for i in accounts:
                file.write(i.stringify())
            file.close()
            break
    else:
        break
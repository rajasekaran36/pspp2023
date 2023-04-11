accounts = []

# It converts CSV file into accounts dictionary
def initiate():
    account_file = open('accounts.csv','r')
    for line in account_file.readlines():
        cols = line.split(',')
        accounts.append({
            'accno':int(cols[0]),
            'name':cols[1],
            'balance':int(cols[2])
        })
    account_file.close()
# get's account dictionary using account_number if found
def get_account(account_number):
    global accounts
    for account in accounts:
        if(account['accno']==account_number):
            return account 
    return None

# display's account details by giving account_number if found
def display_account_details(account_number):
    account = get_account(account_number)
    if account:
        print("ACCNO:",account['accno'])
        print("NAME:",account['name'])
        print("BALANCE:",account['balance'])
    else:
        print('Sorry account not found')

# returns balance of an account if found
def get_balance(account_number):
    account = get_account(account_number)
    if account:
        return account['balance']
    else:
        print('Sorry account not found')

# reduces the balance of an account if account found & sufficient balance 
def withdraw(account_number):
    account = get_account(account_number)
    if account:
        try:
            display_account_details(account_number)
            amount = int(input('Enter amount to withdraw:'))
            if account['balance']>=amount:
                print("Current Balance:",account['balance'])
                account['balance'] = account['balance'] - amount
                print("Amount Debited")
                print("Current Balance:",account['balance'])
            else:
                raise ValueError
        except ValueError:
            print('Insufficient Balance')
    else:
        print('account not found')

# increses the balance if account found
def deposit(account_number):
    account = get_account(account_number)
    if account:
        display_account_details(account_number)
        print('Current Balance:',get_balance(account_number))
        amount = int(input('Enter amount to deposit:'))
        account['balance'] = account ['balance'] + amount
        print("Deposit Completed")
        print('Current Balance:',get_balance(account_number))
    else:
        print("Sorry Account Not Found")

# It saves all changes to the file
def commit():
    global accounts
    account_file = open('accounts.csv','w')
    lines = []
    for account in accounts:
        line = str(account['accno'])+','+account['name']+','+str(account['balance'])+'\n'
        lines.append(line)
    account_file.writelines(lines)
    account_file.close()


#Main Program
initiate()
while True:
    print('''
    1.Account Details
    2.Withdraw
    3.Deposit
    4.Check Balance
    5.Exit
    ''')
    choice = int(input('Enter your choice:  '))
    if choice == 1:
        account_number = int(input('Enter account number:   '))
        display_account_details(account_number)
    elif choice == 2:
        account_number = int(input('Enter account number:   '))
        withdraw(account_number)
    elif choice == 3:
        account_number = int(input('Enter account number:   '))
        deposit(account_number)
    elif choice == 4:
        account_number = int(input('Enter account number:   '))
        print("BALANCE:",get_balance(account_number))
    elif choice == 5:
        print("Thank You !!!")
        commit()
        print("Changes written in accounts file")
        break
    else:
        print("Invalid Choice")   
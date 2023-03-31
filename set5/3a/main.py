'''
Write a Python Program to get the 5 bank customer account details with balance and print
only the customer details whose balance is greater than or equal to 10000
'''
accounts = []
for i in range(5):
    print('Enter',i+1,'customer details')
    name = input('Enter name:')
    balance = int(input('Enter balance amount:'))
    accounts.append({'name':name,'balance':balance})

print('\nThe users having balance > 10000')
for account in accounts:
    if(account['balance']>=10000):
        print(account['name'])
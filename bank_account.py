balance = 2000
amount = int(input("Enter amount to withdraw: "))
isBanned = False

if amount <= balance and not(isBanned):
    balance-=amount
    print(f"{amount} withdrawn successfully, your new balance is {balance}")
else:
    print("Insufficient balance or account is banned!!")
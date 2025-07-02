def deposit(balance,amount):
    if amount > 0:
        balance += amount

    return balance

def withdraw(balance, amount):
    if amount <= balance:
        balance -= amount

    return balance

def check_balance(balance):
    print(f"Balance: {balance}")

hisob = 100

hisob = deposit(hisob, 30)
check_balance(hisob)

hisob = withdraw(hisob, 70)
check_balance(hisob)
print("================")
print("DARA ATM SYSTEM")
print("================")



cards = input("Enter your card (card/no): ").lower()
while cards not in ["card" , "Card"]:
    print("Okay thanks")
    break
 
if cards == "card":  
    cpin = 123069    
    attempt = 3
    while attempt > 0:
        pin = int(input("Enter your pin number: "))
        if pin == cpin:
            print("login success")
            break
        else:
            attempt -= 1
            print("wrong")   
            print("Attempt remaining" , attempt)
            
if attempt == 0:
    print("account locked")             
initbalance = int(input("Enter initial balance: "))
while True:
    print("====Main Menu===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")
    break

op = input("Enter the choices you want: ")
def check_balance(balance):
    return balance

def deposit(balance, amount):
    return balance + amount

def withdraw(balance, amount):
    if amount <= balance:
        return balance - amount
    else:
        print("Insufficient funds")
        return balance
while op not in ["1" , "2" , "3" , "4"]:
    print("Invalid choice. Enter again.")
    op = input("Enter the choices you want: ")
if op == "1":
    print("Your balance is: ", check_balance(initbalance))
elif op == "2":
    amount = int(input("Enter the amount to deposit: "))
    initbalance = deposit(initbalance, amount)
    print("Amount deposited successfully")
elif op == "3":
    amount = int(input("Enter the amount to withdraw: "))
    initbalance = withdraw(initbalance, amount)
elif op == "4":
    print("Thank you for using our ATM")
else:
    print("Invalid choice")
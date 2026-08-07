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

op = input("Enter the choices you want")

    
    
    
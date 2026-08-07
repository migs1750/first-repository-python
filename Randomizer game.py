import random
print("Guessing game number")

x = random.randrange(1,11)
number = int(input("Enter a number: "))

while x != number:
             
             if number > x:
                 print("Too high")
             else:
                 print("Too low")
                 
             number = int(input("Wrong try again. Enter a number: "))
    
print("Congrats its" ,x)

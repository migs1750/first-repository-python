import math
#naka oop na to from fuctions with OOP  
class Calculator:
    def add_num(self , number_1 , number_2):
        return number_1 + number_2
    def sub_num(self , number_1 , number_2):
        return number_1 - number_2
    def mult_num(self , number_1 , number_2):
        return number_1 * number_2
    def div_num(self , number_1 , number_2):
         while number_2 == 0:
            print("Cannot divide by zero")
            number_2 = int(input("Enter another number not zero: "))
            return number_1 / number_2
    
calc = Calculator()

print("Calculator")

choice = input("Calculator or Scientific? (basic calculator/calculator/scientific calculator/scientific/scical): ").lower()

while choice not in ["Basic calculator" , "calculator", "scientific calculator" , "scientific" , "scical" , "calcu"]:
    print("Invalid choice. Enter again.")
    choice = input("Calculator or Scientific? (basic calculator/calculator/scientific calculator/scientific): ").lower()
    
if choice.lower() == 'Basic calculator' or choice == 'calculator' or choice == 'calcu':
    print("OKAY BASIC CALCULATION")
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter another number: "))

    operation = input("Enter your operation (+,-,*, x,/): ").lower()
    while operation not in ['+' , '-' , '*' , '/' , 'x']:
        print("Invalid operand. Enter again.")
        operation = input("Enter your operation (+,-,*, x,/): ").lower()
        
    match operation:
        case "+":
            sum = calc.add_num(number_1 , number_2)
            print(sum)
        case "-":
            diff = calc.sub_num(number_1 , number_2)
            print(diff)
        case "*" | "x" | "X":
            product = calc.mult_num(number_1 , number_2)
            print(product)
        case "/":
           
            quotient = calc.div_num(number_1 , number_2)
            print(quotient)
   
   

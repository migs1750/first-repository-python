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


         #scientifc calculator functions
    def sin_num(self , number_1):
        return math.sin(math.radians(number_1))
    def cos_num(self , number_1):
        return math.cos(math.radians(number_1))
    def tan_num(self , number_1):
        return math.tan(math.radians(number_1))
    def log_num(self , number_1):
        return math.log10(number_1)
    def sqrt_num(self , number_1):
        return math.sqrt(number_1)

calc = Calculator()

print("PYTHON Calculator")

choice = input("Calculator or Scientific? (basic calculator/calculator/scientific calculator/scientific/scical): ").lower()

if choice.lower() == 'basic calculator' or choice == 'calculator' or choice == 'calcu':
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
  #SCIENTIFIC CALCULATOR
if choice.lower() == 'scientific calculator' or choice == 'scientific' or choice == 'scical':
    print("OKAY SCIENTIFIC CALCULATION")

    operation = input("Enter your operation (sin, cos, tan, log, sqrt): ").lower()
    while operation not in ['sin' , 'cos' , 'tan' , 'log' , 'sqrt']:
        print("Invalid operand. Enter again.")
        operation = input("Enter your operation (sin, cos, tan, log, sqrt): ").lower()
        
    match operation:
        case "sin":
            print("Is your number in degrees or radians? (d/r): ")
            angle_type = input().lower()
            while angle_type not in ['d', 'r']:
                print("Invalid input. Enter again.")
                angle_type = input("Is your number in degrees or radians? (d/r): ").lower()
            if angle_type == 'd':
                number_1 = float(input("Enter your number in degrees: "))
                angle_in_radians = math.radians(number_1)
                sin_value = calc.sin_num(angle_in_radians)
                print(sin_value)
            else:
                number_1 = float(input("Enter your number in radians: "))
                angle_in_radians = number_1
                sin_value = calc.sin_num(angle_in_radians)
                print(sin_value)
        case "cos":
            print("Is your number in degrees or radians? (d/r): ")
            angle_type = input().lower()
            while angle_type not in ['d', 'r']:
                print("Invalid input. Enter again.")
                angle_type = input("Is your number in degrees or radians? (d/r): ").lower()
            if angle_type == 'd':
                number_1 = float(input("Enter your number in degrees: "))
                angle_in_radians = math.radians(number_1)
                cos_value = calc.cos_num(angle_in_radians)
                print(cos_value)
            else:
                number_1 = float(input("Enter your number in radians: "))
                angle_in_radians = number_1
                cos_value = calc.cos_num(angle_in_radians)
                print(cos_value)
        case "tan":
            print("Is your number in degrees or radians? (d/r): ")
            angle_type = input().lower()
            while angle_type not in ['d', 'r']:
                print("Invalid input. Enter again.")
                angle_type = input("Is your number in degrees or radians? (d/r): ").lower()
            if angle_type == 'd':
                number_1 = float(input("Enter your number in degrees: "))
                angle_in_radians = math.radians(number_1)
                tan_value = calc.tan_num(angle_in_radians)
                print(tan_value)
            else:
                number_1 = float(input("Enter your number in radians: "))
                angle_in_radians = number_1
                tan_value = calc.tan_num(angle_in_radians)
                print(tan_value)
        case "log":
            number_1 = float(input("Enter your number: "))
            while number_1 <= 0:
                print("Invalid input. Logarithm is only defined for positive numbers.")
                number_1 = float(input("Enter your number: "))
            log_value = calc.log_num(number_1)
            print(log_value)
        case "sqrt":
            number_1 = float(input("Enter your number: "))
            while number_1 < 0:
                print("Invalid input. Square root is only defined for non-negative numbers.")
                number_1 = float(input("Enter your number: "))
            sqrt_value = calc.sqrt_num(number_1)
            print(sqrt_value)
   
   

   

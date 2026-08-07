import math

print("Calculator")
choice = input("Calculator or Scientific? (C/S/c/s): ")

if choice == 'C' or choice == 'c':
    number_1 = int(input("Enter first number: "))
    number_2 = int(input("Enter another number: "))

    operation = input("Enter your operation (+,-,*,/): ")

    match operation:
        case "+":
            print("The sum is:", number_1 + number_2)
        case "-":
            print("The difference is:", number_1 - number_2)
        case "*":
            print("The product is:", number_1 * number_2)
        case "/":
            print("The quotient is:", number_1 / number_2)
        case _:
            print("Invalid operation")

elif choice == "S" or choice == "s":

    operation = input("Enter operation (sin, cos, tan, ln , sqrt, exp): ")

    match operation:

        case "sin":
            unit = input("Degrees or radians? (Deg/deg/Rad/rad): ")

            if unit == "Deg" or unit == "deg":
                angle = float(input("Enter that degree: "))
                radians = math.radians(angle)
                print("Answer:", math.sin(radians))

            elif unit == "Rad" or unit == "rad":
                angle = float(input("Enter that rad here: "))
                
                print("Answer:", math.sin(angle))

            else:
                print("Invalid unit")

        case "cos":
            unit = input("Degrees or radians? (Deg/deg/Rad/rad): ")

            if unit == "Deg" or unit == "deg":
                angle = float(input("Enter that degree: "))
                radians = math.radians(angle)
                print("Answer:", math.cos(radians))

            elif unit == "Rad" or unit == "rad":
                angle = float(input("Enter that rad here: "))
                
                print("Answer:", math.cos(angle))

            else:
                print("Invalid unit")

        case "square root":
            number = int(input("Enter a number: "))
            print("Answer:", math.sqrt(number))

        case "exp":
            number = int(input("Enter a number: "))
            raised_to = int(input("Exponent: "))
            print("Answer:", math.pow(number, raised_to))

        case "ln":
            number = int(input("Enter a number: "))
            print("Answer:", math.log(number))

        case "sqrt":
            number = int(input("Enter a number: "))
            print("Answer:", math.sqrt(number))

else:
    print("Invalid choice")